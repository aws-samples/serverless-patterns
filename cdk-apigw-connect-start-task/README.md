
# CDK Python project for deploying API Gateway integration with Amazon Connect

This CDK project is written in Python, it has a stacks to synthesize cloud formation templates. Customers will be able to  deploy 
    
    API Gateway Rest API with a POST method acting as a proxy to Amazon Connect,
    
    Amazon SQS queue to store the payload posted

Stack 'APigwSqsStack' will create:

    API Gateway Rest API with a POST method acting as a proxy to SQS,
    Amazon SQS queue to store the payload posted

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.