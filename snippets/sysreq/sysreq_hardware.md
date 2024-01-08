The following machine recommendations are for installing individual PADAS components:

| Component   | Storage   | Memory    | CPU   | Nodes   |
| ----------- | --------- | --------- | ----- | ------- |
| Engine      | SSD storage is recommended.  Disk size depends on the number of transformations and queries. For evaluation/test/dev 10-20GB should be sufficient. | 12GB (64GB recommended) | 4 CPU cores or more | 1 to many instances can be deployed depending on number of Kafka topic partition count and scalability requirements|
| User Interface | 50GB, preferably SSD | 2GB | 1 CPU core or more | 1 |