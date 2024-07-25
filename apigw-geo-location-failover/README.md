# Amazon API  Gateway GeoLocation REST API Disaster Recovery

Customers often want to access the resources from the same country where user resides and this pattern will help them to achieve the same. This demo also demonstrates an Amazon API Gateway multi-region active-passive public API that proxies two independent multi-region active-passive Lambda function. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

# Requirements

* Create an AWS account if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* AWS CLI installed and configured
* Git Installed
* AWS Serverless Application Model (AWS SAM) installed


# Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```


2. Change directory to:

    ```
    cd apigw-geo-location-failover
    ```

3. From the command line, use AWS SAM to deploy the AWS resources for the stack as specified in the template.yml file on the primary region:

    ```
    sam deploy -—guided —config-env primary
    ```

 - During the prompts:

   * **Stack Name:** Enter a stack name.
   * **AWS Region:** Enter the desired secondary AWS Region. This stack has been tested with both us-east-1 and us-east-2. **Make sure to use a different region from the primary one but within the same country**.
   * **PublicHostedZoneId:** You must have a public hosted zone in Route 53 with your domain name (i.e. mydomain.com). Enter the Hosted Zone Id for this hosted zone.
   * **DomainName:** Enter your custom domain name (i.e. externalapi.mydomain.com).
   * **CertificateArn** You must have an ACM certificate that covers your custom domain namespace (i.e. *.mydomain.com) on the region your are deploying this stack. Enter the ARN for      this certificate here. **Make sure you are getting the certificate arn for the right region**.
   * **FailoverDomainName:** Enter your failover domain name (i.e. failover.mydomain.com)
   * **Priority:** Enter “SECONDARY” here
   * **GeoLocationValue:** Enter the country code 
   * Allow SAM CLI to create IAM roles with the required permissions.
   * Allow SAM CLI to create the LambdaRegionalApi Lambda function.
   * **SAM configuration environment** Accept the **secondary** default value.

    Once you have run `sam deploy --guided --config-env primary` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy --config-env primary` in future to use these defaults.


4. From the command line, use AWS SAM to deploy the AWS resources for the stack as specified in the template.yml file on the secondary region:

    ```
    sam deploy —guided —config-env secondary
    ```

 - During the prompts:

    * **Stack Name:** Enter a stack name.
    * **AWS Region:** Enter the desired secondary AWS Region. This stack has been tested with both us-east-1 and us-east-2. **Make sure to use a different region from the primary one but within the same country**.
    * **PublicHostedZoneId:** You must have a public hosted zone in Route 53 with your domain name (i.e. mydomain.com). Enter the Hosted Zone Id for this hosted zone.
    * **DomainName:** Enter your custom domain name (i.e. externalapi.mydomain.com).
    * **CertificateArn** You must have an ACM certificate that covers your custom domain namespace (i.e. *.mydomain.com) on the region your are deploying this stack. Enter the ARN for      this certificate here. **Make sure you are getting the certificate arn for the right region**.
    * **FailoverDomainName:** Enter your failover domain name (i.e. failover.mydomain.com)
    * **Priority:** Enter “SECONDARY” here
    * **GeoLocationValue:** Enter the country code 
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Allow SAM CLI to create the LambdaRegionalApi Lambda function.
    * **SAM configuration environment** Accept the **secondary** default value.

    Once you have run `sam deploy --guided --config-env secondary` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy --config-env secondary` in future to use these defaults.

```
 Note the output from the SAM deployment process. These contain details which are used for testing.
```

# How it works

1. You will deploy the same template in two separate regions:

-  When you deploy template in the Primary region, it will create a custom domain name , Geolocation route of custom    domain name mapped to failover route, a Primary Record for failover routing mapped to API gateway domain name and Lambda function integrated with API gateway.
- When you deploy template in the Secondary region, it will create a custom domain name,  a Primary Record for failover routing mapped to API Gateway domain name and Lambda function integrated with API gateway.


    2. If an issue with the primary region occurs, you can user Amazon Route53 ARC to route traffic to the secondary region.
    
    3. This example demonstrates the failover only and does not encompass authentication and data for the multiple regions.

Testing

Once the stack is deployed, get the custom domain name output parameter.
Paste the URL in a browser, or in Postman, or using the curl command.
Eg: 

```
curl https://externalapi.mydomain.com/
```

You should see a response similar to when request made from the same country as GeoLocation:

```
{"message" : "Hello World! This is the regional API"}
```

You should see a response similar to when request made from the same country as GeoLocation:

```
  Could not resolve host: https
  Closing connection
  curl: (6) Could not resolve host: https
```



# Cleanup

1. Delete the stack on the primary region.

    ```
    sam delete --config-env primary
    ```

2. Delete the stack on the secondary region.

    ```
    sam delete --config-env secondary
    ```
