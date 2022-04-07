# New format benchmarks


Commit versions:

- jsonl: [a266fa3](https://github.com/oscar-corpus/ungoliant/commit/a266fa321f5ed168d613bd8a190d90179520fc4a)
- avro: [14fb3f7](https://github.com/oscar-corpus/ungoliant/commit/14fb3f7b6ef540b12f3278ff0aff7e0aa07278ce)
- parquet: TODO


| Format        | Platform   | Num. shards | Input size | Gen time                   | Output size | Get content length of clean docs |
|---------------|------------|-------------|------------|----------------------------|-------------|----------------------------------|
| **jsonl**     | **laptop** | 25          | 3.1G       | **190,6±2.1s (3 samples)** | **3.6G**    | **975ms**                        |
| avro (snappy) | laptop     | 25          | 3.1G       | 195,3±3.2s (3 samples)     | 1.8G        | 1.9s                             |
| jsonl         | HPC        | 100         | TODO       | TODO                       | TODO        | TODO                             |
| avro (snappy) | HPC        | 100         | TODO       | TODO                       | TODO        | TODO                             |
| parquet       | laptop     | 25          | 3.1G       | TODO                       | TODO        | TODO                             |
| parquet       | HPC        | 100         | TODO       | TODO                       | TODO        | TODO                             |
