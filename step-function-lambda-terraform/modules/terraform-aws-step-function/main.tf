# variables
variable "lambda_function_arn" {}

# AWS Step Functions IAM roles and Policies
resource "aws_iam_role" "aws_stf_role" {
  name = "aws-stf-role"
  assume_role_policy = <<EOF
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Action":"sts:AssumeRole",
         "Principal":{
            "Service":[
                "states.amazonaws.com"
            ]
         },
         "Effect":"Allow",
         "Sid":"StepFunctionAssumeRole"
      }
   ]
}
EOF
}

resource "aws_iam_role_policy" "step_function_policy" {
  name = "aws-stf-policy"
  role    = aws_iam_role.aws_stf_role.id

  policy  = <<EOF
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Action":[
            "lambda:InvokeFunction"
         ],
         "Effect":"Allow",
         "Resource":"${var.lambda_function_arn}"
      }
  ]
}

EOF
}

# AWS Step function definition
resource "aws_sfn_state_machine" "aws_step_function_workflow" {
  name = "aws-step-function-workflow"
  role_arn = aws_iam_role.aws_stf_role.arn
  definition = <<EOF
{
   "Comment":"A description of my state machine",
   "StartAt":"TriggerLambda",
   "States":{
      "TriggerLambda":{
         "Type":"Task",
         "Resource":"arn:aws:states:::lambda:invoke",
         "OutputPath":"$.Payload",
         "Parameters":{
            "Payload.$":"$",
            "FunctionName":"${var.lambda_function_arn}"
         },
         "Retry":[
            {
               "ErrorEquals":[
                  "Lambda.ServiceException",
                  "Lambda.AWSLambdaException",
                  "Lambda.SdkClientException"
               ],
               "IntervalSeconds":1,
               "MaxAttempts":6,
               "BackoffRate":2
            }
         ],
         "Next":"Choice"
      },
      "Choice":{
         "Type":"Choice",
         "Choices":[
            {
               "Variable":"$.status",
               "StringEquals":"Success",
               "Next":"Pass"
            }
         ],
         "Default":"Fail"
      },
      "Pass":{
         "Type":"Pass",
         "End":true
      },
      "Fail":{
         "Type":"Fail"
      }
   }
}
EOF

}

# outputs
output "stf_role_arn" {
  value = aws_iam_role.aws_stf_role.arn
}
output "stf_name" {
  value = aws_sfn_state_machine.aws_step_function_workflow
}
output "stf_arn" {
  value = aws_sfn_state_machine.aws_step_function_workflow.arn
}