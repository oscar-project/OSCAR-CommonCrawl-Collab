import re

from urllib.parse import urlparse

from fastwarc.warc import WarcRecordType
from pyspark.sql.types import StructType, StructField, StringType, LongType

from sparkcc_fastwarc import CCFastWarcSparkJob
from import_json import json
from wat_extract_links import ExtractHostLinksJob


class MetaRatingCountJob(CCFastWarcSparkJob):
    """ Count occurrences of `<meta name='rating' content='...'>` or
        the "Rating" HTTP response header using WAT files. FastWARC
        is used to read the WAT files."""

    name = "MetaRatingCount"

    output_schema = StructType([
        StructField("key", StructType([
            StructField("type", StringType(), False),
            StructField("value", StringType(), False),
            StructField("host", StringType(), True),
            StructField("url", StringType(), False)]), False),
        StructField("count", LongType(), False)
    ])

    # process only WAT records
    fastwarc_record_filter = WarcRecordType.metadata

    rx_rating = re.compile(r'^\s*rating\s*$', re.IGNORECASE|re.ASCII)
    HTTP_HEADER_RATING = 'HTTP-header-rating'
    HTML_METATAG_RATING = 'HTML-metatag-rating'

    def init_accumulators(self, session):
        super(MetaRatingCountJob, self).init_accumulators(session)

        sc = session.sparkContext
        self.records_failed = sc.accumulator(0)
        self.records_non_html = sc.accumulator(0)
        self.records_response_wat = sc.accumulator(0)
        self.records_response_wat_parse_failed = sc.accumulator(0)
        self.rating_found = sc.accumulator(0)
        self.rating_html_metatag_found = sc.accumulator(0)
        self.rating_http_header_found = sc.accumulator(0)
        self.rating_http_header_nonhtml_found = sc.accumulator(0)

    def log_accumulators(self, session):
        super(MetaRatingCountJob, self).log_accumulators(session)

        self.log_accumulator(session, self.records_failed,
                             'records failed to process = {}')
        self.log_accumulator(session, self.records_response_wat,
                             'response records WAT = {}')
        self.log_accumulator(session, self.records_response_wat_parse_failed,
                             'records WAT parsing failed = {}')
        self.log_accumulator(session, self.records_non_html,
                             'records not HTML = {}')
        self.log_accumulator(session, self.rating_found,
                             'records with rating = {}')
        self.log_accumulator(session, self.rating_html_metatag_found,
                             'records with rating HTML metatag = {}')
        self.log_accumulator(session, self.rating_http_header_found,
                             'records with rating HTTP header = {}')
        self.log_accumulator(session, self.rating_http_header_nonhtml_found,
                             'records with rating HTTP header not HTML = {}')

    @staticmethod
    def get_host_name(url):
        m = ExtractHostLinksJob.url_parse_host_pattern.match(url)
        if m:
            host = m.group(1)
        else:
            try:
                host = urlparse(url).hostname
            except:
                return None
            if not host:
                return None
        return host.strip().lower()

    def process_record(self, record):
        # Notes:
        # - HTTP headers may include multiple "Rating" headers
        # - WAT records store HTTP headers as JSON objects not preserving multiple
        #   headers, see https://github.com/commoncrawl/ia-web-commons/issues/18

        if not self.is_wat_json_record(record):
            return

        record = json.loads(self.get_payload_stream(record).read())
        try:
            warc_header = record['Envelope']['WARC-Header-Metadata']
            payload = record['Envelope']['Payload-Metadata']
            if 'HTTP-Response-Metadata' not in payload:
                # WAT request or metadata records
                return

            self.records_response_wat.add(1)
            response_metadata = payload['HTTP-Response-Metadata']

            # HTTP header "Rating"
            http_headers = response_metadata['Headers']
            http_header_rating = set()
            url = warc_header['WARC-Target-URI']
            host_name = None
            for header in http_headers:
                if self.rx_rating.match(header):
                    http_header_rating.add(http_headers[header].strip())
            if http_header_rating:
                self.rating_http_header_found.add(1)
                if not host_name:
                    host_name = self.get_host_name(url)
                for val in http_header_rating:
                    yield (self.HTTP_HEADER_RATING, val, host_name, url), 1

            if 'HTML-Metadata' not in response_metadata:
                self.records_non_html.add(1)
                if http_header_rating:
                    self.rating_found.add(1)
                    self.rating_http_header_nonhtml_found.add(1)
                return

            html_metadata = response_metadata['HTML-Metadata']
            html_metatag_rating = set()
            if 'Head' not in html_metadata:
                return
            head = html_metadata['Head']
            if 'Metas' not in head:
                return
            for m in head['Metas']:
                if ('name' in m and
                    self.rx_rating.match(m['name']) and
                    'content' in m):
                    html_metatag_rating.add(m['content'].strip())

            if html_metatag_rating:
                self.rating_html_metatag_found.add(1)
                if not host_name:
                    host_name = self.get_host_name(url)
                for val in html_metatag_rating:
                    yield (self.HTML_METATAG_RATING, val, host_name, url), 1

            if http_header_rating or html_metatag_rating:
                self.rating_found.add(1)

        except KeyError as e:
            self.records_response_wat_parse_failed.add(1)
            self.get_logger().warn("Failed to parse WAT record for %s: %s",
                                   self.get_warc_header(record, 'WARC-Target-URI'),
                                   e)


if __name__ == "__main__":
    job = MetaRatingCountJob()
    job.run()
