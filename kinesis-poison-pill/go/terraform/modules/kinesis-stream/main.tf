//Create kinesis stream

resource "aws_kinesis_stream" "kinesis-stream" {
  name                      = "kinesis-stream"
  shard_count               = var.shard_count
}