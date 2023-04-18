# // TODO - Edit this to simply do the following:
// - Copy file from landing bucket to input bucket with UUID added
// - Copy file from input bucket to output bucket
// - Write the S3 file metadata to DynamoDB

resource "random_uuid" "sample_file_uuid" {
}

resource "aws_sfn_state_machine" "sample_sfn_state_machine" {
  # // prevents timeout error for deletion of sfn state machine
  # // this operation can take a while to complete
  # timeouts {
  #   delete = "20m"
  # }
  name     = var.sample_sfn_state_machine_name
  role_arn = aws_iam_role.sample_step_functions_master_restricted_access[0].arn
  definition = jsonencode({
    Comment = "A State Machine that processes files with and writes metadata to DynamoDB"
    StartAt = var.sample_sfn_state_generate_uuid_name
    States = merge(
      # - Generate UUID -
      # Generates a UUID from S3 PutObject id
      {
        "${var.sample_sfn_state_generate_uuid_name}" = {
          Type = "Pass",
          Result = {
            "uuid.$" = "$.id"
          }
          ResultPath = "$.taskresult"
          Next       = "${var.sample_sfn_state_get_sample_input_file_name}"
        }
      },

      # - CopyToAppStorage -
      {
        CopyToAppStorage = {
          Type       = "Task",
          Resource   = "arn:aws:states:::aws-sdk:s3:copyObject",
          ResultPath = "$.getS3Output"
          Parameters = {
            Bucket         = "${aws_s3_bucket.sample_app_storage_bucket.id}",
            "Key.$"        = "States.Format('{}-{}',$.detail.object.key, $.id)",                                        // reference object key from InputPath and add uuid
            "CopySource.$" = "States.Format('${aws_s3_bucket.sample_input_bucket.id}/{}-{}',$.detail.object.key, $.id)" // reference bucket name and object path from InputPath
          },
          Next = "WriteToDynamoDB"
        }
      },

      # # - PrepareS3ObjectMetadata -
      # {
      #   PrepareS3ObjectMetadata = {
      #     Type = "Pass",
      #     Parameters = {
      #       ResultSelector = {
      #         "fileMetadata.$" = "$.CallAnalyticsJob",
      #         "fileContent.$"  = "States.StringToJson($.getS3ObjectMetadata.Body)",
      #       }
      #     }
      #     Next = "WriteToDynamoDB"
      #   }
      # },

      # - WriteToDynamoDB -
      {
        WriteToDynamoDB = {
          Type       = "Task",
          Resource   = "arn:aws:states:::aws-sdk:dynamodb:putItem"
          Comment    = "Write the S3 Object metadata to DynamoDB"
          ResultPath = "$.DynamoDB"
          Parameters = {
            TableName = "${aws_dynamodb_table.sample_output.id}"
            # IMPORTANT - Even if your value is not a string, you need to put a string value.
            # The data type ("N","S", etc.) will identify it as the type you describe
            # Note - the data type "SS" as of October 2022 is not supported by Step Functions
            Item = {
              # Column = {
              #   S = "id"
              # }
              ObjectId = {
                "S.$" = "$.id"
              },
              Version = {
                "S.$" = "$.version"
              },
              DetailType = {
                "S.$" = "$.detail-type"
              },
              Source = {
                "S.$" = "$.source"
              },
              AccountId = {
                "S.$" = "$.account"
              },
              CreatedAt = {
                "S.$" = "$.time"
              },
              Region = {
                "S.$" = "$.region"
              },
              CurrentBucket = {
                "S.$" = "States.Format('${aws_s3_bucket.sample_app_storage_bucket.id}')"
              },
              FileName = {
                "S.$" = "$.detail.object.key"
              },
              # FileName = {
              #   "S.$" = "States.Format('{}-{}', $.detail.object.key, $.id)"
              # },
              FilePath = {
                "S.$" = "States.Format('s3://${aws_s3_bucket.sample_app_storage_bucket.id}/{}-{}', $.detail.object.key, $.id)"
              },
              // SS - String Set (i.e. an array of strings)
              // NS - Number Set (i.e. an array of numbers)
              OriginalBucket = {
                "S.$" = "States.JsonToString($.resources)"
              },
              ObjectSize = {
                "N.$" = "States.JsonToString($.detail.object.size)"
              },
              SourceIPAddress = {
                "S.$" = "$.detail.source-ip-address"
              },
              LifecycleConfig = {
                "S.$" = "$.getSampleInputStateOutput.Expiration"
              },
            }
          }
          Next = "Success"
        }
      },


      # # - FailSNS -
      # {
      #   FailSNS = {
      #     Type     = "Task",
      #     Resource = "arn:aws:states:::aws-sdk:sns:publish"
      #     # Resource = "arn:aws:states:::sns:publish"
      #     Comment = "This is part of the polling loop that gets the TCA job nam to be used with the choice state"
      #     Parameters = {
      #       # "Message.$" = "$"
      #       Message  = "The TCA Step Function has failed. Please check the logs and try to re-upload your media."
      #       TopicArn = "${aws_sns_topic.sample_sfn_status.arn}"
      #     }
      #     Next = "Fail"
      #   }
      # },


      # - Success End State -
      {
        Success = {
          Type = "Succeed"
        },

      },

      # # # - Fail End State -
      # {
      #   Fail = {
      #     Type = "Fail"
      #   },

      # },

      // GetSampleInputFile
      coalesce((var.create_sample_sfn_state_get_sample_input_file) ? {
        # (var.sample_sfn_state_get_sample_input_file_name) = {
        "${var.sample_sfn_state_get_sample_input_file_name}" = {
          Type       = "Task",
          Resource   = "arn:aws:states:::aws-sdk:s3:copyObject",
          ResultPath = "$.getSampleInputStateOutput"
          Parameters = {
            Bucket         = "${aws_s3_bucket.sample_input_bucket.id}",
            "Key.$"        = "States.Format('{}-{}',$.detail.object.key, $.id)",               // reference object key from InputPath and add uuid
            "CopySource.$" = "States.Format('{}/{}',$.detail.bucket.name,$.detail.object.key)" // reference bucket name and object path from InputPath
          },
          Next = "CopyToAppStorage"
        },
      } : null, {}),

      # ---- TEMPLATE FOR OPTIONAL STATE MACHINE STATES ----
      # coalesce(var.condition ? {
      #   # (conditional attributes here)
      # } : null, {}),




    )
  })
}



