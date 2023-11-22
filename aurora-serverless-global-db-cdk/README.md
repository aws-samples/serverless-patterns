# Amazon Aurora Serverless V2 Primary to Secondary Global Database
The pattern creates a serverless global database cluster enabling data replication from the primary to secondary cluster. The regional primary cluster contains a serverless db instance supporting both writes and reads. The regional secondary cluster contains a serverless db instance supporting only reads. In the unlikely event of a regional degradation or outage, the secondary region can be promoted to read and write capabilities in less than 1 minute. Also the pattern adopts the multiple stack capability of CDK to provision the resources across the primary and secondary regions. You can deploy each stack indvidually or deploy all the stacks using --all option.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/aurora-serverless-global-db-cdk](https://serverlessland.com/patterns/aurora-serverless-global-db-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed.
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd aurora-serverless-global-db-cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Configure AWS CDK to bootstrap the AWS account, primary region and secondary region :
    ```
    cdk bootstrap 111111111111/eu-west-1
    cdk bootstrap 111111111111/eu-west-2
    ```
5. From the command line, use AWS CDK to deploy the all the stacks synthesized: 
    ```
    cdk deploy --all
    ```
    Alternatively you can also deploy each stack individually. From the command line, use AWS CDK to deploy each stack: 
    ```
    cdk deploy aurora-global-cluster
    cdk deploy primary-cluster
    cdk deploy secondary-cluster
    cdk deploy primary-test-app
    cdk deploy secondary-test-app
    ```
7. Note the outputs from the CDK deployment process. These contain the primary and secondary URLs which are used for testing.

## How it works

- The template in this pattern synthesizes five stacks for deployment using the multiple stack approach of CDK. 
- The first stack named aurora-global-cluster creates the Aurora Global Cluster. 
- The second stack named primary-cluster deploys the primary cluster with a serverless v2 instance in the primary region defined.
- The third stack named secondary-cluster deploys the secondary cluster with a serverless v2 instance in the secondary region defined.
- The fourth and fifth stack named primary-test-app and secondary-test-app deploys a fargate container with a nodejs app for testing the global database tables. 
- The primary cluster supports both write and read operations. The secondary cluster supports read operation only.
- Once you deploy all the stacks, you have built a global database that automatically replicates data from the primary to the secondary region.

## Testing

Note down the primary-test-app.FargateServiceURL and secondary-test-app.FargateServiceURL values from the CDK output and update them in each of the test commands below. 

1.  Initialize the Global Database by creating a table 

    ```
    curl primary-test-app.FargateServiceURL/init
    ```

    Expected Response :
    "Task table created.."

2. Write a task into the Primary Cluster 
    ```
    curl -X POST primary-test-app.FargateServiceURL/tasks -H 'Content-Type: application/json' -d '{"name":"Task1","status":"created"}'
    ```
    Expected Response : Task added with ID: 1
3. Read the tasks from the Secondary cluster 
    ```
    curl secondary-test-app.FargateServiceURL/tasks 
    ```
    Expected Response : 
    [{"id":1,"name":"Task1","status":"created"}]

4. Attempt to write a task into the Secondary cluster 
    ```
    curl -X POST secondary-test-app.FargateServiceURL/tasks -H 'Content-Type: application/json' -d '{"name":"Task1","status":"created"}'
    ```
    Expected Response : error : cannot execute INSERT in a read-only transaction
    
    Note : You can enable Write forwarding feature to continue to use the Secondary cluster endpoint for write transactions as well. 

5. You can also try to update and delete the task on the Primary cluster 
    ```
    curl -X PUT primary-test-app.FargateServiceURL/tasks/1 -H 'Content-Type: application/json' -d '{"name":"Task1","status":"in-progress"}'

    curl -X DELETE primary-test-app.FargateServiceURL/tasks/1

    ```
6. Check if the task is deleted from the Secondary cluster 
    ```
    curl secondary-test-app.FargateServiceURL/tasks 
    ```
    Expected Response : 
    []

## Cleanup
 
1. Delete the stack
    ```
    cdk destroy --all 
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
