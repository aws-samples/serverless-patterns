locals {
  bucket_name     = "REPLACE_ME_WITH_S3_BUCKET"
  event_bus_name  = "default"
  container_image = "REPLACE_ME_WITH_ECR_IMAGE_ARN"
  ecs_subnet_id   = "REPLACE_ME_WITH_SUBNET_ID"
  region          = "REPLACE_ME_WITH_AWS_REGION"
  
}

provider "aws" {
  region = "${local.region}"
 }

### S3 Resource Configuration ###
resource "aws_s3_bucket" "bucket" {
  bucket      = local.bucket_name
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket      = aws_s3_bucket.bucket.id
  eventbridge = true
}

resource "aws_s3_bucket_public_access_block" "bucket_bpa" {
  bucket = aws_s3_bucket.bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

### Choreography Reporting Rule ###
resource "aws_cloudwatch_event_rule" "serverlessland-s3-notification-rule" {
  name           = "serverlessland-s3-notification-rule"
  description    = "Capture s3 events"
  event_bus_name = local.event_bus_name
  
  event_pattern = <<EOF
{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"],
  "detail": {
    "bucket": {
      "name": ["${local.bucket_name}"]
    },
    "object": {
      "key": [{
        "prefix": "incoming"
      }]
    }
  }
}
EOF
}

### Eventbridge Event Target ###
resource "aws_cloudwatch_event_target" "serverlessland-s3-event-ecs-event-target" {
  target_id      = "serverlessland-s3-event-ecs-event-target"
  rule           = aws_cloudwatch_event_rule.serverlessland-s3-notification-rule.name
  arn            = aws_ecs_cluster.serverlessland-ecs-test-cluster.id
  role_arn       = aws_iam_role.serverlessland-eventbridge-invoke-ecs-role.arn
  event_bus_name = local.event_bus_name

  ecs_target {
    task_count          = 1
    task_definition_arn = aws_ecs_task_definition.serverlessland-ecs-task-definition.arn
    launch_type         = "FARGATE"
    
    network_configuration {
      subnets          = [ local.ecs_subnet_id ] 
      assign_public_ip = true
   }
  }

  input_transformer {
    input_paths = {
      bucket_name        = "$.detail.bucket.name",
      object_key         = "$.detail.object.key",
      source-ip-address  = "$.detail.source-ip-address"
    }
    input_template = <<EOF
{
  "containerOverrides": [
    {
      "name": "serverlessland-dump-env-vars",
      "environment" : [
        {
          "name" : "BUCKET_NAME",
          "value" : <bucket_name>
        },
        {
          "name" : "OBJECT_KEY",
          "value" : <object_key>
        },
        {
          "name" : "SOURCE_IP",
          "value" : <source-ip-address>
        }
      ]
    }
  ]
}
EOF
  }
}

### ECS Cluster ###
resource "aws_ecs_cluster" "serverlessland-ecs-test-cluster" {
  name = "serverlessland-ecs-test-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

### ECS Task Definition ###
resource "aws_ecs_task_definition" "serverlessland-ecs-task-definition" {
  family                   = "serverlessland-ecs-task-definition"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 1024
  memory                   = 2048
  task_role_arn            = aws_iam_role.serverlessland-ecs-task-role.arn
  execution_role_arn       = aws_iam_role.serverlessland-ecs-task-execution-role.arn
  container_definitions    = <<TASK_DEFINITION
[
  {
    "name": "serverlessland-dump-env-vars",
    "image": "${local.container_image}",
    "cpu": 1024,
    "memory": 2048,
    "essential": true,
    "logConfiguration": {
          "logDriver": "awslogs",
          "options": {
            "awslogs-group": "${aws_cloudwatch_log_group.serverlessland-cw-log-grp-dump-env-vars.name}",
            "awslogs-region": "${local.region}",
            "awslogs-stream-prefix": "ecs"
          }
    }
  }
]
TASK_DEFINITION

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }
}

### CloudWatch Log Group ###
resource "aws_cloudwatch_log_group" "serverlessland-cw-log-grp-dump-env-vars" {
  name = "/ecs/serverlessland-dump-env-vars"
}

### ECS Task Execution Role ###
resource "aws_iam_role" "serverlessland-ecs-task-execution-role" {
  name = "serverlessland-ecs-task-execution-role"
  managed_policy_arns = ["arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"]

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      },
    ]
  })
}

### Create a policy to access S3 buckets ###
resource "aws_iam_policy" "ecs_s3_access_policy"{
  name = "serverlessland_ecs_s3_access_policy"
  policy = jsonencode({
  
    Version: "2012-10-17",
    Statement: [
      {
        Sid: "",
        Action: [
        "s3:GetObject",
        "s3:ListBucket"        
        ],
        Effect: "Allow",
        Resource: [
             "arn:aws:s3:::${local.bucket_name}",
            "arn:aws:s3:::${local.bucket_name}/*"
        ]
      }
    ]
  })
}

### ECS Task Role ###
resource "aws_iam_role" "serverlessland-ecs-task-role" {
  name                = "serverlessland-ecs-task-role"
  managed_policy_arns = [
          "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
           aws_iam_policy.ecs_s3_access_policy.arn]
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

### ECS Eventbridge Invocation Role ###
resource "aws_iam_role" "serverlessland-eventbridge-invoke-ecs-role" {
  name                = "serverlessland-eventbridge-invoke-ecs-role"
  managed_policy_arns = [aws_iam_policy.serverlessland-eventbridge-invoke-ecs-policy.arn]

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "events.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_policy" "serverlessland-eventbridge-invoke-ecs-policy" {
  name = "serverlessland-eventbridge-invoke-ecs-policy"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecs:RunTask"
            ],
            "Resource": [
                "${aws_ecs_task_definition.serverlessland-ecs-task-definition.arn}:*",
                "${aws_ecs_task_definition.serverlessland-ecs-task-definition.arn}"
            ],
            "Condition": {
                "ArnLike": {
                    "ecs:cluster": "${aws_ecs_cluster.serverlessland-ecs-test-cluster.arn}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "ecs-tasks.amazonaws.com"
                }
            }
        }
    ]
})
}

