# Amazon ECS Express Mode service with AWS CDK

This pattern deploys a containerized Node.js web application on [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html) with the AWS CDK in TypeScript. You give Express Mode a container image and two IAM roles, and it creates a Fargate service, an internet-facing Application Load Balancer with HTTPS, auto scaling, logging and a URL for the service.

AWS App Runner is closed to new customers, and AWS recommends Amazon ECS Express Mode as the replacement. See [App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html). This pattern used to deploy the same app on App Runner.

The CDK app builds the image from the `cdk/src` folder with `DockerImageAsset` when you run `cdk deploy`, so you don't need to push an image to Amazon ECR first. The stack defines the service with the `AWS::ECS::ExpressGatewayService` CloudFormation resource (`CfnExpressGatewayService` in `aws-cdk-lib`) and passes an environment variable to the container.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apprunner.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node.js](https://nodejs.org/) 22 or later
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) CLI 2.1148.0 or later. `npx aws-cdk@latest` works too.
- Docker or another container runtime, to build the image
- A default VPC with public subnets in the Region you deploy to. Express Mode puts the load balancer there when you don't give it subnets.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/apprunner-cdk/cdk
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. If you haven't used the CDK in this account and Region before, bootstrap it:
   ```bash
   cdk bootstrap aws://ACCOUNT-NUMBER/REGION
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```
6. Note the outputs from the CDK deployment process. `ExpressServiceEndpoint` is the URL you use for testing.

## How it works

- `cdk deploy` builds the image from the files in `cdk/src` and pushes it to the CDK bootstrap ECR repository.
- The stack creates an ECS cluster, a task execution role with `AmazonECSTaskExecutionRolePolicy`, and an infrastructure role with `AmazonECSInfrastructureRoleforExpressGatewayServices`.
- The `AWS::ECS::ExpressGatewayService` resource runs the image on Fargate with 1 vCPU and 2 GB of memory, on container port 80, and health checks `/`.
- Using the infrastructure role, ECS creates an internet-facing Application Load Balancer with a TLS certificate, security groups, an auto scaling policy and a CloudWatch log group, and gives the service a URL in the format `https://<service-name>.ecs.<region>.on.aws`.

The service is public: anyone with the URL can call it. That fits this hello-world sample. For an app that holds private data, add authentication in the app, or put the service in private subnets with the `NetworkConfiguration` property.

## Testing

Get the service URL from the `ExpressServiceEndpoint` output of `cdk deploy`. The service can take a few minutes to become active after the stack finishes.

The service has one endpoint, `/`. A GET request returns a JSON hello message:

```bash
curl https://<ExpressServiceEndpoint>/
```

The response looks like this:

```json
{"message":"Hello from Amazon ECS Express Mode service running in region us-east-1 !"}
```

If the endpoint output already starts with `https://`, use it as it is.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

2. The image stays in the CDK bootstrap ECR repository (`cdk-hnb659fds-container-assets-ACCOUNT-REGION`). Delete it from the Amazon ECR console if you don't need it.

## Documentation and useful references
- [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html)
- [AWS::ECS::ExpressGatewayService](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-expressgatewayservice.html)
- [CfnExpressGatewayService in aws-cdk-lib](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.CfnExpressGatewayService.html)
- [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html)
