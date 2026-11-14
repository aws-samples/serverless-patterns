terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.64.0"
    }
  }
}

locals{
  region              = "REPLACE_ME_WITH_AWS_REGION"
  container_image     = "amazon/amazon-ecs-sample"
  vpc_cidr            = "REPLACE_ME_WITH_AWS_VPC_CIDRS"
  availability_zones  = "REPLACE_ME_WITH_AWS_AVAILABILITY_ZONES"
  public_subnets      = "REPLACE_ME_WITH_AWS_PUBLIC_SUBNETS"
  private_subnets     = "REPLACE_ME_WITH_AWS_PRIVATE_SUBNETS"
}

provider "aws" {
  region = "${local.region}"

}

### EventBridge schedule setup ###
resource "aws_scheduler_schedule" "serverlessland-eb-ecs-invoke-schedule" {
      name = "serverlessland-eb-ecs-invoke-schedule"
      flexible_time_window {
      mode = "OFF"
  }
    schedule_expression = "rate(5 minute)"
    target {
      arn = aws_ecs_cluster.serverlessland-ecs-test-cluster.arn
      role_arn = aws_iam_role.serverlessland-eventbridge-invoke-ecs-role.arn
      ecs_parameters {
          task_count = 1
          task_definition_arn = aws_ecs_task_definition.serverlessland-ecs-task-definition.arn
          launch_type = "FARGATE"
    
          network_configuration {
                subnets          = aws_subnet.prod-subnet-public-1.*.id
                assign_public_ip = true
                security_groups = [aws_security_group.prod-sg.id]

   }
  }
  }
}

output "ScheduleTargetTask" {
  value = aws_ecs_cluster.serverlessland-ecs-test-cluster.arn
  description = "The ARN of the ecs task being invoked from EventBridge Scheduler"
}
output "ScheduleName" {
  value = aws_scheduler_schedule.serverlessland-eb-ecs-invoke-schedule.name
  description = "Name of the EventBridge Schedule"
}


### VPC, Subnets and SG ###
resource "aws_vpc" "prod-vpc" {
    cidr_block = local.vpc_cidr
    enable_dns_support = "true" #gives you an internal domain name
    enable_dns_hostnames = "true" #gives you an internal host name
    instance_tenancy = "default"    
    
    tags = {
        Name = "prod-vpc"
    }
}

resource "aws_subnet" "prod-subnet-public-1" {
    vpc_id = "${aws_vpc.prod-vpc.id}"
    count = length(local.public_subnets)
    cidr_block =  element(local.public_subnets,count.index)
    availability_zone = element(local.availability_zones,count.index)
    map_public_ip_on_launch = "true" //it makes this a public subnet
    depends_on = [aws_internet_gateway.aws-igw]
    tags = {
        Name = "prod-subnet-public-1"
        Environment = "prod"
    }
}

resource "aws_subnet" "prod-subnet-private-1" {
    vpc_id = "${aws_vpc.prod-vpc.id}"
    count = length(local.private_subnets)
    cidr_block =  element(local.private_subnets,count.index)
    availability_zone = element(local.availability_zones,count.index)
    depends_on = [aws_internet_gateway.aws-igw]
    tags = {
        Name = "prod-subnet-private-1"
        Environment = "prod"
    }
}

resource "aws_security_group" "prod-sg" {
  name   = "prod-sg"
  vpc_id = aws_vpc.prod-vpc.id
   ingress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

### Networking ###
resource "aws_internet_gateway" "aws-igw" {
  vpc_id = aws_vpc.prod-vpc.id
  tags = {
    Name        = "prod-igw"
    Environment = "prod"
    }

}


resource "aws_route_table" "public" {
  vpc_id = aws_vpc.prod-vpc.id

  tags = {
    Name        = "prod-routing-table-public"
    Environment = "prod"
    
  }
}

resource "aws_route" "public" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.aws-igw.id
}

resource "aws_route_table_association" "public" {
  count          = length(local.public_subnets) 
  subnet_id      = element(aws_subnet.prod-subnet-public-1.*.id, count.index)
  route_table_id = aws_route_table.public.id
}


### ECS Cluster ###
resource "aws_ecs_cluster" "serverlessland-ecs-test-cluster" {
  name = "serverlessland-ecs-test-cluster"
  depends_on = [aws_internet_gateway.aws-igw]
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
    "name": "webcontainer",
    "image": "${local.container_image}",
    "cpu": 1024,
    "memory": 2048,
    "essential": true,
    "logConfiguration": {
          "logDriver": "awslogs",
          "options": {
            "awslogs-group": "${aws_cloudwatch_log_group.serverlessland-cw-log-grp-dump-ecs.id}",
            "awslogs-region": "${local.region}",
            "awslogs-stream-prefix": "ecs"
          }
    },
    "portMappings": [
        {
          "containerPort": 8080,
          "hostPort": 8080
        }
      ]
  }
]
TASK_DEFINITION

}


### CloudWatch Log Group ###
resource "aws_cloudwatch_log_group" "serverlessland-cw-log-grp-dump-ecs" {
  name = "/ecs/webcontainer"
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


### ECS Task Role ###
resource "aws_iam_role" "serverlessland-ecs-task-role" {
  name                = "serverlessland-ecs-task-role"
  managed_policy_arns = [
          "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
          ]
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
          Service = "scheduler.amazonaws.com"
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




