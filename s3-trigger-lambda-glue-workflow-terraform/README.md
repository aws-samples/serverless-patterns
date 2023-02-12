# AWS S3 to AWS Lambda to AWS Glue workflow

This pattern << explain usage >>

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md). 

## Testing

Call the endpoint retrieved from the `apigatewayv2_api_api_endpoint` output using `curl` or Postman.

```
curl https://wargabe3ei.execute-api.eu-west-1.amazonaws.com

#sample output
{
  "version": 4,
  "terraform_version": "1.2.5",
  "serial": 57,
  "lineage": "6c4b8536-f489-00bd-ed6e-79520365843e",
  "outputs": {
    "S3-Bucket": {
      "value": "s3-landing-7XXXXXXXXXXX",
      "type": "string"
    },
    "cloudwatch_log_group": {
      "value": "/aws/lambda/file_ingestion_trigger_glue_workflow",
      "type": "string"
    },
    "lambda_function_name": {
      "value": "file_ingestion_trigger_glue_workflow",
      "type": "string"
    }
  },
  "resources": [
    {
      "mode": "data",
      "type": "archive_file",
      "name": "lambda_zip_dir",
      "provider": "provider[\"registry.terraform.io/hashicorp/archive\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "excludes": null,
            "id": "d4506d0613b6a83042d0e9a98ad532d54e73765f",
            "output_base64sha256": "RnhXwFThT4l4oVo2Q0l1IRD2hQATJtqSLZrIyw8UGTA=",
            "output_file_mode": null,
            "output_md5": "719c770f2067ffc23d163e3e81c0c308",
            "output_path": "/tmp/file_trigger_lambda-k4xX.zip",
            "output_sha": "d4506d0613b6a83042d0e9a98ad532d54e73765f",
            "output_size": 343,
            "source": [],
            "source_content": null,
            "source_content_filename": null,
            "source_dir": "src",
            "source_file": null,
            "type": "zip"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "archive_file",
      "name": "lambda_zip_file",
      "provider": "provider[\"registry.terraform.io/hashicorp/archive\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "excludes": null,
            "id": "d4506d0613b6a83042d0e9a98ad532d54e73765f",
            "output_base64sha256": "RnhXwFThT4l4oVo2Q0l1IRD2hQATJtqSLZrIyw8UGTA=",
            "output_file_mode": null,
            "output_md5": "719c770f2067ffc23d163e3e81c0c308",
            "output_path": "./lambda.zip",
            "output_sha": "d4506d0613b6a83042d0e9a98ad532d54e73765f",
            "output_size": 343,
            "source": [],
            "source_content": null,
            "source_content_filename": null,
            "source_dir": null,
            "source_file": "./src/app.py",
            "type": "zip"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "aws_caller_identity",
      "name": "current",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "account_id": "7XXXXXXXXXXX",
            "arn": "arn:aws:iam::7XXXXXXXXXXX:user/Admin",
            "id": "7XXXXXXXXXXX",
            "user_id": "AIDA3A2HN6EZQESORIF7I"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "aws_iam_policy_document",
      "name": "AWSLambdaPolicy",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "id": "407721089",
            "json": "{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [\n    {\n      \"Sid\": \"\",\n      \"Effect\": \"Allow\",\n      \"Action\": [\n        \"s3:PutObjectVersionTagging\",\n        \"s3:PutObjectTagging\",\n        \"s3:PutObjectRetention\",\n        \"s3:PutObjectLegalHold\",\n        \"s3:PutObject\",\n        \"s3:List*\",\n        \"s3:GetObject*\",\n        \"s3:GetBucket*\",\n        \"s3:DeleteObject*\",\n        \"s3:Abort*\"\n      ],\n      \"Resource\": \"arn:aws:s3:::s3-landing-7XXXXXXXXXXX\"\n    },\n    {\n      \"Sid\": \"\",\n      \"Effect\": \"Allow\",\n      \"Action\": [\n        \"logs:PutLogEvents\",\n        \"logs:CreateLogStream\",\n        \"logs:CreateLogGroup\"\n      ],\n      \"Resource\": \"arn:aws:logs:us-east-1:7XXXXXXXXXXX:log-group:/aws/lambda/file_ingestion_trigger_glue_workflow\"\n    }\n  ]\n}",
            "override_json": null,
            "override_policy_documents": null,
            "policy_id": null,
            "source_json": null,
            "source_policy_documents": null,
            "statement": [
              {
                "actions": [
                  "s3:Abort*",
                  "s3:DeleteObject*",
                  "s3:GetBucket*",
                  "s3:GetObject*",
                  "s3:List*",
                  "s3:PutObject",
                  "s3:PutObjectLegalHold",
                  "s3:PutObjectRetention",
                  "s3:PutObjectTagging",
                  "s3:PutObjectVersionTagging"
                ],
                "condition": [],
                "effect": "Allow",
                "not_actions": [],
                "not_principals": [],
                "not_resources": [],
                "principals": [],
                "resources": [
                  "arn:aws:s3:::s3-landing-7XXXXXXXXXXX"
                ],
                "sid": ""
              },
              {
                "actions": [
                  "logs:CreateLogGroup",
                  "logs:CreateLogStream",
                  "logs:PutLogEvents"
                ],
                "condition": [],
                "effect": "Allow",
                "not_actions": [],
                "not_principals": [],
                "not_resources": [],
                "principals": [],
                "resources": [
                  "arn:aws:logs:us-east-1:7XXXXXXXXXXX:log-group:/aws/lambda/file_ingestion_trigger_glue_workflow"
                ],
                "sid": ""
              }
            ],
            "version": "2012-10-17"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "aws_iam_policy_document",
      "name": "AWSLambdaTrustPolicy",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "id": "3693445097",
            "json": "{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [\n    {\n      \"Sid\": \"\",\n      \"Effect\": \"Allow\",\n      \"Action\": \"sts:AssumeRole\",\n      \"Principal\": {\n        \"Service\": \"lambda.amazonaws.com\"\n      }\n    }\n  ]\n}",
            "override_json": null,
            "override_policy_documents": null,
            "policy_id": null,
            "source_json": null,
            "source_policy_documents": null,
            "statement": [
              {
                "actions": [
                  "sts:AssumeRole"
                ],
                "condition": [],
                "effect": "Allow",
                "not_actions": [],
                "not_principals": [],
                "not_resources": [],
                "principals": [
                  {
                    "identifiers": [
                      "lambda.amazonaws.com"
                    ],
                    "type": "Service"
                  }
                ],
                "resources": [],
                "sid": ""
              }
            ],
            "version": "2012-10-17"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "aws_region",
      "name": "current",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "description": "US East (N. Virginia)",
            "endpoint": "ec2.us-east-1.amazonaws.com",
            "id": "us-east-1",
            "name": "us-east-1"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_cloudwatch_log_group",
      "name": "lambda_demo_loggroup",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:logs:us-east-1:7XXXXXXXXXXX:log-group:/aws/lambda/file_ingestion_trigger_glue_workflow",
            "id": "/aws/lambda/file_ingestion_trigger_glue_workflow",
            "kms_key_id": "",
            "name": "/aws/lambda/file_ingestion_trigger_glue_workflow",
            "name_prefix": "",
            "retention_in_days": 365,
            "skip_destroy": false,
            "tags": {},
            "tags_all": {}
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_iam_role.terraform_function_role",
            "aws_lambda_function.file_ingestion_trigger_glue_workflow",
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir",
            "data.aws_caller_identity.current",
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy",
            "random_string.randomstring_fileingestion"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_iam_policy",
      "name": "lambda_policy",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:iam::7XXXXXXXXXXX:policy/lambda_policy",
            "description": "Policy to access S3",
            "id": "arn:aws:iam::7XXXXXXXXXXX:policy/lambda_policy",
            "name": "lambda_policy",
            "name_prefix": null,
            "path": "/",
            "policy": "{\"Statement\":[{\"Action\":[\"s3:PutObjectVersionTagging\",\"s3:PutObjectTagging\",\"s3:PutObjectRetention\",\"s3:PutObjectLegalHold\",\"s3:PutObject\",\"s3:List*\",\"s3:GetObject*\",\"s3:GetBucket*\",\"s3:DeleteObject*\",\"s3:Abort*\"],\"Effect\":\"Allow\",\"Resource\":\"arn:aws:s3:::s3-landing-7XXXXXXXXXXX\",\"Sid\":\"\"},{\"Action\":[\"logs:PutLogEvents\",\"logs:CreateLogStream\",\"logs:CreateLogGroup\"],\"Effect\":\"Allow\",\"Resource\":\"arn:aws:logs:us-east-1:7XXXXXXXXXXX:log-group:/aws/lambda/file_ingestion_trigger_glue_workflow\",\"Sid\":\"\"}],\"Version\":\"2012-10-17\"}",
            "policy_id": "ANPA3A2HN6EZRBJAVQB4U",
            "tags": {},
            "tags_all": {}
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_cloudwatch_log_group.lambda_demo_loggroup",
            "aws_iam_role.terraform_function_role",
            "aws_lambda_function.file_ingestion_trigger_glue_workflow",
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir",
            "data.aws_caller_identity.current",
            "data.aws_iam_policy_document.AWSLambdaPolicy",
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy",
            "random_string.randomstring_fileingestion"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_iam_role",
      "name": "terraform_function_role",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:iam::7XXXXXXXXXXX:role/terraform_function_role",
            "assume_role_policy": "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"lambda.amazonaws.com\"},\"Sid\":\"\"}],\"Version\":\"2012-10-17\"}",
            "create_date": "2023-02-12T03:48:18Z",
            "description": "",
            "force_detach_policies": false,
            "id": "terraform_function_role",
            "inline_policy": [],
            "managed_policy_arns": [
              "arn:aws:iam::7XXXXXXXXXXX:policy/lambda_policy"
            ],
            "max_session_duration": 3600,
            "name": "terraform_function_role",
            "name_prefix": "",
            "path": "/",
            "permissions_boundary": null,
            "tags": {},
            "tags_all": {},
            "unique_id": "AROA3A2HN6EZ7SN6Y4KSJ"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_iam_role_policy_attachment",
      "name": "terraform_lambda_policy",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "id": "terraform_function_role-20230212035041462900000001",
            "policy_arn": "arn:aws:iam::7XXXXXXXXXXX:policy/lambda_policy",
            "role": "terraform_function_role"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_cloudwatch_log_group.lambda_demo_loggroup",
            "aws_iam_policy.lambda_policy",
            "aws_iam_role.terraform_function_role",
            "aws_lambda_function.file_ingestion_trigger_glue_workflow",
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir",
            "data.aws_caller_identity.current",
            "data.aws_iam_policy_document.AWSLambdaPolicy",
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy",
            "random_string.randomstring_fileingestion"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_lambda_function",
      "name": "file_ingestion_trigger_glue_workflow",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "architectures": [
              "x86_64"
            ],
            "arn": "arn:aws:lambda:us-east-1:7XXXXXXXXXXX:function:file_ingestion_trigger_glue_workflow",
            "code_signing_config_arn": "",
            "dead_letter_config": [],
            "description": "",
            "environment": [],
            "ephemeral_storage": [
              {
                "size": 2048
              }
            ],
            "file_system_config": [],
            "filename": null,
            "function_name": "file_ingestion_trigger_glue_workflow",
            "handler": "file_ingestion_trigger_glue_workflow.lambda_handler",
            "id": "file_ingestion_trigger_glue_workflow",
            "image_config": [],
            "image_uri": "",
            "invoke_arn": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:7XXXXXXXXXXX:function:file_ingestion_trigger_glue_workflow/invocations",
            "kms_key_arn": "",
            "last_modified": "2023-02-12T03:48:33.743+0000",
            "layers": [],
            "memory_size": 512,
            "package_type": "Zip",
            "publish": false,
            "qualified_arn": "arn:aws:lambda:us-east-1:7XXXXXXXXXXX:function:file_ingestion_trigger_glue_workflow:$LATEST",
            "qualified_invoke_arn": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:7XXXXXXXXXXX:function:file_ingestion_trigger_glue_workflow:$LATEST/invocations",
            "replace_security_groups_on_destroy": null,
            "replacement_security_group_ids": null,
            "reserved_concurrent_executions": -1,
            "role": "arn:aws:iam::7XXXXXXXXXXX:role/terraform_function_role",
            "runtime": "python3.9",
            "s3_bucket": "s3-landing-7XXXXXXXXXXX",
            "s3_key": "lambda_scripts/file_ingestion_trigger_glue_workflow.zip",
            "s3_object_version": null,
            "signing_job_arn": "",
            "signing_profile_version_arn": "",
            "snap_start": [],
            "source_code_hash": "RnhXwFThT4l4oVo2Q0l1IRD2hQATJtqSLZrIyw8UGTA=",
            "source_code_size": 343,
            "tags": {},
            "tags_all": {},
            "timeout": 900,
            "timeouts": null,
            "tracing_config": [
              {
                "mode": "PassThrough"
              }
            ],
            "version": "$LATEST",
            "vpc_config": []
          },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjo2MDAwMDAwMDAwMDAsInVwZGF0ZSI6NjAwMDAwMDAwMDAwfX0=",
          "dependencies": [
            "aws_iam_role.terraform_function_role",
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir",
            "data.aws_caller_identity.current",
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy",
            "random_string.randomstring_fileingestion"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_lambda_permission",
      "name": "file_lambda_permission",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "action": "lambda:InvokeFunction",
            "event_source_token": null,
            "function_name": "file_ingestion_trigger_glue_workflow",
            "function_url_auth_type": null,
            "id": "AllowS3Invoke",
            "principal": "s3.amazonaws.com",
            "principal_org_id": null,
            "qualifier": "",
            "source_account": null,
            "source_arn": "arn:aws:s3:::s3-landing-7XXXXXXXXXXX",
            "statement_id": "AllowS3Invoke",
            "statement_id_prefix": ""
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_iam_role.terraform_function_role",
            "aws_lambda_function.file_ingestion_trigger_glue_workflow",
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir",
            "data.aws_caller_identity.current",
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy",
            "random_string.randomstring_fileingestion"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_s3_bucket",
      "name": "landing_bucket",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "acceleration_status": "",
            "acl": null,
            "arn": "arn:aws:s3:::s3-landing-7XXXXXXXXXXX",
            "bucket": "s3-landing-7XXXXXXXXXXX",
            "bucket_domain_name": "s3-landing-7XXXXXXXXXXX.s3.amazonaws.com",
            "bucket_prefix": null,
            "bucket_regional_domain_name": "s3-landing-7XXXXXXXXXXX.s3.amazonaws.com",
            "cors_rule": [],
            "force_destroy": false,
            "grant": [
              {
                "id": "1c0737c3b51efc591a5a99f158264f325de9501754deeef4cdf35a598d3ef1ed",
                "permissions": [
                  "FULL_CONTROL"
                ],
                "type": "CanonicalUser",
                "uri": ""
              }
            ],
            "hosted_zone_id": "Z3AQBSTGFYJSTF",
            "id": "s3-landing-7XXXXXXXXXXX",
            "lifecycle_rule": [],
            "logging": [],
            "object_lock_configuration": [],
            "object_lock_enabled": false,
            "policy": "",
            "region": "us-east-1",
            "replication_configuration": [],
            "request_payer": "BucketOwner",
            "server_side_encryption_configuration": [],
            "tags": {},
            "tags_all": {},
            "timeouts": null,
            "versioning": [
              {
                "enabled": false,
                "mfa_delete": false
              }
            ],
            "website": [],
            "website_domain": null,
            "website_endpoint": null
          },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjoxMjAwMDAwMDAwMDAwLCJkZWxldGUiOjM2MDAwMDAwMDAwMDAsInJlYWQiOjEyMDAwMDAwMDAwMDAsInVwZGF0ZSI6MTIwMDAwMDAwMDAwMH19",
          "dependencies": [
            "data.aws_caller_identity.current"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_s3_bucket_notification",
      "name": "aws-lambda-trigger",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "bucket": "s3-landing-7XXXXXXXXXXX",
            "eventbridge": false,
            "id": "s3-landing-7XXXXXXXXXXX",
            "lambda_function": [
              {
                "events": [
                  "s3:ObjectCreated:*"
                ],
                "filter_prefix": "",
                "filter_suffix": "",
                "id": "tf-s3-lambda-20230212034833586300000001",
                "lambda_function_arn": "arn:aws:lambda:us-east-1:7XXXXXXXXXXX:function:file_ingestion_trigger_glue_workflow"
              }
            ],
            "queue": [],
            "topic": []
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_iam_role.terraform_function_role",
            "aws_lambda_function.file_ingestion_trigger_glue_workflow",
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir",
            "data.aws_caller_identity.current",
            "data.aws_iam_policy_document.AWSLambdaTrustPolicy",
            "random_string.randomstring_fileingestion"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_s3_object",
      "name": "lambda_code_upload",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "acl": "private",
            "bucket": "s3-landing-7XXXXXXXXXXX",
            "bucket_key_enabled": false,
            "cache_control": "",
            "content": null,
            "content_base64": null,
            "content_disposition": "",
            "content_encoding": "",
            "content_language": "",
            "content_type": "binary/octet-stream",
            "etag": "719c770f2067ffc23d163e3e81c0c308",
            "force_destroy": false,
            "id": "lambda_scripts/file_ingestion_trigger_glue_workflow.zip",
            "key": "lambda_scripts/file_ingestion_trigger_glue_workflow.zip",
            "kms_key_id": null,
            "metadata": {},
            "object_lock_legal_hold_status": "",
            "object_lock_mode": "",
            "object_lock_retain_until_date": "",
            "server_side_encryption": "",
            "source": "/tmp/file_trigger_lambda-k4xX.zip",
            "source_hash": null,
            "storage_class": "STANDARD",
            "tags": {},
            "tags_all": {},
            "version_id": "",
            "website_redirect": ""
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_s3_bucket.landing_bucket",
            "data.archive_file.lambda_zip_dir"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "random_string",
      "name": "randomstring_fileingestion",
      "provider": "provider[\"registry.terraform.io/hashicorp/random\"]",
      "instances": [
        {
          "schema_version": 2,
          "attributes": {
            "id": "k4xX",
            "keepers": null,
            "length": 4,
            "lower": true,
            "min_lower": 0,
            "min_numeric": 0,
            "min_special": 0,
            "min_upper": 0,
            "number": true,
            "numeric": true,
            "override_special": null,
            "result": "k4xX",
            "special": false,
            "upper": true
          },
          "sensitive_attributes": []
        }
      ]
    }
  ]
}

```

