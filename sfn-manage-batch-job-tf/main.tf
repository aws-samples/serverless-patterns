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
  project_name = "manage-batch-job"

}

data "aws_caller_identity" "caller" {}
data "aws_partition" "partition" {}


resource "random_string" "random" {
  length           = 16
  special          = false
  upper            = false
}

resource "aws_sns_topic" "batch_job" {
  name = "StepFunctions-BatchJobManagement-${random_string.random.result}"
  kms_master_key_id = "alias/aws/sns"
}

resource "aws_iam_role" "batch_job_execution_role" {
  name               = "StepFunctions-BatchJobManagementRole"
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
  name               = "ecs_instance_role"
  assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json
}

resource "aws_iam_role_policy_attachment" "ecs_instance_role" {
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_iam_instance_profile" "ecs_instance_role" {
  name = "ecs_instance_role"
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

/* #Attach the IGW to the VPC
resource "aws_internet_gateway_attachment" "gw_attach" {
  internet_gateway_id = aws_internet_gateway.gw.id
  vpc_id              = aws_vpc.vpc.id
} */

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

resource "aws_batch_job_queue" "batch_job_queue" {
  name     = "StepFunctions-BatchJobManagementQueue-${random_string.random.result}"
  state    = "ENABLED"
  priority = 1
  compute_environments = [
    aws_batch_compute_environment.batch_compute_env.arn
  ]
}

resource "aws_iam_role" "sfn_batch_job_role" {
  name = "start-batch-job-${random_string.random.result}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "states.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "sfn_batch_job_policy" {
  name = "sfn-batch-job-policy-${random_string.random.result}"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                aws_sns_topic.batch_job.arn
            ],
            "Effect": "Allow"
        },
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

resource "aws_iam_role_policy_attachment" "state_machine_custom_policy_attachment" {
  policy_arn = aws_iam_policy.sfn_batch_job_policy.arn
  role       = aws_iam_role.sfn_batch_job_role.id
}

resource "aws_sfn_state_machine" "sfn_batch_job" {
  name     = "state-machine-manage-batch-job-${random_string.random.result}"
  role_arn = aws_iam_role.sfn_batch_job_role.arn
    definition = templatefile("${path.module}/statemachine/statemachine.asl.json", {
    sns_topic = aws_sns_topic.batch_job.arn,
    batch_job_definition  = aws_batch_job_definition.batch_job.arn,
    batch_job_queue     = aws_batch_job_queue.batch_job_queue.arn

  })
}
