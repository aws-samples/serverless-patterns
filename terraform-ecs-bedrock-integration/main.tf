provider "aws" {
  region = "us-east-1"
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

####################################################
# Locals and Tagging
####################################################

locals {
  common_tags = {
    organization = var.organization
    env          = var.env
  }
  region                 = data.aws_region.current.name
  account_id             = data.aws_caller_identity.current.account_id
  standard_resource_name = "${var.env}-${var.organization}-genai-app"
  ecr_base_arn           = "${local.account_id}.dkr.ecr.${local.region}.amazonaws.com"
  aws_path               = "/${var.env}/${var.organization}/"
  containercode_dir      = "./containercode/"
  aws_subnets            = var.aws_subnets
}


/*
# Uncomment to dynamically get list of subnets based on tags
#################################################################################
# Query Subnets (Assumption that you have a VPC with subnets tagged as Public)
#################################################################################
data "aws_subnets" "public_subnet" {
  filter {
    name   = "vpc-id"
    values = [var.aws_vpc_id]
  }
  tags = {
    Network = "public"
  }
}
*/



##############################
# Create Security Group
##############################
resource "aws_security_group" "this_aws_security_group" {
  name        = local.standard_resource_name
  description = "Allow only outbound traffic for ECS Web Hosted Application"
  vpc_id      = var.aws_vpc_id
  tags        = local.common_tags
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


##############################
# Create KMS Key & Policy
##############################
resource "aws_kms_key" "this_aws_kms_key" {
  description             = local.standard_resource_name
  deletion_window_in_days = 30
  policy = templatefile("templates/kms-policy.json",
    {
      account_number         = local.account_id
      standard_resource_name = "${var.env}-${var.organization}"
      region                 = local.region
    }
  )
  multi_region        = true
  enable_key_rotation = true
  tags                = merge(local.common_tags)
}

resource "aws_kms_alias" "this_aws_kms_alias" {
  name          = "alias/${local.standard_resource_name}"
  target_key_id = aws_kms_key.this_aws_kms_key.key_id
}

#####################################
# Checks if build folder has changed
#####################################
data "external" "this_external" {
  program = ["bash", "${path.module}/bin/dir_md5.sh", "${path.module}/${local.containercode_dir}"]
}

###########
# ECR
###########
resource "aws_ecr_repository" "this_aws_ecr_repository" {
  name                 = local.standard_resource_name
  tags                 = local.common_tags
  image_tag_mutability = "MUTABLE"
  force_delete         = true
  image_scanning_configuration {
    scan_on_push = true
  }
  encryption_configuration {
    encryption_type = "KMS"
    kms_key         = aws_kms_key.this_aws_kms_key.arn
  }
}

resource "aws_ecr_lifecycle_policy" "ecr_lifecycle_policy" {
  policy = templatefile("templates/ecr-lifecycle-policy.json",
    {}
  )
  repository = aws_ecr_repository.this_aws_ecr_repository.name
}

########################################################
# Builds service and pushes it into aws_ecr_repository
########################################################
resource "terraform_data" "this_terraform_data_build_ecr_image" {
  depends_on = [aws_ecr_repository.this_aws_ecr_repository]
  triggers_replace = [
    data.external.this_external.result.md5,
    aws_ecr_repository.this_aws_ecr_repository.id
  ]
  provisioner "local-exec" {
    command = "bash ${path.module}/bin/build.sh ${local.ecr_base_arn} ${path.module}/${local.containercode_dir} ${aws_ecr_repository.this_aws_ecr_repository.name} ${aws_ecr_repository.this_aws_ecr_repository.repository_url} ${local.region}"
  }
}

data "aws_ecr_image" "this_aws_ecr_image" {
  depends_on      = [terraform_data.this_terraform_data_build_ecr_image, aws_ecr_repository.this_aws_ecr_repository]
  repository_name = aws_ecr_repository.this_aws_ecr_repository.name
  most_recent     = true
}

########################################################
# Create IAM role, policy and policy attachment
########################################################
resource "aws_iam_role" "this_aws_iam_role" {
  name               = local.standard_resource_name
  path               = local.aws_path
  description        = "Role to be Assumed by ECS Task"
  tags               = local.common_tags
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {"Service": "ecs-tasks.amazonaws.com"},
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_policy" "this_aws_iam_policy" {
  name = local.standard_resource_name
  policy = templatefile("templates/ecs-role.json", {
    account_number         = local.account_id
    standard_resource_name = local.standard_resource_name
    kms_key_arn            = aws_kms_key.this_aws_kms_key.arn
  })
}

resource "aws_iam_policy_attachment" "this_aws_iam_policy_attachment" {
  name       = local.standard_resource_name
  roles      = [aws_iam_role.this_aws_iam_role.name]
  policy_arn = aws_iam_policy.this_aws_iam_policy.arn
}

###############################
# Cloudwatch log Group
###############################
resource "aws_cloudwatch_log_group" "this_aws_cloudwatch_log_group" {
  name              = "/aws/${local.standard_resource_name}"
  retention_in_days = 30
  kms_key_id        = aws_kms_key.this_aws_kms_key.arn
  tags              = local.common_tags
}

#########################################
# Create ECS Cluster for Hosting the App
#########################################
resource "aws_ecs_cluster" "this_aws_ecs_cluster" {
  name = local.standard_resource_name
  tags = local.common_tags
}

resource "aws_ecs_task_definition" "this_aws_ecs_task_definition" {
  family                   = local.standard_resource_name
  execution_role_arn       = aws_iam_role.this_aws_iam_role.arn
  task_role_arn            = aws_iam_role.this_aws_iam_role.arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.task_cpu
  memory                   = var.task_memory
  tags                     = local.common_tags
  container_definitions    = <<DEFINITION
[
  {
    "name": "${local.standard_resource_name}",
    "image": "${aws_ecr_repository.this_aws_ecr_repository.repository_url}:${data.aws_ecr_image.this_aws_ecr_image.image_tags[0]}",
    "cpu": ${var.task_cpu},
    "memory": ${var.task_memory},
    "memoryReservation": 300,
    "networkMode": "awsvpc",
    "portMappings": [
     {
        "containerPort": 8501
     }
    ],
    "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "${aws_cloudwatch_log_group.this_aws_cloudwatch_log_group.name}",
          "awslogs-region": "${local.region}",
          "awslogs-stream-prefix": "${local.standard_resource_name}"
        }
    },
    "environment": [
      {
        "name": "ENV",
        "value": "${var.env}"
      }
    ]
  }
]
DEFINITION
}

