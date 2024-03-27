# IaC Template for CloudWatch Logs to OpenSearch Serverless



## Overview


This document describes the process to deploy this solution architecture within your own AWS account.  The automation  provided is a CloudFormation YAML template that is divided into two parts:

[Image: cloudformation_architecture.png]
1. **Backend Template:** provides the core services to ingest CloudWatch Logs, transform them to JSON objects for OpenSearch, store the logs in an S3 archive, and load into an OpenSearch Serverless Collection
2. **Frontend Template:** provides an example of how to configure CloudWatch Log Groups with a CloudWatch Subscription to emit logs to Kinesis Data Fireose.  Also includes a test application that generates variety of fake data in JSON format to be able to analyze in OpenSearch Serverless.



## Installation

Follow these installation steps to build this solution architecture in your own account.  


### Step 1: Download the Cloudformation Templates


![Backend Template](cloudwatch-to-opensearch-backend-v4.yml)

![Frontend Template](cloudwatch-to-opensearch-frontend-v2.yml)



### Step 2: Create Backend Stack

1. Log into AWS console with User or Role with sufficient administrative privilege to create the components
2. Go to **Cloudformation** → **Stacks** → **Create stack with new resources (standard)**
3. For Template source, choose **Upload a template file** and use **Choose file** button to upload the backend template file.  Choose **Next**.
4. Enter a stack name:  `cw-to-oss-backend`
5. For Parameters, change the OSSADMIN value to an administrator role to use for access to OpenSearch Serverless.  The role should be one you are in so you can access the dashboard.  If unsure, use the top right drop down to copy your user identity and then paste into the parameter field.  Remove the “/” and everything after it to leave just the role name.  Choose **Next**.
6. Leave stack options to default and Choose **Next**.
7. Under review and create, go to Capabilities and select “**I acknowledge that AWS CloudFormation might create IAM resources with custom names**.  Choose **Submit**.
8. When stack is complete, go to Output and copy the values for **Kinesis Firehose Arn** and **CloudWatch Logs Role Arn**.



### Step 3:  Create Frontend Stack

1. Go to **Cloudformation** → **Stacks** → **Create stack with new resources (standard)**
2. For Template source, choose **Upload a template file** and use **Choose file** button to upload the backend template file.  Choose **Next**.
3. Enter a stack name:  ```cw-to-oss-frontend```
4. For Parameters, change the following:
    1.  **CloudWatchLogsToKinesisRoleArn:** change to the **CloudWatch Logs Role Arn** copied previously.
    2.   **KinesisFirehoseDeliveryStreamArn :** change to the **Kinesis Firehose Arn** copied previously.
5. Leave stack options to default and Choose **Next**.
6. Under review and create, go to Capabilities and select “**I acknowledge that AWS CloudFormation might create IAM resources with custom names**.  Choose **Submit**.



## Testing

With both stacks created, you can now test the overall data flow from CloudWatch to OpenSearch Serverless.  


### Generating Logs

1. In AWS Console, Go to **Lambda** → **Functions**
2. Choose **cloudwatch-oss-test**
3. Select the blue drop down button next to **Test** and choose **Configure test event.**
    
4. [Image: images/iac8.PNG]
5. Configure a test event by giving it a name:  ```test``` and **Save** it.
6. [Image: images/iac9.PNG]
7. Click the Test button and run the test event for this Lambda.  Each invocation will generate fake logs for a fictitious banking app that  will log customer, account, and transaction data.  You will see a generic response indicating the test run is complete.

```
Response
{
    "statusCode": 200,
    "body": "\"Test Complete!\""
}

```

1. After a minute, check the **S3 bucket** created (named **clooudwatch-logs-to-osis**-<random value>).  There should be a folder structure in the bucket based on the time of the logs.  Follow it down to see the processed log file.  
2. Run the test multiple times to get log data generated for ingestion into OpenSearch.  Each run will generate pseudo-random data based on four fictional customers.



### Analyzing Logs

1. In the console, go to **Amazon OpenSearch Service → Collections → oss-cloudwatch Dashboard
    **
2. A new tab opens to the OpenSearch console
3. click on **Manage** in the upper right corner and select **Index Patterns**
 [Image: images/iac1.PNG]
4. You should be presented with the following screen.  Chose to **Create index pattern**.
 [Image: images/iac2.PNG]
5. For index pattern, enter “*****” and go to **Next Step.**  
 [Image: images/iac3.PNG]
6. Choose the **@timestamp** field for the Time field.  This corresponds to the ingestion timestamp added during OpenSearch Ingestion.  Choose **Create index pattern**.  Note that you will be presented with all the objects found in the index, including those customer, account, and transaction fields.
 [Image: images/iac4.PNG]
7. Go to the discovery screen (by choosing hamburger menu on top left of window and then Discover).  You will now see the main search screen with data ingested from your log bucket.  Note the fields on the left that have been auto-discovered based on the JSON format ingested by OpenSearch Ingestion Service.
 [Image: iac6.PNG]
8. Search through the data by selecting fields and choosing a specific value.  Or use the search bar to add your own query in DQL format.  
[Image: images/iac7.PNG]
9. Expand the document to see the fields created by the transform Lambda.  Note how JSON object messages were handled differently than plain text messages.

## Clean-Up

When removing resources, be sure to delete all objects in the s3 bucket first.  Go to the bucket and select the top level directory and choose to delete the files.  You will need to confirm by typing **permanently delete.**

1. Go to the AWS console → **CloudFormation** → **Stacks**
2. Select the **backend** Stack and click the **Delete** button.  Confirm that you agree to delete permanently.
3. Perform the same step for the **frontend** Stack