Then check the logs for the Lambda function from the Lambda console.

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 4.9 |
| <a name="requirement_random"></a> [random](#requirement\_random) | >= 2.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_random"></a> [random](#provider\_random) | >= 2.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_api_gateway"></a> [api\_gateway](#module\_api\_gateway) | terraform-aws-modules/apigateway-v2/aws | ~> 2.0 |
| <a name="module_lambda_function"></a> [lambda\_function](#module\_lambda\_function) | terraform-aws-modules/lambda/aws | ~> 4.0 |

## Resources

| Name | Type |
|------|------|
| [random_pet.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet) | resource |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_apigatewayv2_api_api_endpoint"></a> [apigatewayv2\_api\_api\_endpoint](#output\_apigatewayv2\_api\_api\_endpoint) | The URI of the API |
| <a name="output_lambda_function_arn"></a> [lambda\_function\_arn](#output\_lambda\_function\_arn) | The ARN of the Lambda Function |
| <a name="output_lambda_function_invoke_arn"></a> [lambda\_function\_invoke\_arn](#output\_lambda\_function\_invoke\_arn) | The Invoke ARN of the Lambda Function |
| <a name="output_lambda_function_name"></a> [lambda\_function\_name](#output\_lambda\_function\_name) | The name of the Lambda Function |
| <a name="output_lambda_function_qualified_arn"></a> [lambda\_function\_qualified\_arn](#output\_lambda\_function\_qualified\_arn) | The ARN identifying your Lambda Function Version |
| <a name="output_lambda_function_version"></a> [lambda\_function\_version](#output\_lambda\_function\_version) | Latest published version of Lambda Function |
| <a name="output_lambda_role_arn"></a> [lambda\_role\_arn](#output\_lambda\_role\_arn) | The ARN of the IAM role created for the Lambda Function |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd _patterns-model
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Explain how the service interaction works.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
