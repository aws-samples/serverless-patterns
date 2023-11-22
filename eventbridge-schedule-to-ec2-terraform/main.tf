terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.64.0"
    }
  }
}

provider "aws" {
  region = var.region
}

locals {
  project_name = "tf-test"
}


# This section creates VPC resources for the Amazon EC2 environment

resource "aws_vpc" "vpc" {
  cidr_block  = var.vpc_cidr
}

resource "aws_subnet" "subnet" {
  vpc_id      = aws_vpc.vpc.id
  cidr_block  = var.subnet_cidr
  tags        = {
    Name = "private-subnet-1"
  }
}

# This section creates an Amazon EC2 instance using the latest Amazon Linux AMI

data "aws_ami" "amazon-linux-2" {
  most_recent = true

  filter {
    name = "owner-alias"
    values = ["amazon"]
  }
  
  filter {
    name = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

resource "aws_instance" "test-ec2" {
  ami           = "${data.aws_ami.amazon-linux-2.id}"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.subnet.id
  tags = {
    Name = "tf-test-ec2"
  }
}

# This section creates cron schedules using Amazon EventBridge Scheduler, as well as the required IAM roles to interact with EC2

resource "aws_scheduler_schedule" "ec2-start-schedule" {
  name = "ec2-start-schedule"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(0 8 ? * MON-FRI *)" # Scheduled startInstances at 8am EST Mon-Fri
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "Start instances event"

  target {
    arn = "arn:aws:scheduler:::aws-sdk:ec2:startInstances"
    role_arn = aws_iam_role.scheduler-ec2-role.arn
  
    input = jsonencode({
      "InstanceIds": [
        "${aws_instance.test-ec2.id}"
      ]
    })
  }
}

resource "aws_scheduler_schedule" "ec2-stop-schedule" {
  name = "ec2-stop-schedule"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(0 17 ? * MON-FRI *)" # Scheduled stopinstances at 5pm EST Mon-Fri
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "Stop instances event"

  target {
    arn = "arn:aws:scheduler:::aws-sdk:ec2:stopInstances"
    role_arn = aws_iam_role.scheduler-ec2-role.arn
  
    input = jsonencode({
      "InstanceIds": [
        "${aws_instance.test-ec2.id}"
      ]
    })
  }
}

resource "aws_iam_policy" "scheduler_ec2_policy" {
  name = "scheduler_ec2_policy"

  policy = jsonencode(
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "ec2:StartInstances",
                    "ec2:StopInstances"
                ],
                "Resource": [
                  "${aws_instance.test-ec2.arn}:*",
                  "${aws_instance.test-ec2.arn}"
                ],
            }
        ]
    }
  )
}

resource "aws_iam_role" "scheduler-ec2-role" {
  name = "scheduler-ec2-role"
  managed_policy_arns = [aws_iam_policy.scheduler_ec2_policy.arn]

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "scheduler.amazonaws.com"
        }
      },
    ]
  })
}
