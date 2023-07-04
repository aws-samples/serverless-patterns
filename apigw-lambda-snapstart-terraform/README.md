# Amazon API Gateway, AWS Lambda and Amazon DynamoDB with Lambda SnapStart for Java deployed with Terraform

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) installed
* [Maven](https://maven.apache.org/)
* [Artillery CLI](https://www.artillery.io/docs/guides/getting-started/installing-artillery)

## Deployment Instructions


1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-lambda-snapstart-terraform
    ```
3. Build the function:
    ```
    cd UnicornStockLambda
    mvn package
    cd ..
    ```    
4. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
5. Deploy the infrastructure
    ```
    terraform apply
    ```
6. Confirm that it was deployed correctly
    ```
    terraform show
    ```


## Testing

To test the Lambda function you can run the artillery load test with the following commands

```bash
export API_GW_URL=$(terraform output -raw apigw-url)
artillery run -t $API_GW_URL -v '{ "url": "/transactions" }' UnicornStockLambda/misc/loadtest.yaml
```

## Measuring the results

You can use the following AWS CloudWatch Insights query to measure the duration your SnapStart Lambda function.

```
filter @type = "REPORT"
  | parse @log /\d+:\/aws\/lambda\/(?<function>.*)/
  | parse @message /Restore Duration: (?<restoreDuration>.*?) ms/
  | stats
count(*) as invocations,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 0) as p0,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 25) as p25,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 50) as p50,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 90) as p90,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 95) as p95,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 99) as p99,
pct(@duration+coalesce(@initDuration,0)+coalesce(restoreDuration,0), 100) as p100
group by function, (ispresent(@initDuration) or ispresent(restoreDuration)) as coldstart
  | sort by coldstart desc
```

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd apigw-lambda-snapstart-terraform
    ```
2. Delete all created resources
    ```bash
    terraform destroy
    ```
3. During the prompts:
   * Enter yes
4. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
