terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0.0"
    }
  }
}

provider "aws" {
  region = var.region
}

data "aws_caller_identity" "current" {}

locals {
    account_id = data.aws_caller_identity.current.account_id
}

# This section creates the VPC and subnet for the Amazon EC2 instance

resource "aws_vpc" "vpc" {
  cidr_block  = var.vpc_cidr
}

resource "aws_subnet" "subnet" {
  vpc_id      = aws_vpc.vpc.id
  cidr_block  = var.subnet_cidr
  tags        = {
    Name = "my-private-subnet-1"
  }
}

# This section creates an Amazon EC2 instance using the latest Amazon Linux 2 AMI

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

resource "aws_instance" "example-ec2" {
  ami           = "${data.aws_ami.amazon-linux-2.id}"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet.id
  tags = {
    Name = "example-ec2"
  }
}

# This section creates an Amazon CloudWatch alarm of the CPUUtilization metric

resource "aws_cloudwatch_metric_alarm" "example-ec2-cpu-alarm" {
  alarm_name          = "example-ec2-cpu-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "60"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "This alarm is monitoring the CPUUtilization metric of an EC2 instance"
  alarm_actions       = []
  dimensions = {
    InstanceId = "${aws_instance.example-ec2.id}"
  }
}


# This section creates the cron schedules using Amazon EventBridge Scheduler

resource "aws_scheduler_schedule" "enable-ec2-alarm" {
  name = "enable-ec2-alarm"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(0 8 ? * MON-FRI *)" # Scheduled EnableAlarmActions at 8am EST Mon-Fri
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "Enable the CloudWatch alarm for EC2 CPU monitoring"

  target {
    arn = "arn:aws:scheduler:::aws-sdk:cloudwatch:enableAlarmActions"
    role_arn = aws_iam_role.scheduler-alarm-role.arn
  
    input = jsonencode({
      "AlarmNames": [
        "example-ec2-cpu-alarm"
      ]
    })
  }
}

resource "aws_scheduler_schedule" "disable-ec2-alarm" {
  name = "disable-ec2-alarm"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(0 17 ? * MON-FRI *)" # Scheduled DisableAlarmActions at 5pm EST Mon-Fri
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "Disable the CloudWatch alarm for EC2 CPU monitoring"

  target {
    arn = "arn:aws:scheduler:::aws-sdk:cloudwatch:disableAlarmActions"
    role_arn = aws_iam_role.scheduler-alarm-role.arn
  
    input = jsonencode({
      "AlarmNames": [
        "example-ec2-cpu-alarm"
      ]
    })
  }
}

# This section creates the required IAM policy and role to interact with CloudWatch alarm

resource "aws_iam_policy" "scheduler_alarm_policy" {
  name = "scheduler_alarm_policy"

  policy = jsonencode(
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "cloudwatch:EnableAlarmActions",
                    "cloudwatch:DisableAlarmActions"
                ],
                "Resource": [
                  "arn:aws:cloudwatch:${var.region}:${local.account_id}:alarm:example-ec2-cpu-alarm"
                ],
            }
        ]
    }
  )
}

resource "aws_iam_role" "scheduler-alarm-role" {
  name = "scheduler-alarm-role"
  managed_policy_arns = [aws_iam_policy.scheduler_alarm_policy.arn]

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