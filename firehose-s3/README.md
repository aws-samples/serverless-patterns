# Firehose to S3 Dynamic Partitioning Enabled

This template deploys a Firehose delivery stream that sends events to an S3 Bucket. Events sent to this bucket are dynamically partioned based on the event type.

Events that do not have type defined are sent to the `failed` partition of the delivery bucket.

### References
- [AWS Blog - Firehose Now Supports Dynamic Partitioning to S3](https://aws.amazon.com/blogs/big-data/kinesis-data-firehose-now-supports-dynamic-partitioning-to-amazon-s3/)
- [Firehose API changes - Dynamic Partitioning](https://awsapichanges.info/archive/changes/b90858-firehose.html)
