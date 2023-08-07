# Use event-driven architecture (EDA) to promote worker safety using Amazon S3, AWS Lambda, Amazon Rekognition, and AWS IoT Core

This pattern demonstrates how to detect if individuals are wearing the correct personal protective equipment (PPE) and sends an alert via IoT Core. This pattern is compatible with the published [AWS IoT Puppy Park workshop](https://catalog.workshops.aws/iot-puppy-park). 

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
   cd s3-lambda-rekognition-iot-cdk
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

1. In the AWS console, go to the AWS IoT Core service. IN the left sidebar, choose the MQTT test client under Test. Subscribe to the topic that the Lambda function will publish to:`Bittle1/sub`. You are now subscribed to MQTT topic. 

1. Run the command below to upload an image with individuals wearing PPE (or not) to the S3 bucket created in the stack. The bucket name should be:
`ppeiotviolationsstack-imagesbucketXXXX-XXXX`.  Ex: "Worker.jpg".

   ```
   aws s3 cp Worker.jpg s3://[S3BucketName]/Worker.jpg
   ```

2. You should see the message ("khi") in IoT core under the topic ("Bittle1/sub") if there is a violation. If this was set up with the [IoT Puppy Park workshop](https://github.com/novekm/iot-puppy-park), the bittle should perform the 'hi' action.

## (Optional) Configuration
You can set environment variables for the Lambda function for the following in 
`s3-lambda-rekognition-iot-cdk/lib/s3-lambda-rekognition-iot-stack.ts`:

1. Change the IoT Core Topic
2. Change the IoT Core Message
3. Change the required PPE for alerts
4. Set the Rekognition confidence level


## Cleanup

1. To delete the stack, run:
   ```bash
   cdk destroy --all
   ```

---

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

# This project was developed with the assistance of AWS CodeWhisperer
