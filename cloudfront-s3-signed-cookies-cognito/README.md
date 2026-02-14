# Amazon CloudFront signed cookies with Amazon Cognito authentication using Python CDK

This pattern demonstrates how to implement Amazon CloudFront signed cookies for private S3 content access with Amazon Cognito user authentication using AWS CDK with Python.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed and configured 
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.9+](https://www.python.org/downloads/) installed
* [Docker] required during the building process

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd cloudfront-s3-signed-cookies-cognito
    ```
3. Create a virtual environment for Python:
    ```bash
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
    For Windows:
    ```bash
    .venv\Scripts\activate.bat
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Bootstrap your AWS account for CDK (if you haven't done so already):
    ```bash
    cdk bootstrap
    ```
7. Deploy the stack:
    ```bash
    cdk deploy
    ```
Note the outputs from the CDK deployment. These contain the API endpoints, CloudFront distribution URL, and other important resource information.

## How it works

This pattern creates a secure content delivery solution using CloudFront signed cookies with the following workflow:

1. **User Registration**: Users register via the `/register` API endpoint, which creates a new user in the Amazon Cognito User Pool.

2. **User Authentication**: Users authenticate via the `/login` API endpoint with their email and password. Upon successful authentication:
   - Cognito returns JWT tokens (ID token, access token, refresh token)
   - The Lambda function retrieves the CloudFront private key from AWS Secrets Manager
   - CloudFront signed cookies are generated with a configurable TTL
   - Both Cognito tokens and signed cookies are returned to the client

3. **Content Access**: 
   - Public content under the default path is accessible without authentication
   - Private content under the `/private/*` path requires valid CloudFront signed cookies
   - The CloudFront distribution validates the signed cookies against the configured Key Group

4. **Security**:
   - S3 bucket is configured as private with no public access
   - CloudFront uses Origin Access Control (OAC) to securely access S3 content
   - RSA key pairs are used for signing, with the private key securely stored in AWS Secrets Manager
   - The public key is configured in a CloudFront Key Group for cookie validation

## Architecture Components

- **Amazon Cognito User Pool**: Manages user registration and authentication
- **API Gateway**: REST API with `/register` and `/login` endpoints
- **AWS Lambda**: Two functions for user registration and login (with signed cookie generation)
- **AWS Secrets Manager**: Securely stores the CloudFront private key
- **Amazon S3**: Hosts private content accessible only via CloudFront
- **Amazon CloudFront**: 
  - Distribution with Origin Access Control (OAC)
  - Public Key and Key Group for signed cookie validation
  - Behavior rules for public vs private content
- **AWS Lambda Powertools**: For structured logging and observability

## Testing

### 1. Register a new user

```bash
curl -X POST https://{API_ENDPOINT}/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "TestPassword123!",
    "name": "Test User"
  }'
```

### 2. Login and receive signed cookies

```bash
curl -X POST https://{API_ENDPOINT}/login \
  -H "Content-Type: application/json" \
  -c cookies.txt \
  -d '{
    "email": "user@example.com",
    "password": "TestPassword123!"
  }'
```

The response includes Cognito tokens and CloudFront signed cookies (`CloudFront-Policy`, `CloudFront-Signature`, `CloudFront-Key-Pair-Id`).

### 3. Upload test content to S3

```bash
# Upload public content
aws s3 cp test/public_content.html s3://{BUCKET_NAME}/public_content.html

# Upload private content
aws s3 cp test/private_content.html s3://{BUCKET_NAME}/private/private_content.html
```

### 4. Access public content (no authentication required)

```bash
curl https://{CLOUDFRONT_DOMAIN}/public_content.html
```

### 5. Access private content (requires signed cookies)

```bash
# Without cookies (should fail)
curl https://{CLOUDFRONT_DOMAIN}/private/private_content.html
```

Following commands will extract the signed cookies from the response and use them to access private content:

```bash
# Extract CloudFront signed cookie values from cookies.txt
CF_POLICY=$(awk -F'\t' '$6=="CloudFront-Policy"{print $7; exit}' cookies.txt)
CF_SIG=$(awk -F'\t' '$6=="CloudFront-Signature"{print $7; exit}' cookies.txt)
CF_KID=$(awk -F'\t' '$6=="CloudFront-Key-Pair-Id"{print $7; exit}' cookies.txt)

curl -H "Cookie: CloudFront-Policy=$CF_POLICY; CloudFront-Signature=$CF_SIG; CloudFront-Key-Pair-Id=$CF_KID" \
  https://{CLOUDFRONT_DOMAIN}/private/private_content.html
```

## Configuration

The stack supports the following context variables in `cdk.json`:

- `allowed_cors_origin`: CORS origin for API Gateway (default: "*")
- `cookie_domain`: Domain for CloudFront signed cookies (optional)
- `same_site`: SameSite attribute for cookies (default: "None")
- `cookie_ttl_seconds`: TTL for signed cookies in seconds (default: 600)

Example:
```bash
cdk deploy -c allowed_cors_origin="https://example.com" -c cookie_ttl_seconds=3600
```

## Cleanup
 
1. Empty the S3 bucket (if you uploaded any content):
    ```bash
    aws s3 rm s3://{BUCKET_NAME} --recursive
    ```
2. Delete the stack:
    ```bash
    cdk destroy
    ```
3. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'CloudFrontSignedCookiesStack')].StackStatus"
    ```

