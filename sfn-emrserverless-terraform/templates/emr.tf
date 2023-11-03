resource "aws_emr_studio" "dev_studio" {
  auth_mode                   = "IAM"
  default_s3_location         = "s3://${aws_s3_bucket.emr_studio_bucket.bucket}/logs"
  engine_security_group_id    = aws_security_group.emr_security_group.id
  name                        = "${var.app}-${var.stage_name}-studio"
  service_role                = aws_iam_role.emr_studio_role.arn
  subnet_ids                  = [aws_subnet.emr_public_subnet1.id]
  vpc_id                      = aws_vpc.emr_vpc.id
  workspace_security_group_id = aws_security_group.emr_security_group.id
  tags = {
    Application = var.app
    Environment = var.stage_name
  }
}


resource "aws_emrserverless_application" "emr_serverless" {
  name          = "${var.app}-${var.stage_name}-emr-${data.aws_caller_identity.current.account_id}"
  release_label = "emr-6.9.0"
  type          = "spark"

  initial_capacity {
    initial_capacity_type = "Driver"

    initial_capacity_config {
      worker_count = 5
      worker_configuration {
        cpu    = "4 vCPU"
        memory = "20 GB"
      }
    }
  }

  initial_capacity {
    initial_capacity_type = "Executor"

    initial_capacity_config {
      worker_count = 5
      worker_configuration {
        cpu    = "4 vCPU"
        memory = "20 GB"
      }
    }
  }

  maximum_capacity {
    cpu    = "150 vCPU"
    memory = "1000 GB"
  }

  tags = {
    Name        = "EMR Serverless Application"
    Environment = var.stage_name
    Application = var.app
  }
}
