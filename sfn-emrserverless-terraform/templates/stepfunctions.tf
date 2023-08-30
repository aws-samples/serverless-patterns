resource "aws_sfn_state_machine" "sfn_state_machine" {
  name     = "${var.app}-${var.stage_name}-state-machine"
  role_arn = aws_iam_role.lambda_emr_sfn_start_job_role.arn
  tags = {
    Name        = "State Machine"
    Environment = var.stage_name
    Application = var.app
  }

  definition = <<EOF
{
  "Comment": "Workflow to trigger an EMR Serverless Job.",
  "StartAt": "StartEMRServerlessJob",
  "States": {
    "StartEMRServerlessJob": {
     "Type": "Task",
      "Resource": "arn:aws:states:::aws-sdk:emrserverless:startJobRun",
      "ResultPath": "$.Job.Input",
      "Next": "GetJobStatus",
      "Parameters": {
        "ApplicationId": "${aws_emrserverless_application.emr_serverless.id}",
        "ClientToken.$": "States.UUID()",
        "Name": "${aws_emrserverless_application.emr_serverless.name}",
        "ExecutionRoleArn": "${aws_iam_role.emr_serverless_role.arn}",
        "JobDriver": {
          "SparkSubmit": {
            "EntryPoint": "s3://${aws_s3_bucket.job_source_s3_bucket.id}/${var.jar_name}",
            "EntryPointArguments.$": "States.Array($.InputDate, 'us-east-1-clicklogger-dev-firehose-delivery-078876706719', 'us-east-1-pattern-sfn-emrserverless-dev-output-078876706719')",
            "SparkSubmitParameters": "--class com.examples.clicklogger.Loggregator"
          }
        }
     }
    },
    "GetJobStatus": {
        "Next": "CheckJobSuccess",
        "Type": "Task",
        "ResultPath": "$.Job.Status",
        "Resource": "arn:aws:states:::aws-sdk:emrserverless:getJobRun",
        "Parameters": {
          "ApplicationId": "${aws_emrserverless_application.emr_serverless.id}",
          "JobRunId.$": "$.Job.Input.JobRunId"
        }
      },
      "Wait": {
        "Type": "Wait",
        "Seconds": 20,
        "Next": "GetJobStatus"
      },
      "CheckJobSuccess": {
        "Type": "Choice",
        "Choices": [
          {
            "And": [
              {
                "Variable": "$.Job.Status",
                "IsPresent": true
              },
              {
                "Or": [
                  {
                    "Variable": "$.Job.Status.JobRun.State",
                    "StringEquals": "SUCCESS"
                  }
                ]
              }
            ],
            "Next": "Success"
          }
        ],
        "Default": "CheckJobFailure"
      },
      "CheckJobFailure": {
        "Type": "Choice",
        "Choices": [
          {
            "And": [
              {
                "Variable": "$.Job.Status",
                "IsPresent": true
              },
              {
                "Or": [
                  {
                    "Variable": "$.Job.Status.JobRun.State",
                    "StringEquals": "CANCELLED"
                  },
                  {
                    "Variable": "$.Job.Status.JobRun.State",
                    "StringEquals": "FAILED"
                  }
                ]
              }
            ],
            "Next": "Failure"
          }
        ],
        "Default": "Wait"
      },
      "Failure": {
        "Type": "Fail"
      },
      "Success": {
        "Type": "Succeed"
      }
    }
}
EOF
}
