terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 5.61"
      }
    }
}

provider "aws" { 
    region = "eu-west-2"
    profile = "default"
}

data "aws_region" "current" {
}

data "aws_caller_identity" "current" {
}

resource "aws_cloudfront_origin_access_control" "spa_aoc" {
  name                              = "spa_aoc"
  description                       = "spa_aoc"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "cf_distribution" {
  enabled             = true
  default_root_object = "index.html"
  is_ipv6_enabled     = true
  price_class         = "PriceClass_All"

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
  origin {
    domain_name              = aws_s3_bucket.host.bucket_regional_domain_name
    origin_id                = "spa_portal"
    origin_access_control_id = aws_cloudfront_origin_access_control.spa_aoc.id
  }

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "spa_portal"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 300
    max_ttl                = 1200
  }

  viewer_certificate {
    cloudfront_default_certificate = true
    minimum_protocol_version       = "TLSv1.2_2021"
  }
}

locals {
  s3_origin_id = "host-store"
}

resource "aws_s3_bucket" "host" {
  bucket = local.s3_origin_id
}

resource "aws_s3_bucket_public_access_block" "bucket_access_block" {
  bucket                  = aws_s3_bucket.host.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "host_ownership" {
  bucket = aws_s3_bucket.host.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "host_acl" {
  depends_on = [aws_s3_bucket_ownership_controls.host_ownership]

  bucket = aws_s3_bucket.host.id
  acl    = "private"
}


resource "aws_s3_bucket_website_configuration" "website_configuration" {
  bucket = aws_s3_bucket.host.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

resource "aws_s3_bucket_policy" "host_policy" {
  bucket = aws_s3_bucket.host.id

  policy = jsonencode({
    Statement = [
      {
        Action   = "s3:GetObject"
        Effect   = "Allow"
        Resource = "arn:aws:s3:::${aws_s3_bucket.host.bucket}/*"
        Principal = {
          Service = "cloudfront.amazonaws.com"
        },
        Condition = {
          StringEquals = {
            "AWS:SourceArn" = "arn:aws:cloudfront::${data.aws_caller_identity.current.account_id}:distribution/${aws_cloudfront_distribution.cf_distribution.id}"
          }
        }
      }
    ]
  })
}