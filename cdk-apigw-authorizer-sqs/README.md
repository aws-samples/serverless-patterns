# CDK Python project for deploying Rest API that can inseet and list Marketplace Metering records.

Marketplace consumption based pricing (a.k.a usage-based dimentions consumption-based dimensions, or metered dimensions) should be reported to AWS Marketplace and must be stored in a DynamoDB table called
AWSMarketplaceMeteringRecords. This table gets created in the Seller’s AWS account as part of AWS Markerplace SaaS quickstart integration. 

Sellers manually insert meterning record into AWSMarketplaceMeteringRecords table. But in production, they are expected to automatically insert records based on monitoring buyers' consumption. 

This CDK project will create API Gateway Rest API endpoints that can help sellers, incorporate them into their Billing systems, to automate sending metering information to AWS Marketplace.


![Alt text](images/MP-metering-records.png?raw=true "Pattern using API gateway to enter Metering records")


This CDK project is written in Python, it has a stacks and can synthesize  cloud formation templates. 
 
##### Stack 'cdk-apigw-markerplace-metering-records' will create:
* API Gateway Rest API with 3 endpoints to insert and list metering records.


Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [CDK Installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) 

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/serverless-patterns/cdk-apigw-markerplace-metering-records.git
```
2. Change directory
```
cd cdk-apigw-markerplace-metering-records
```
3. To manually create a virtualenv on MacOS and Linux:
```
$ python3 -m venv .venv
```
4. After the init process completes and the virtualenv is created, you can use the following to activate virtualenv.
```
$ source .venv/bin/activate
``` 
6. After activating your virtual environment for the first time, install the app's standard dependencies:
```
python -m pip install -r requirements.txt
```
7. Install APIGateway Module
```
python -m pip install aws-cdk.aws-apigateway
```
9. Update 'cdk-apigw-markerplace-metering-records/cdk.context.json' file with your application specific parameters
```
{
    "params":{
        "aws_region_name":"<aws_region_name>",
        "metering_table_name":"AWSMarketplaceMeteringRecords"
    }
}
``` 
10. To generate a cloudformation templates (optional)
```
cdk synth
```
11. To deploy AWS resources as a CDK project
```
cdk deploy 
```

## How it works

At the end of the deployment the CDK output will list stack outputs, and an API Gateway URL. In the customer's AWS account, a REST API with 3 endpoints will be created.

![Alt text](images/MP-apigw-endpoints.png?raw=true "AWS Console showing API Gateway creation")

## Testing
Note: The payload that will be posted to the API’s will only need customer identifier and metered dimension data. Below is some sample data for reference.

# TEST DATA THAT SELLER WILL SEND FOR SINGLE CUSTOMER/BUYER 
"customerIdentifier": "<Customer identifier Value>",
{
    "metered_dimensions": [
        {"dimension_name":"<Metered dimension 1>", "dimension_value":<Metered dimension unit value>},
        {"dimension_name":"<Metered dimension 2>", "dimension_value":<Metered dimension unit value>}
    ]
}
## Example json data.
"customerIdentifier": "ExWoL3vTir2",
{
    "metered_dimensions": [
        {"dimension_name":"metered_1_id", "dimension_value":10},
        {"dimension_name":"metered_3_id", "dimension_value":20}
    ]
}
# TEST DATA THAT SELLER WILL SEND FOR BATCH PROCESSING
{
    "buyers" : [
        {"customerIdentifier": "ExWoL3vTir2",
         "metered_dimensions": [
                {"dimension_name":"metered_1_id", "dimension_value":10},
                {"dimension_name":"metered_2_id", "dimension_value":20}
            ]  
        },
        {"customerIdentifier": "ExWoL3vTir2",
         "metered_dimensions": [
                {"dimension_name":"metered_id_1", "dimension_value":10},
                {"dimension_name":"metered_3_id", "dimension_value":20}
            ]  
        }
    ]
    
}



Test the api invocation using curl:
```
curl -X POST "https://<apigateway-id>.execute-api.<aws-region>.amazonaws.com/prod/sqs" -H "Authorization:testtoken"  -H "Content-Type: application/json" --data '{"status": "ok"}'
```
If the execution is successful, you will get  response similar to
```
{"SendMessageResponse":{"ResponseMetadata":{"RequestId":"2e75dac6-4f87-52ab-8fa4-8615640b84f4"},"SendMessageResult":{"MD5OfMessageAttributes":null,"MD5OfMessageBody":"0d7ac2dec5f281678f65dcf7fe4681ba","MD5OfMessageSystemAttributes":null,"MessageId":"9d72cd66-5aaf-4c0f-8f03-8fc96b7a45e1","SequenceNumber":null}}}
```
You can poll the SQS queue for arrival of the test message.

## Cleanup
 
1. Delete the stack
    ```bash
   cdk destroy STACK-NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    cdk list
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0