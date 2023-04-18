# #  TODO - Create SNS notification for and failed jobs
# resource "aws_sns_topic" "sample_sfn_status" {
#   # count = var.sample_enable_sns ? 1 : 0
#   name = "sample_sfn_status"
# }

# // IMPORTANT - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sns_topic_subscription
# resource "aws_sns_topic_subscription" "sample_sfn_status_sqs_target" {
#   # count     = var.sample_enable_sns ? 1 : 0
#   topic_arn = aws_sns_topic.sample_sfn_status.arn
#   protocol  = "email"
#   # protocol  = "email-json"
#   endpoint = var.sample_sns_email_endpoint
# }
