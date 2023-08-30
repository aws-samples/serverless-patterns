/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/kinesisanalytics/main.tf ---

# Access the effective Account ID
data "aws_caller_identity" "current" {}

# Setting Account ID
locals {
    account_id = data.aws_caller_identity.current.account_id
}

# Create Kinesis Analytics Application
resource "aws_kinesisanalyticsv2_application" "kinesis_analytics_application" {
    name                   = var.kinesis_analytics_application
    runtime_environment    = var.kinesis_analytics_application_runtime
    service_execution_role = aws_iam_role.iam_role_for_kinesis_analytics.arn

    application_configuration {
        application_code_configuration {
          code_content {
            s3_content_location {
                bucket_arn = var.bucket_arn
                file_key   = var.file_key
            }
          }
          code_content_type = var.code_content_type       
        }
    
      environment_properties {
        property_group {
          property_group_id = var.consumer_property_group

          property_map = {
            "input.stream.name"   = var.stream_name
            "aws.region"          = var.region
            "scan.stream.initpos" = var.scan_stream_initpos
          }
        }

        property_group {
          property_group_id = var.application_runtime_options

          property_map = {
            "python"  = var.python_code_file
            "jarfile" = var.jar_file
          }
        }

        property_group {
          property_group_id = var.sink_config

          property_map = {
            "output.bucket.name"  = var.bucket_name
          }
        }
      }

      flink_application_configuration {
        checkpoint_configuration {
          configuration_type = var.checkpoint_configuration_type
        } 

        monitoring_configuration {
          configuration_type = var.monitoring_configuration_type
          log_level          = var.log_level
          metrics_level      = var.metrics_level
        }

        parallelism_configuration {
          auto_scaling_enabled = var.auto_scaling_enabled
          configuration_type   = var.parallelism_configuration_type
          parallelism          = var.parallelism
          parallelism_per_kpu  = var.parallelism_per_kpu
        }
      }  
    }

    cloudwatch_logging_options {
      log_stream_arn = aws_cloudwatch_log_stream.log_stream.arn
    } 
}

# IAM Role for Kinesis Analytics 
resource "aws_iam_role" "iam_role_for_kinesis_analytics" {
    name               = "iam_role_for_kinesis_analytics"
    assume_role_policy = templatefile("${path.module}/iam_role_for_kinesis_analytics.tftpl", 
                                        {aws_region      = var.region, 
                                        account_id       = local.account_id, 
                                        application_name = var.kinesis_analytics_application})
}

# IAM Policy for Kinesis Analytics
resource "aws_iam_policy" "iam_policy_for_kinesis_analytics" {
    name   = "iam_policy_for_kinesis_analytics"
    policy = templatefile("${path.module}/iam_policy_for_kinesis_analytics.tftpl", 
                            {account_id      = local.account_id, 
                            s3_bucket_arn    = var.bucket_arn, 
                            aws_region       = var.region, 
                            application_name = var.kinesis_analytics_application, 
                            stream_name      = var.stream_name
                            file_key         = var.file_key
                            log_stream_name  = var.log_stream})
}

# Attach IAM Role with IAM Policy for Kinesis Analytics
resource "aws_iam_role_policy_attachment" "attach_iam_role_with_iam_policy" {
    policy_arn = aws_iam_policy.iam_policy_for_kinesis_analytics.arn
    role       = aws_iam_role.iam_role_for_kinesis_analytics.name
}

# Create Cloudwatch Log Group
resource "aws_cloudwatch_log_group" "cloudwatch_log_group" {
  name              = "/aws/kinesis-analytics/${var.kinesis_analytics_application}" 
  retention_in_days = 1
}

# Create Cloudwatch Log Stream
resource "aws_cloudwatch_log_stream" "log_stream" {
  name           = var.log_stream
  log_group_name = aws_cloudwatch_log_group.cloudwatch_log_group.name
}