# Parquet

## General introductions
- Data Engineering Podcast, Episode 8, Data Serialization Formats with Doug Cutting and Julien Le Dem
  https://www.dataengineeringpodcast.com/data-serialization-with-doug-cutting-and-julien-le-dem-episode-8/
- Owen O'Malley, Fast Access To Your Complex Data - Avro, JSON, ORC, and Parquet
  https://2018.berlinbuzzwords.de/18/session/fast-access-your-complex-data-avro-json-orc-and-parquet.html
- https://eng.uber.com/cost-efficiency-big-data/
  - recommendations: use zstd, column sorting, remove large unused columns

## Compression
- compression benchmarks
  - https://peazip.github.io/fast-compression-benchmark-brotli-zstandard.html
  - https://quixdb.github.io/squash-benchmark/

## Querying
- [Presto](https://prestodb.io/) / [Athena](https://aws.amazon.com/athena/)
- [Spark](https://spark.apache.org/)
- [Duckdb](https://duckdb.org/2021/06/25/querying-parquet.html)
- [PostgreSQL Parquet file wrapper](https://github.com/adjust/parquet_fdw/)
- [SQLite Parquet virtual table](https://github.com/cldellow/sqlite-parquet-vtable/), see also [query Parquet files in SQLite](https://cldellow.com/2018/06/22/sqlite-parquet-vtable.html)

## Text corpora in Parquet and columnar formats
- https://ids-pub.bsz-bw.de/frontdoor/deliver/index/docId/6261/file/McClure_etal_Organizing_corpora_2017.pdf
- Wikiparq - https://aclanthology.org/L16-1654/
  - https://fileadmin.cs.lth.se/nlp/Marcus_PhD_Print_Thesis.pdf

## Parquet for web archives
- https://zenodo.org/record/3633290
  - https://github.com/archivesunleashed/notebooks/blob/main/datathon-nyc/parquet_pandas_stonewall.ipynb
  - https://colab.research.google.com/github/archivesunleashed/notebooks/blob/colab-tweak/Parquet%20Examples/parquet_text_analyis.ipynb
- https://arxiv.org/pdf/2003.14046.pdf
- https://digital.library.unt.edu/ark:/67531/metadc1608961/m1/1/

## Various data format specifications based on Parquet

- [GeoParquet](https://github.com/opengeospatial/geoparquet)

## See also

- [Parquet – a column-oriented file format](../slides/columnar-storage-parquet.pdf) (slides 2022-04-22)