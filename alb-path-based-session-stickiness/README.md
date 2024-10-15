
# ALB Path-Based Session Stickiness

## Project Description and Purpose

This project demonstrates how to implement path-based session stickiness using AWS CDK with Python. The purpose is to showcase a solution for maintaining user sessions based on specific URL paths in an Application Load Balancer (ALB) environment.

## Architecture

The architecture consists of:
- An Application Load Balancer (ALB)
- EC2 instances as targets
- A Lambda function for cookie generation
- CloudWatch for monitoring and logging

The ALB uses path-based routing and a Lambda function to generate session cookies, ensuring requests are directed to the same target based on the URL path.

## Requirements

- AWS Account
- AWS CLI configured with appropriate permissions
- Python 3.7 or later
- Node.js 10.13.0 or later
- AWS CDK CLI

## Deployment Instructions

1. Clone the repository
2. Navigate to the project directory
3. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Synthesize the CloudFormation template:
   ```
   cdk synth
   ```
6. Deploy the stack:
   ```
   cdk deploy
   ```

## How it Works

1. The ALB receives incoming requests
2. Based on the URL path, the ALB triggers the Lambda function
3. The Lambda function generates a session cookie
4. The ALB uses this cookie to maintain session stickiness
5. Subsequent requests with the same cookie are routed to the same target

## Testing

To test the deployment:
1. Access the ALB URL provided in the deployment output
2. Navigate through different paths and observe the session stickiness behavior
3. Monitor the CloudWatch logs for the Lambda function and ALB

## Cleanup

To avoid incurring future charges, remember to destroy the resources:

```
cdk destroy
```

## Useful Commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
