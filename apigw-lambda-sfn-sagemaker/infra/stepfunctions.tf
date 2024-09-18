resource "aws_sfn_state_machine" "manage_sagemaker" {
  name       = "manage_sagemaker_workflow"
  role_arn   = aws_iam_role.stepfunctions_role.arn
  definition = <<EOF
{
  "Comment": "A Hello World example of the Amazon States Language using Pass states",
  "StartAt": "Wait X Seconds",
  "States": {
    "Wait X Seconds": {
      "Type": "Wait",
      "Seconds": 10,
      "Next": "Get Domain Status"
    },
    "Get Domain Status": {
      "Comment": "Placeholder for a task state which checks status of the job. Replace with an API action.",
      "Type": "Task",
      "Parameters": {
        "DomainId.$": "$.domain_id"
      },
      "Resource": "arn:aws:states:::aws-sdk:sagemaker:describeDomain",
      "ResultPath": "$.domainstatus",
      "Next": "Domain Ready?"
    },
    "Domain Ready?": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.domainstatus.Status",
          "StringEquals": "Failed",
          "Next": "Domain Creation Failed"
        },
        {
          "Variable": "$.domainstatus.Status",
          "StringEquals": "InService",
          "Next": "Domain Creation Succeeded"
        }
      ],
      "Default": "Wait X Seconds"
    },
    "Domain Creation Succeeded": {
      "Comment": "Placeholder for a state which handles the success.",
      "Type": "Pass",
      "End": true
    },
    "Domain Creation Failed": {
      "Comment": "Placeholder for a state which handles the failure.",
      "Type": "Pass",
      "End": true
    }
  }
}
EOF
}
