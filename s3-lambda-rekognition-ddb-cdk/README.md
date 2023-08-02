# Use Event Driven Architecture (EDA) to detect labels using S3, Lambda, Rekognition, and DynamoDB with Cloud Development Kit (CDK)

This pattern demonstrates how to detect labels using an event driven architecture.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

# Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd s3-lambda-rekognition-ddb-cdk
   ```
3. Run below command to install required dependancies:

   ```
   npm install
   ```

4. Run the command below to bootstrap your account. CDK needs it to deploy

   ```
   cdk bootstrap
   ```

5. From the command line, run:
   ```
   cdk deploy --all
   ```

## Testing

1. Run the command below to upload an image to S3 bucket created in the stack which is outputted via the console in the output as `S3LambdaRekognitionStack.bucketName`. The bucket name should be `s3lambdarekognitionstack-imagesbucketdxxxxxxx-xxxxxx`. The image file name can relate to the object in the image. Ex: "Lion.jpg".

   ```
   aws s3 cp <your_image>.jpg s3://[S3BucketName]/<your_image>.jpg
   ```

2. You should see the Rekognition label output in your DynamoDB table.

## Cleanup

1. To delete the stack, run:
   ```bash
   cdk destroy --all
   ```

---

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

# This project was developed with the assistance of AWS CodeWhisperer
