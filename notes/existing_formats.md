# Existing formats

_Note: This is a simple bullet-point list of facts about WARC, Parquet and Avro file formats._


What this document is:

A short, informal comparison of different file formats put in context of OSCAR and CommonCrawl


## WARC (Web ARCHIVE)
- Accepted standard of web archival ([WARC 1.1](https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/))
- Easy to read
- Optional per-record compression (gzip)
- “Row-oriented”, since each record is appended to the others
- May be less practical for nested metadata
- Rust lib: jedireza/warc, 22 stars, active


## Avro
- Apache project (https://avro.apache.org/)
- Row-oriented
- Binary, compression built-in
- Appendable, easy to write to
- Tiny
- Already used in Ungoliant for rebuilding files (“shard_id” => [“records_to_get”, “identifications”]
- Rust lib: apache/avro, 2.1k stars, active

## Parquet
- Apache project (https://parquet.apache.org/)
- Column oriented
- Binary, compression built-in
- Not append/modification friendly
- Built to last? cf. [this](https://stackoverflow.com/questions/56472727/difference-between-apache-parquet-and-arrow/56481636#56481636) stackoverflow response
- Interop. with arrow, a parquet-like format geared towards in memory storage.
- Rust lib: apache/arrow-rs, 800 stars, active, incomplete (missing row writer, async write)

## ORC
- Apache project (https://orc.apache.org/)
- Similar to Parquet



We should see the performance of the worst case scenarios (iterating over records with parquet)
