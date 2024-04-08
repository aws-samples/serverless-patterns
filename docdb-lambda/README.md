# Amazon DocumentDB to AWS Lambda Event Source Mapping

This pattern creates an AWS Lambda function to process events in an Amazon DocumentDB (with MongoDB compatibility) change stream by configuring an Amazon DocumentDB cluster as an event source.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/docdb-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed 
* [AWS VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) This can be a default VPC or a Custom VPC.
* [Two Private Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) The Private Subnets should be configured in the above VPC, and should have a NAT Gateway attached to their '0.0.0.0' route. The NAT Gateway should be configured with a Public Subnet (Subnet with Interet Gateway attached). 

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd docdb-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter a name for your DocumentDB Cluster
    * Enter a name for your DocumentDB Instance
    * Enter the DocumentDB Instance Class (Eg. db.t3.medium)
    * Enter the VPC ID where the resources needs to be created
    * Enter the First Private Subnet ID that belongs to the above VPC
    * Enter the Second Private Subnet ID that belongs to the above VPC
    * Enter the Username for AWS Secrets manager to authenicate with Amazon DocumentDB
    * Enter the Password for AWS Secrets manager to authenicate with Amazon DocumentDB
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates Amazon DocumentDB Cluster along with an AWS Lambda Function in the supplied VPC configurations. An Event Source Mapping (ESM) is created that will help Lambda to process the events from a change stream in DocumentDB. The ESM will use AWS Secrets Manager to authenticate the Lambda client to DocumentDB. Two Security Groups will be created for DocumentDB and Lambda function to ensure connectivity for DocumentDB and the Lambda function.

In this tutorial, we will be creating a database **'docdbdemo'** and a collection **'products'**. We will be tracking changes to this **'products'** collection and activate change streams here.

Whenever a record in the **'products'** collection updates, the Lambda service will receive an Event and invoke the Lambda function. 
This function will print the event received from ESM in its CloudWatch logs.

The credentials mentioned under Secret Manager will be used by clients for connecting to DocumentDB.

You can check this [AWS Documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html) for more information.


## Testing

We will be referring this [AWS Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html) for testing.

You can use an EC2 instance / AWS Cloud9 for connecting to the DocumentDB Cluster and test the architecture using below steps:

1. Setup an EC2 instance / AWS Cloud9 in the same VPC and configure the Security Group for connecting to the DocumentDB Cluster. 
    The Default Outbound Rule allows All Traffic to everything, which should be fine for our scenario.
    [AWS Documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html#docdb-cloud9-environment)

2. Install Mongo Shell in your EC2 instance / Cloud9 by executing below commands in the terminal:
    
    Create the MongoDB repository file by downloading the metadata from repo.mongodb.org for Amazon linux and save the repository file in /etc/yum.repos.d directory.
    ```
    echo -e "[mongodb-org-4.0] \nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/4.0/x86_64/\ngpgcheck=1 \nenabled=1 \ngpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc" | sudo tee /etc/yum.repos.d/mongodb-org-4.0.repo
    ```

    Install the mongo shell
    ```
    sudo yum install -y mongodb-org-shell
    ```

    Download the public key for Amazon DocumentDB to encrypt data in transit
    ```
    wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
    ```
    [AWS Documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html#docdb-install-the-mongo-shell)

3. Connect to DocumentDB Cluster from EC2 / Cloud9:
    
    ```
    mongo --ssl --host <Your_DocumentDB_Cluster_Endpoint>:27017 --sslCAFile global-bundle.pem --username <your_username> --password  <your_password>
    ```
    Make sure to replace the DocumentDB Cluster Endpoint that you can find in the output of SAM template.
    Also make sure to use the same Username and Password that you specified in SAM parameters for Secrets Manager.

    After entering the above command, if the command prompt becomes rs0:PRIMARY>, then you’re connected to your Amazon DocumentDB cluster.

    [AWS Documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html#docdb-connect-to-cluster)

4. Activating change streams using below commands :
    
    Create a database called **'docdbdemo'**
    ```
    use docdbdemo
    ```

    Insert a record into docdbdemo:
    ```
    db.products.insert({"hello":"world"})
    ```

    Activate change streams on the **'products'** collection of the **'docdbdemo'** database
    ```
    db.adminCommand({modifyChangeStreams: 1,
        database: "docdbdemo",
        collection: "products", 
        enable: true});
    ```
    [AWS Documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html#docdb-activate-change-streams)

5. Invoking the Lambda by inserting, updating and deleting a record in **'products'** collection of the **'docdbdemo'** database

    Inserting a record
    ```
    db.products.insert({"name":"Pencil", "price": 1.00})
    ```

    Updating the above record
    ```
    db.products.update(
        { "name": "Pencil" },
        { $set: { "price": 0.50 }}
    )
    ```

    Deleting the above record
    ```
    db.products.remove( { "name": "Pencil" } )
    ```

6. Go to the CloudWatch log group **aws/lambda/DocDBLambda** of the Lambda Function to verify the invocations. There should be three execution logs generated for the above tests.


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0