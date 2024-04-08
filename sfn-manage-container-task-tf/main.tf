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
  project_name = "manage-container-task"

}

data "aws_caller_identity" "caller" {}
data "aws_partition" "partition" {}


resource "random_string" "random" {
  length           = 16
  special          = false
  upper            = false
}

# VPC
# main.tf

module "vpc" {
  source = "./vpc"

  vpc_name = "example-vpc"
  cidr_block = "10.0.0.0/16"
  public_subnet_cidr_blocks = ["10.0.1.0/24", "10.0.2.0/24"]
  availability_zones = ["us-east-1a", "us-east-1b"]
}

# Security Group
resource "aws_security_group" "fargate_sg" {
  name_prefix = "FargateTaskNotification-SG-${random_string.random.result}"
  description = "Allow access to the public facing load balancer"
  vpc_id      = module.vpc.vpc_id
  ingress {
    from_port = 80
    to_port   = 80
    protocol  = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "fargate-container-sg"
  }
}

# Create a new IAM role for the Fargate task
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "FargateTaskNotification-${random_string.random.result}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Attach the required policies to the IAM role
resource "aws_iam_role_policy_attachment" "ecsTaskExecutionPolicyAttachment" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
  role       = aws_iam_role.ecs_task_execution_role.name
}

# Define ECS task definition: creating a Fargate task that runs an nginx web server container and outputs a success message when started.
resource "aws_ecs_task_definition" "fargate_task" {
  family                   = "FargateTaskNotification-${random_string.random.result}"
  network_mode             = "awsvpc"
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  requires_compatibilities = ["FARGATE"]
  container_definitions    = jsonencode(
    [
      {
        "cpu" : 256,
        "image" : "nginx",
        "memory" : 512,
        "name" : "my_container",
        "command": ["echo", "Task succeeded!"],
        "essential": true,
        "portMappings" : [
          {
            "containerPort" : 80,
            "protocol" : "tcp"
          }
        ]
      }
    ])
}


# Define ECS cluster
resource "aws_ecs_cluster" "fargate_cluster" {
  name = "FargateTaskNotification-${random_string.random.result}"
}

resource "aws_ecs_service" "example" {
  name            = "example-service"
  cluster         = aws_ecs_cluster.fargate_cluster.id
  task_definition = aws_ecs_task_definition.fargate_task.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    security_groups = [aws_security_group.fargate_sg.id]
    subnets         = [module.vpc.public_subnet_1_id, module.vpc.public_subnet_2_id]
  }
}

# Define SNS topic
resource "aws_sns_topic" "sns_topic" {
  name = "FargateTaskNotification-${random_string.random.result}"
}

#SFN
resource "aws_iam_role" "sfn_container_task_role" {
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

resource "aws_iam_policy" "sfn_container_task_policy" {
  name = "sfn-conteiner-task-policy-${random_string.random.result}"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                aws_sns_topic.sns_topic.arn
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "ecs:RunTask"
            ],
            "Resource": [
                aws_ecs_task_definition.fargate_task.arn
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "ecs:StopTask",
                "ecs:DescribeTasks"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "events:PutTargets",
                "events:PutRule",
                "events:DescribeRule",
                "iam:PassRole"
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
  policy_arn = aws_iam_policy.sfn_container_task_policy.arn
  role       = aws_iam_role.sfn_container_task_role.id
}

resource "aws_sfn_state_machine" "sfn_container_task" {
  name       = "state-machine-container-task-${random_string.random.result}"
  role_arn   = aws_iam_role.sfn_container_task_role.arn
  definition = templatefile("${path.module}/statemachine/statemachine.asl.json", {
    sns_topic            = aws_sns_topic.sns_topic.arn,
    ecs_cluster          = aws_ecs_cluster.fargate_cluster.arn,
    task_definition      = aws_ecs_task_definition.fargate_task.arn,
    subnet_a             = module.vpc.public_subnet_1_id,
    subnet_b             = module.vpc.public_subnet_2_id
  })
}