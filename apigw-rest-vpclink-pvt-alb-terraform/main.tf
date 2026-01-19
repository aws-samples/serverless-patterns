# Required providers configuration
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.80"
    }
  }
  required_version = ">= 1.9"
}

provider "aws" {
  profile = "default"
  region  = var.aws_region
}

##############################################
# PART 1: Private ALB with ECS Fargate Target
##############################################

# ALB security group
resource "aws_security_group" "alb_sg" {
  name        = "rest-api-alb-sg"
  description = "Security group for private ALB"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "rest-api-alb-sg"
  }
}

# ALB egress rule to ECS
resource "aws_security_group_rule" "alb_to_ecs" {
  type                     = "egress"
  description              = "Allow traffic to ECS tasks"
  from_port                = 80
  to_port                  = 80
  protocol                 = "tcp"
  security_group_id        = aws_security_group.alb_sg.id
  source_security_group_id = aws_security_group.ecs_sg.id
}

# ECS task security group
resource "aws_security_group" "ecs_sg" {
  name        = "rest-api-ecs-sg"
  description = "Security group for ECS tasks"
  vpc_id      = var.vpc_id

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "rest-api-ecs-sg"
  }
}

# ECS ingress rule from ALB
resource "aws_security_group_rule" "ecs_from_alb" {
  type                     = "ingress"
  description              = "Allow traffic from ALB"
  from_port                = 80
  to_port                  = 80
  protocol                 = "tcp"
  security_group_id        = aws_security_group.ecs_sg.id
  source_security_group_id = aws_security_group.alb_sg.id
}

# ECS Cluster
resource "aws_ecs_cluster" "main" {
  name = "rest-api-cluster"

  tags = {
    Name = "rest-api-cluster"
  }
}

# ECS Task Execution Role
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "rest-api-ecs-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# ECS Task Role
resource "aws_iam_role" "ecs_task_role" {
  name = "rest-api-ecs-task-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

# ECS Task Definition
resource "aws_ecs_task_definition" "app" {
  family                   = "rest-api-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn            = aws_iam_role.ecs_task_role.arn

  container_definitions = jsonencode([
    {
      name      = "web"
      image     = "nginx"
      essential = true
      portMappings = [
        {
          containerPort = 80
          protocol      = "tcp"
        }
      ]
    }
  ])

  tags = {
    Name = "rest-api-task"
  }
}

# ECS Service
resource "aws_ecs_service" "app" {
  name                               = "rest-api-service"
  cluster                            = aws_ecs_cluster.main.id
  task_definition                    = aws_ecs_task_definition.app.arn
  desired_count                      = 2
  deployment_maximum_percent         = 200
  deployment_minimum_healthy_percent = 50
  enable_ecs_managed_tags            = false
  health_check_grace_period_seconds  = 60
  launch_type                        = "FARGATE"

  network_configuration {
    subnets         = var.private_subnets
    security_groups = [aws_security_group.ecs_sg.id]
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.ecs_tg.arn
    container_name   = "web"
    container_port   = 80
  }

  depends_on = [aws_lb_target_group.ecs_tg, aws_lb_listener.http]

  tags = {
    Name = "rest-api-service"
  }
}

# Create private Application Load Balancer
resource "aws_lb" "private_alb" {
  name               = "rest-api-private-alb"
  internal           = true
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = var.private_subnets

  tags = {
    Name = "rest-api-private-alb"
  }
}

# Create target group for ECS
resource "aws_lb_target_group" "ecs_tg" {
  name        = "rest-api-ecs-tg"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = var.vpc_id
  target_type = "ip"

  tags = {
    Name = "rest-api-ecs-tg"
  }
}

# Create ALB listener
resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.private_alb.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs_tg.arn
  }
}

##############################################
# PART 2: VPC Link V2
##############################################

resource "aws_apigatewayv2_vpc_link" "vpclink" {
  name               = "rest-api-vpclink-v2"
  security_group_ids = []
  subnet_ids         = var.private_subnets

  tags = {
    Name = "rest-api-vpclink-v2"
  }
}

##############################################
# PART 3: REST API with VPC Link Integration
##############################################

# Create REST API
resource "aws_api_gateway_rest_api" "rest_api" {
  name        = "rest-api-vpclink-demo"
  description = "REST API with VPC Link V2 to private ALB"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

# Create proxy resource
resource "aws_api_gateway_resource" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id   = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part   = "{proxy+}"
}

# Create ANY method
resource "aws_api_gateway_method" "proxy_any" {
  rest_api_id   = aws_api_gateway_rest_api.rest_api.id
  resource_id   = aws_api_gateway_resource.proxy.id
  http_method   = "ANY"
  authorization = "NONE"

  request_parameters = {
    "method.request.path.proxy" = true
  }
}

# Create VPC Link integration with VPC Link V2
# Note: REST API + VPC Link V2 integration requires using AWS CLI directly
# as Terraform AWS provider doesn't fully support the integration_target parameter yet
resource "null_resource" "vpclink_integration" {
  triggers = {
    rest_api_id    = aws_api_gateway_rest_api.rest_api.id
    resource_id    = aws_api_gateway_resource.proxy.id
    vpc_link_id    = aws_apigatewayv2_vpc_link.vpclink.id
    alb_arn        = aws_lb.private_alb.arn
  }

  provisioner "local-exec" {
    command = <<-EOT
      aws apigateway put-integration \
        --rest-api-id ${aws_api_gateway_rest_api.rest_api.id} \
        --resource-id ${aws_api_gateway_resource.proxy.id} \
        --http-method ANY \
        --type HTTP_PROXY \
        --integration-http-method ANY \
        --connection-type VPC_LINK \
        --connection-id ${aws_apigatewayv2_vpc_link.vpclink.id} \
        --integration-target ${aws_lb.private_alb.arn} \
        --uri http://${aws_lb.private_alb.dns_name}/{proxy} \
        --request-parameters '{"integration.request.path.proxy":"method.request.path.proxy"}'
    EOT
  }

  depends_on = [
    aws_apigatewayv2_vpc_link.vpclink,
    aws_lb_listener.http,
    aws_api_gateway_method.proxy_any
  ]
}

# Create deployment
resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id

  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.proxy.id,
      aws_api_gateway_method.proxy_any.id,
      null_resource.vpclink_integration.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }

  depends_on = [null_resource.vpclink_integration]
}

# Create stage
resource "aws_api_gateway_stage" "prod" {
  deployment_id = aws_api_gateway_deployment.deployment.id
  rest_api_id   = aws_api_gateway_rest_api.rest_api.id
  stage_name    = "prod"
}