resource "aws_ecs_service" "this_aws_ecs_service" {
  name                 = local.standard_resource_name
  launch_type          = var.launch_type
  cluster              = aws_ecs_cluster.this_aws_ecs_cluster.id
  task_definition      = aws_ecs_task_definition.this_aws_ecs_task_definition.arn
  desired_count        = var.desired_count
  tags                 = local.common_tags
  force_new_deployment = true
  lifecycle {
    replace_triggered_by = [
      aws_ecs_task_definition.this_aws_ecs_task_definition.id
    ]
  }
  network_configuration {
    assign_public_ip = true
    security_groups  = [aws_security_group.this_aws_security_group.id]
    subnets          = local.aws_subnets
  }
  load_balancer {
    container_name   = local.standard_resource_name
    target_group_arn = aws_lb_target_group.this_aws_lb_target_group_front_end.arn
    container_port   = "8501"
  }
}

resource "aws_alb" "this_aws_alb_front_end" {
  name               = local.standard_resource_name
  internal           = var.subnet_type == "public" ? false : true
  load_balancer_type = "application"
  subnets            = local.aws_subnets
  security_groups    = [aws_security_group.this_aws_security_group.id]
}

resource "aws_lb_target_group" "this_aws_lb_target_group_front_end" {
  name        = local.standard_resource_name
  port        = 8080
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = var.aws_vpc_id
}

resource "aws_alb_listener" "this_aws_alb_listener_front_end" {
  load_balancer_arn = aws_alb.this_aws_alb_front_end.arn
  port              = "8080"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.this_aws_lb_target_group_front_end.arn
  }
}