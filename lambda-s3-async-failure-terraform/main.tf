provider "aws" {
  region = "us-east-1"
}

# Random UUID for bucket name suffix
resource "random_uuid" "bucket_suffix" {}

# S3 bucket as destination for async invocation records
resource "aws_s3_bucket" "destination_bucket" {
  bucket = "async-lambda-destination-${random_uuid.bucket_suffix.result}"
}

resource "aws_s3_bucket_ownership_controls" "destination_bucket" {
  bucket = aws_s3_bucket.destination_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

# Add versioning to the bucket
resource "aws_s3_bucket_versioning" "destination_bucket" {
  bucket = aws_s3_bucket.destination_bucket.id
  versioning_configuration {
    status = "Disabled"
  }
}

# Block public access
resource "aws_s3_bucket_public_access_block" "destination_bucket" {
  bucket = aws_s3_bucket.destination_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# IAM role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "async_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# IAM policy for Lambda to write to CloudWatch Logs
resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# IAM policy for Lambda to write to S3 destination
resource "aws_iam_role_policy" "lambda_s3_policy" {
  name = "lambda_s3_policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:ListBucket"
        ]
        Resource = [
            "${aws_s3_bucket.destination_bucket.arn}/*",
            "${aws_s3_bucket.destination_bucket.arn}"
        ],
        Condition = {
          StringEquals = {
            "s3:ResourceAccount": "${data.aws_caller_identity.current.account_id}"
          }
        }
        
      }
    ]
  })
}
data "aws_caller_identity" "current" {}
data "archive_file" "async_function_initial_lambda_artifact" {
    type = "zip"
    output_path = "${path.root}/.archive_files/async_function.zip"
    source {
      filename = "index.js"
      content = <<EOF
exports.handler = async (event, context) => {
    try {
        console.log('Event received:', JSON.stringify(event, null, 2));
        
        // Check for forceError parameter to simulate failures
        if (event.forceError === true) {
            throw new Error('Forced error for testing async failure handling');
        }
        
        // Simulate some async processing
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Example processing logic
        const result = {
            processedAt: new Date().toISOString(),
            eventId: context.awsRequestId,
            input: event
        };
        
        // Log the result
        console.log('Processing completed:', JSON.stringify(result, null, 2));
        
        // Return success response
        return {
            statusCode: 200,
            body: JSON.stringify(result)
        };
    } catch (error) {
        console.error('Error processing event:', error);
        
        // Return error response
        throw new Error('Failed to process event: ' + error.message);
    }
};
EOF
    }
}

# Lambda function with inline code
resource "aws_lambda_function" "async_function" {
  lifecycle {
    ignore_changes = [ 
        filename,
        source_code_hash
     ]
  }

  reserved_concurrent_executions = 0 # set to 0 to directly fail async execution. Check that the bucket correctly populates with the Failure Object.

  function_name = "async_function"
  filename         = "${path.root}/.archive_files/async_function.zip"

  role         = aws_iam_role.lambda_role.arn
  handler      = "index.handler"
  runtime      = "nodejs22.x"
  architectures = ["arm64"]
  environment {
    variables = {
      DESTINATION_BUCKET = aws_s3_bucket.destination_bucket.id
    }
  }
  code_signing_config_arn = null
  source_code_hash = data.archive_file.async_function_initial_lambda_artifact.output_base64sha256
}

# Lambda function async config with destination
resource "aws_lambda_function_event_invoke_config" "async_destination" {
  function_name = aws_lambda_function.async_function.function_name

  destination_config {
    # # Could send to sns, sqs, etc. Does not apply for this example.
    # on_success {
    #   destination = 
    # }
    on_failure {
      destination = aws_s3_bucket.destination_bucket.arn
    }
  }

  maximum_event_age_in_seconds = 60
  maximum_retry_attempts      = 2
}

# Output the generated bucket name
output "destination_bucket_name" {
  value = aws_s3_bucket.destination_bucket.id
}

output "test_with_this_command" {
    value = "aws lambda invoke --function-name async_function --invocation-type Event --payload '{ \"forceError\": true }' --region us-east-1 --cli-binary-format raw-in-base64-out response.json"
  
}
