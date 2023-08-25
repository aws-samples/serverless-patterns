resource "aws_s3_bucket" "emr_studio_bucket" {
  bucket = "${data.aws_region.current.name}-${var.app}-${var.stage_name}-emr-studio-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "EMR studio bucket"
    Application = var.app
    Environment = var.stage_name
  }
}

resource "aws_s3_bucket" "output_s3_bucket" {
  bucket = "${data.aws_region.current.name}-${var.app}-${var.stage_name}-output-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "EMR Job Output S3 bucket"
    Application = var.app
    Environment = var.stage_name
  }
}

resource "aws_s3_bucket" "job_source_s3_bucket" {
  bucket = "${data.aws_region.current.name}-${var.app}-${var.stage_name}-source-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "EMR Job Source (eg. jar file) S3 bucket"
    Application = var.app
    Environment = var.stage_name
  }
}
