# Serverless pattern to integrate EventBridge and ECS-Fargate tasks

![Serverless Pattern Architecture](/EventBridge/s3-eb-ecs.png)

This serverless pattern uses EventBridge to trigger multiple ECS tasks on Fargate. The ECS task queries the S3 bucket for files and reads them. These ECS tasks can be extended to insert the data to a database, thus speeding up the process of loading data from S3 to a database.

This application pattern can be extended to

    1. Process a file from a single bucket in parallel
    2. Perform long running tasks not suited for Lambda processing in parallel

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

# Requirements

- [Create an AWS account](https://aws.amazon.com) if you do not already have, create them and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Terramform installed](https://www.terraform.io/)

# Deployment Instructions

1. Configure AWS CLI to the account and region you want to deploy the application to

2. Create a new directory then navigate to that directory in a terminal and clone the GitHub repository:
    ~~~ code
    git clone https://github.com/aws-samples/serverless-patterns
    
3. Change directory to the pattern directory:
    ~~~ code
    cd serverless-patterns/eventbridge-ecs
    
4. Go to the [Docker directory](./docker/README.md) and execute the docker command and bash script to do the following:
    - Create the ECR Repository
    - Create the task image and push it to the repository
    - Note the ARNs of the image name for the task. The ARN and image name will be needed in terraform script

5. Make the following changes in the [terraform script](./terraform/pattern_s3_eb_ecs.tf) located inside of terraform folder:
    - Put an unique S3 bucket name in line 2
    - Put the image URI in the line 4
    - Put a subnet block in line 5
    - Put the AWS region where the script will deploy resources in line 6

    ~~~~ code
    #Sample Configuration
    locals {
        bucket_name     = "mybucketname"
        event_bus_name  = "default"
        container_image = "123456789000.dkr.ecr.us-east-2.amazonaws.com/myimagename:latest"
        ecs_subnet_id   = "subnet-00000000000000000"
        region          = "us-east-1"

    }

6. Execute the following terraform command to deploy the stack

    ~~~~ code
    terraform init
    terraform plan
    terraform apply -auto-approve

7. The terraform will create a ECS cluster and deploy the image (created in step 4) in ECS. The script will use the default EventBridge event bus and create S3 notification rule to the default event bus.The rule will listen to the S3 upload events in the incoming folder. The script will provision all the necessary IAM roles and policies to execute the pattern

# Testing

1. Once the terraform script executed successfully, create a folder called 'incoming' inside the newly created S3 bucket and upload a sample csv file

2. The S3 file upload will trigger an EventBridge Rule which will call the ECS task. The ECS task will execute and print the csv data in the cloudwatch log

3. Check the CloudWatch log group to see the ECS task execution details. the logs can be found in /ecs/serverlessland-dump-env-vars

# Cleanup

1. For deleting the EventBridge, S3, ECS task and associated IAM roles and policies, execute the following command:

    ~~~ code
    terramform destroy
    
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
