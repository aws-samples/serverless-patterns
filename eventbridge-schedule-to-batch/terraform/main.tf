# eventbridge-schedule-to-batch-terraform

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>4.0"
    }
  }
}

provider "aws" {
  region  = var.region
}

locals {
  project_name = "batch-job"
}

resource "random_string" "random" {
  length           = 16
  special          = false
  upper            = false
}

# This section creates the Batch job and any IAM resources required for the job to execute
resource "aws_iam_role" "batch_job_execution_role" {
  name               = "StepFunctions-BatchJobManagementRole-${random_string.random.result}"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "batch_job_execution_policy" {
  role       = aws_iam_role.batch_job_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_batch_job_definition" "batch_job" {
  name = "StepFunctions-BatchJobManagement-${random_string.random.result}"
  type = "container"
  container_properties = jsonencode({
    command = ["ls", "-la"],
    image   = "busybox"

    resourceRequirements = [
      {
        type  = "VCPU"
        value = "1"
      },
      {
        type  = "MEMORY"
        value = "512"
      }
    ]

    volumes = [
      {
        host = {
          sourcePath = "/tmp"
        }
        name = "tmp"
      }
    ]

    environment = [
      {
        name  = "VARNAME"
        value = "VARVAL"
      }
    ]

    mountPoints = [
      {
        sourceVolume  = "tmp"
        containerPath = "/tmp"
        readOnly      = false
      }
    ]

    ulimits = [
      {
        hardLimit = 1024
        name      = "nofile"
        softLimit = 1024
      }
    ]
    executionRoleArn = aws_iam_role.batch_job_execution_role.arn
  })
}

data "aws_iam_policy_document" "ec2_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "ecs_instance_role" {
  name               = "ecs_instance_role_${random_string.random.result}"
  assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json
}

resource "aws_iam_role_policy_attachment" "ecs_instance_role" {
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_iam_instance_profile" "ecs_instance_role" {
  name = "ecs_instance_role_${random_string.random.result}"
  role = aws_iam_role.ecs_instance_role.name
}

data "aws_iam_policy_document" "batch_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["batch.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

# This section creates a VPC and related resources for the AWS Batch environment

# VPC to hold all Batch resources
resource "aws_vpc" "vpc" {
  cidr_block = var.vpc_cidr

}

# Create an Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.vpc.id
}

# Public Route Table
resource "aws_route_table" "public_route" {
  vpc_id = aws_vpc.vpc.id
  route {

    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

}

#Create a single subnet which allows public IP's
resource "aws_subnet" "subnet" {
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = var.subnet_cidr
  map_public_ip_on_launch = true
}

# Associate the route table with the subnet
resource "aws_route_table_association" "subnet_rt" {
  subnet_id      = aws_subnet.subnet.id
  route_table_id = aws_route_table.public_route.id
}

#Create a security group for the batch job
resource "aws_security_group" "batch_sg" {
  name        = "${local.project_name}-sg"
  description = "Security group for Batch environment"
  vpc_id      = aws_vpc.vpc.id
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]

  }
}

# Create the Role and Policies for the Batch environment
resource "aws_iam_role" "batch_role" {
  name = "${local.project_name}-batch-svc-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "batch.amazonaws.com"
        }
      },
    ]
  })
  managed_policy_arns = ["arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole"]
}

#Create the ECS instance role
resource "aws_iam_role" "batch_ecs_role" {
  name = "${local.project_name}-batch-ecs-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
  managed_policy_arns = ["arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"]
}

# Create the ECS instance profile
resource "aws_iam_instance_profile" "ecs_profile" {
  name = "${local.project_name}-batch-profile"
  role = aws_iam_role.batch_ecs_role.name
}

# Create the Batch compute environment
resource "aws_batch_compute_environment" "batch_compute_env" {
  compute_environment_name = "BatchComputeEnvironment-${random_string.random.result}"
  type         = "MANAGED"
  service_role = aws_iam_role.batch_role.arn
  compute_resources {
    max_vcpus     = 64
    min_vcpus     = 0
    desired_vcpus = 2
    type          = "EC2"
    instance_role = aws_iam_instance_profile.ecs_profile.arn
    security_group_ids = [
      aws_security_group.batch_sg.id
    ]
    instance_type = ["optimal"]
    subnets = [
      aws_subnet.subnet.id
    ]
  }
  depends_on = [
    aws_iam_role.batch_ecs_role,
    aws_subnet.subnet,
    aws_security_group.batch_sg,
    aws_iam_role.batch_role
  ]
}

# Create the Batch job queue
resource "aws_batch_job_queue" "batch_job_queue" {
  name     = "Scheduler-Batch-Queue-${random_string.random.result}"
  state    = "ENABLED"
  priority = 1
  compute_environments = [
    aws_batch_compute_environment.batch_compute_env.arn
  ]
}

# This section creates schedules using Amazon EventBridge Scheduler, as well as the required IAM roles to interact with Batch

resource "aws_scheduler_schedule" "batch-schedule" {
  name = "batch-submit-job-schedule"
  
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(5 minutes)"
  schedule_expression_timezone = "US/Eastern" # Default is UTC
  description = "submitJob Batch event"

  target {
    arn = "arn:aws:scheduler:::aws-sdk:batch:submitJob"
    role_arn = aws_iam_role.scheduler-batch-role.arn
  
    input = jsonencode({
        "JobName": "scheduled-job",
        "JobDefinition": "${aws_batch_job_definition.batch_job.arn}",
        "JobQueue": "${aws_batch_job_queue.batch_job_queue.arn}"
    })
  }
}

resource "aws_iam_policy" "scheduler_batch_policy" {
  name = "scheduler_batch_policy"

    policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "batch:SubmitJob",
                "batch:DescribeJobs",
                "batch:TerminateJob"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "events:PutTargets",
                "events:PutRule",
                "events:DescribeRule"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow"
        }
       ]
      }
    )
}

resource "aws_iam_role" "scheduler-batch-role" {
  name = "scheduler-batch-role"
  managed_policy_arns = [aws_iam_policy.scheduler_batch_policy.arn]

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

