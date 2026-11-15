//Output Kinesis Stream ARN
output "kinesis_stream_arn" {
    value       = aws_kinesis_stream.kinesis-stream.arn
    description = "kinesis_stream_arn"
}