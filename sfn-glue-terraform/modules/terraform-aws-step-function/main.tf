# variables
variable "glue_job_arn" {}
variable "glue_job_name" {}
variable "glue_message" {default = "This is a message passed by the AWS Step Function"}

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
                "glue:StartJobRun",
                "glue:GetJobRun",
                "glue:GetJobRuns",
                "glue:BatchStopJobRun"
         ],
         "Effect":"Allow",
         "Resource":"${var.glue_job_arn}"
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
   "Comment":"A description of the sample glue job state machine using Terraform",
   "StartAt":"Glue StartJobRun",
   "States":{
      "Glue StartJobRun":{
         "Type":"Task",
         "Resource":"arn:aws:states:::glue:startJobRun.sync",
         "Parameters":{
            "JobName":"${var.glue_job_name}",
            "Arguments": {
              "--message": "${var.glue_message}"
            }
         },
         "End":true
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