# AWS Lambda function to Amazon Aurora Serverless

The pattern creates an AWS Lambda function and an Amazon Aurora Serverless cluster, a Log group and the IAM resources required to run the application. The database credentials are stored in AWS Secrets Manager secret.

The Lambda function is written in Python that uses pymysql client to establish connectivity with the serverless database.

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md).

## Steps

First of all, you will need to install the 'pymysql' client depedency which is used in the Lambda function code.
```shell
cd src/function
pip3 install -r requirements.txt -t .
cd ../..
```
Then perform the following terraform commands to deploy the stack
```shell
terraform init
terrform apply
```

Naming constraints with Amazon Aurora for Master password:
- The password for the database master user can include any printable ASCII character except /, ', ", @, or a space.
- The password can contain the following number of printable ASCII characters depending on the DB engine: Aurora MySQL: 8–41 and Aurora PostgreSQL: 8–99.
For more information, please refer to [this](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html#RDS_Limits.Constraints)



## Testing

After deployment, invoke Lambda function with multiple inputs, and go to the Step Function Console and view the different invocations to note the different behavior with the different inputs.

To do this, you can run these commands in the terminal (replace `<function-name>` with the value returned in `lambda_function_name`):

```shell
aws lambda invoke --function-name <function-name> --payload '{"key": "value"}' response.json
```
## Output

Upon successful invocation, the function returns the following response -

```json
{
  "statusCode": 200,
  "body": "{\"message\": \"Successfully connected to the database\", \"database\": \"mydb\", \"host\": \"aurora-serverless-cluster.cluster-cna4c0mg426r.us-east-1.rds.amazonaws.com\"}"
}
```

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= "5.84.0" |