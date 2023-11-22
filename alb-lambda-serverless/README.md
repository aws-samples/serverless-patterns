# Application Load Balancer with Lambda as a target

This pattern registers the lambda function as the target for the Application Load Balancer.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [NodeJS](https://nodejs.org/en/download/) (LTS version) installed
* [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` sh
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ``` sh
    cd serverless-patterns/alb-lambda-serverless
    ```

1. From the command line, use npm/yarn to install the development dependencies:

    ``` sh
    npm install
    ```
    -or-

    ``` sh
    yarn install
    ```

1. From the command line, use Serverless Framework to deploy the AWS resources for the pattern as specified in the serverless.yml file:

    ``` sh
    serverless deploy --verbose
    ```

    The above command will deploy resources to `ap-south-1` region by default. You can override the target region with `--region <region>` CLI option, e.g.

    ``` sh
    serverless deploy --verbose --region us-west-2
    ```

1. Note the `LoadBalancerDNSName` output from the Serverless Framework deployment process. You will use this value for testing.

## How it works

This pattern registers the lambda function as the target for the Application Load Balancer. When the load balancer endpoint is hit in the browser, if the specified URL (`/hello`) path matches, it triggers the lambda function & the file (hello) is downloaded in your local system with the output from lambda function.


## Testing

### Hit the Load Balancer DNS endpoint.

To test the endpoint, paste the output URL obtained from serverless framework in the browser of your choice.

### Expected result

As no specific URL path is provided, it returns the default output i.e. 404-Page Not Found.
```html
Page Not Found
```

Now edit the URL by appending the `/hello` path in it. This will download a file named `hello` in your local system. The file will have the following content.

```json
<p>Lambda function integrated with ALB called</p>
```

### CloudWatch logs

Open AWS CloudWatch Console and navigate to [/aws/lambda/alb-lambda-serverless-prod-functionOne](https://ap-south-1.console.aws.amazon.com/cloudwatch/home?region=ap-south-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Falb-lambda-serverless-prod-functionOne/) log group.
You should be able to see a new Event Stream with the Received Event information, and Event Message, logged into the stream.




## Cleanup

1. Delete the stack

    ```sh
    serverless remove --verbose
    ```

1. Confirm the stack has been deleted

    ```sh
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'alb-lambda-serverless-prod')].StackStatus"
    ```

    Expected output

    ```json
    [
        "DELETE_COMPLETE"
    ]
    ```

    NOTE: You might need to add `--region <region>` option to AWS CLI command if you AWS CLI default region does not match the one, that you used for the Serverless Framework deployment.

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0