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
  standard_resource_name = "${var.env}-${var.organization}"
  ecr_base_arn           = "${local.account_id}.dkr.ecr.${local.region}.amazonaws.com"
  aws_path               = "/${var.env}/${var.organization}/"
  containercode_dir      = "./containercode/"
}

#################################################################################
# Query Subnets (Assumption that you have a VPC with subnets tagged as Private)
#################################################################################
data "aws_subnets" "private_subnet" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
  tags = {
    Network = "private"
  }
}

##############################
# Create Security Group
##############################
resource "aws_security_group" "this_security_group" {
  name        = local.standard_resource_name
  description = "Allow only outbound traffic for ECS Container"
  vpc_id      = var.vpc_id
  tags        = local.common_tags
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    self      = true
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
resource "aws_kms_key" "aws_kms_key" {
  description             = local.standard_resource_name
  deletion_window_in_days = 30
  policy = templatefile("templates/kms-policy.json",
    {
      account_number         = local.account_id
      standard_resource_name = local.standard_resource_name
      region                 = local.region
    }
  )
  multi_region        = true
  enable_key_rotation = true
  tags                = merge(local.common_tags)
}

resource "aws_kms_alias" "aws_kms_key_alias" {
  name          = "alias/${local.standard_resource_name}"
  target_key_id = aws_kms_key.aws_kms_key.key_id
}

#################################
# Create an EFS and Mount Target
#################################
resource "aws_efs_file_system" "efs_volume" {
  encrypted        = true
  kms_key_id       = aws_kms_key.aws_kms_key.arn
  performance_mode = "generalPurpose"
  tags             = local.common_tags
}

resource "aws_efs_mount_target" "ecs_space_az" {
  for_each        = toset(data.aws_subnets.private_subnet.ids)
  file_system_id  = aws_efs_file_system.efs_volume.id
  subnet_id       = each.value
  security_groups = [aws_security_group.this_security_group.id]
}

###########
# ECR
###########
resource "aws_ecr_repository" "aws_ecr_repository_efs_updater" {
  name                 = "${local.standard_resource_name}-efs-updater"
  tags                 = local.common_tags
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
  encryption_configuration {
    encryption_type = "KMS"
    kms_key         = aws_kms_key.aws_kms_key.arn
  }
}

resource "aws_ecr_lifecycle_policy" "ecr_lifecycle_policy" {
  policy = templatefile("templates/ecr-lifecycle-policy.json",
    {}
  )
  repository = aws_ecr_repository.aws_ecr_repository_efs_updater.name
}

#####################################
# Checks if build folder has changed
#####################################
data "external" "external_efs_updater" {
  program = ["bash", "${path.module}/bin/dir_md5.sh", "${path.module}/${local.containercode_dir}"]
}

########################################################
# Builds service and pushes it into aws_ecr_repository
########################################################
resource "null_resource" "null_resource_efs_updater" {
  depends_on = [aws_ecr_repository.aws_ecr_repository_efs_updater]
  #triggers   = { always_run = "${timestamp()}" }
  triggers = { build_folder_content_md5 = data.external.external_efs_updater.result.md5 }
  provisioner "local-exec" {
    command = "bash ${path.module}/bin/build.sh ${local.ecr_base_arn} ${path.module}/${local.containercode_dir} ${aws_ecr_repository.aws_ecr_repository_efs_updater.name} ${aws_ecr_repository.aws_ecr_repository_efs_updater.repository_url} ${local.region}"
  }
}

########################################################
# Create ECS Cluster
########################################################
resource "aws_ecs_cluster" "this_ecs_cluster" {
  name = "${local.standard_resource_name}-efs-updater"
  tags = local.common_tags
}

########################################################
# Create ECS role, policy and policy attachment
########################################################
resource "aws_iam_role" "this_task_role" {
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

resource "aws_iam_policy" "this_iam_policy" {
  name = local.standard_resource_name
  policy = templatefile("templates/ecs-role.json", {
    account_number         = local.account_id
    standard_resource_name = local.standard_resource_name
    kms_key_arn            = aws_kms_key.aws_kms_key.arn
  })
}

resource "aws_iam_policy_attachment" "this_aws_iam_policy_attachment" {
  name       = local.standard_resource_name
  roles      = [aws_iam_role.this_task_role.name]
  policy_arn = aws_iam_policy.this_iam_policy.arn
}

###############################
# Cloudwatch log Group
###############################
resource "aws_cloudwatch_log_group" "aws_cloudwatch_log_group_efs_updater" {
  name              = "/aws/${local.standard_resource_name}-efs-updater"
  retention_in_days = 30
  kms_key_id        = aws_kms_key.aws_kms_key.arn
  tags              = local.common_tags
}

################################
# ECS Task Definition
###############################
resource "aws_ecs_task_definition" "aws_ecs_task_definition_efs_updater" {
  family                   = "${local.standard_resource_name}-efs-updater"
  execution_role_arn       = aws_iam_role.this_task_role.arn
  task_role_arn            = aws_iam_role.this_task_role.arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.task_cpu
  memory                   = var.task_memory
  tags                     = local.common_tags
  container_definitions    = <<DEFINITION
[
  {
    "name": "${local.standard_resource_name}",
    "image": "${aws_ecr_repository.aws_ecr_repository_efs_updater.repository_url}:latest",
    "cpu": ${var.task_cpu},
    "memory": ${var.task_memory},
    "memoryReservation": 300,
    "networkMode": "awsvpc",
    "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "${aws_cloudwatch_log_group.aws_cloudwatch_log_group_efs_updater.name}",
          "awslogs-region": "${local.region}",
          "awslogs-stream-prefix": "${local.standard_resource_name}"
        }
    },
    "environment": [
      {
        "name": "ENV",
        "value": "${var.env}"
      }
    ],
    "mountPoints" : [
      {
        "sourceVolume" : "efs-vol",
        "containerPath" : "/efs",
        "readOnly" : false
      }
    ]
  }
]
DEFINITION
  volume {
    name = "efs-vol"
    efs_volume_configuration {
      file_system_id = aws_efs_file_system.efs_volume.id
      root_directory = "/"
    }
  }
}