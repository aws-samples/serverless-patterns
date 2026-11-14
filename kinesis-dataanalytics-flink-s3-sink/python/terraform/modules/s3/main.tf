/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/s3/main.tf ---

# File path - flink application code
locals {
    file_path = "${path.module}/${var.path}/${var.name}"    
}

# Random number generator
resource "random_id" "random_generator" {
    byte_length = 8
}

# Create the Amazon S3 Destination Bucket for Kinesis Data Streams
resource "aws_s3_bucket" "kinesis_analytics_flink_application_bucket" {
    bucket        = "${var.s3_bucket_name_prefix}-${random_id.random_generator.hex}"
    force_destroy = true

    // Delete Flink Application Zip File
    ///tmp/sample_application_zip need to be updated accordingly per your requirements
    provisioner "local-exec" {
        environment = {
            file_path = "${path.module}/tmp/sample_application.zip" //Change this per your application needs
        }
        
        command = "rm -f $file_path"
        when    = destroy
    }
}

# S3 Destination Bucket - block public access
resource "aws_s3_bucket_public_access_block" "kinesis_analytics_flink_application_bucket_acl" {
    bucket                  = aws_s3_bucket.kinesis_analytics_flink_application_bucket.id
    block_public_acls       = true
    block_public_policy     = true
    ignore_public_acls      = true
    restrict_public_buckets = true
}

# Download the Flink Kinesis SQL connector from Maven Central into src/ so it is
# packaged into the application zip next to streaming-file-sink.py.
# The jar is not committed; the checksum pins the exact file.
resource "terraform_data" "flink_kinesis_connector" {
    triggers_replace = [var.connector_jar_sha256]

    provisioner "local-exec" {
        interpreter = ["/bin/sh", "-c"]
        environment = {
            JAR_URL    = var.connector_jar_url
            JAR_SHA256 = var.connector_jar_sha256
            JAR_PATH   = "${path.module}/src/${var.connector_jar_name}"
        }
        command = <<-EOT
            set -e
            sha256() { if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1"; else shasum -a 256 "$1"; fi | cut -d' ' -f1; }
            if [ ! -f "$JAR_PATH" ] || [ "$(sha256 "$JAR_PATH")" != "$JAR_SHA256" ]; then
                curl -fsSL --retry 3 -o "$JAR_PATH.download" "$JAR_URL"
                if [ "$(sha256 "$JAR_PATH.download")" != "$JAR_SHA256" ]; then
                    rm -f "$JAR_PATH.download"
                    echo "Checksum mismatch for $JAR_URL" >&2
                    exit 1
                fi
                mv "$JAR_PATH.download" "$JAR_PATH"
            fi
        EOT
    }
}

# Zip the source code
data "archive_file" "sample_flink_application_in_compressed_format" {
    type        = "${var.compression_type}"
    source_dir  = "${path.module}/src/"
    output_path = local.file_path

    depends_on = [terraform_data.flink_kinesis_connector]
}

# Upload the flink application to S3 bucket
resource "aws_s3_object" "kinesis_analytics_flink_application" {
    bucket = aws_s3_bucket.kinesis_analytics_flink_application_bucket.bucket
    key    = "${var.key}"
    source = data.archive_file.sample_flink_application_in_compressed_format.output_path
}

