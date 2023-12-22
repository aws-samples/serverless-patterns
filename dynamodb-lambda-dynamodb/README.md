# multi-region-data-replication
This is a serverless solution for multi-regio data replication that can help store consistent data across different regions.
![image](https://github.com/saiaunghlyanhtet/multi-region-data-replication/assets/71708201/d2120c4c-0182-4545-9775-d3110f37e836)

The terraform template deploys a Lambda function, two DynamoDB in different regions, and the minimum IAM resources required to run the application.

When items are written or updated or deleted in the table in first region (e.g. us-east-1), the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. When the function is invoked, it retrieves data from the payload containing the contents of the table item that has been written or updated or deleted in the table in the first region, then it makes changes in the table of the second region (e.g. us-west-2) based on the event type.

## Requirements
- [Create an AWS account](https://aws.amazon.com/) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://aws.amazon.com/) installed and configured
- [Git](https://git-scm.com/downloads) Installed
- [Terraform CLI](https://developer.hashicorp.com/terraform/install) installed and configured

## Deployment Instructions
1. Create a new directory, navigate to that directory, and clone the repository.
   ```
   git clone git@github.com:saiaunghlyanhtet/multi-region-data-replication.git
   ```

2. Change directory to the project directory.
   ```
   cd multi-region-data-replication
   ```

3. Build the Java Lambda Function jar file using Maven.
   ```
   mvn clean package
   ```

4. From the command line, initialize terraform to to download and install the providers defined in the configuration.
   ```
   terraform init
   ```

5. From the command line, plan the resouces in the configuration.
   ```
   terraform plan -out plan.tfplan
   ```

6. From the command line, apply the configuration.
   ```
   terraform plan plan.tfplan
   ```

7. During the prompts:
   - Enter yes

## How it works
When items are written or updated or deleted in the table in first region (e.g. us-east-1), the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. When the function is invoked, it retrieves data from the payload containing the contents of the table item that has been written or updated or deleted in the table in the first region, then it makes changes in the table of the second region (e.g. us-west-2) based on the event type.

## Testing
Everytime after having made changes in the table in the first region, those changes will be reflected in the table of the second region. You can also see the detailed logs in the cloudwatch log group for the lambda function.

## Clean Up
1. Delete all deployed resouces.
   ```
   terraform destroy
   ```

2. During the prompts
   - Enter yes

3. Confirm all created resources are deleted.
   ```
   terraform show
   ```
