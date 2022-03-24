# Resources

## create a S3 Bucket
data "aws_caller_identity" "current_caller" {}

resource "aws_s3_bucket" "s3_sample_glue_bucket" {
  bucket = "sample-bucket-glue-scripts-terraform-${data.aws_caller_identity.current_caller.id}"

}

## block public access
resource "aws_s3_bucket_public_access_block" "s3_glue_bucket_block_public_access" {
  bucket = aws_s3_bucket.s3_sample_glue_bucket.id

  block_public_acls   = true
  block_public_policy = true
  ignore_public_acls = true
  restrict_public_buckets = true
}

# upload the AWS Glue script to the bucket
resource "aws_s3_bucket_object" "glue_script_object" {
  bucket = aws_s3_bucket.s3_sample_glue_bucket.bucket
  key    = "glue_script.py"
  source = "./resources/glue_script.py"
  acl = "private"
}

## IAM Resources



# Outputs
output "bucket_name" {
  value = aws_s3_bucket.s3_sample_glue_bucket.bucket
}
output "bucket_arn" {
  value = aws_s3_bucket.s3_sample_glue_bucket.arn
}

output "glue_script_name" {
  value = aws_s3_bucket_object.glue_script_object.key
}