import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as nodejs from "aws-cdk-lib/aws-lambda-nodejs";
import { Construct } from "constructs";

export class LambdaAzAwareRoutingStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB table to record AZ routing decisions
    const table = new dynamodb.Table(this, "AzRoutingTable", {
      partitionKey: { name: "pk", type: dynamodb.AttributeType.STRING },
      sortKey: { name: "sk", type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Lambda function that reads AZ metadata and demonstrates routing
    const routerFn = new nodejs.NodejsFunction(this, "AzRouterFn", {
      entry: "src/az-router/index.ts",
      handler: "handler",
      runtime: lambda.Runtime.NODEJS_22_X,
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      environment: {
        TABLE_NAME: table.tableName,
      },
      bundling: {
        minify: true,
        sourceMap: true,
      },
      description:
        "Reads Lambda AZ metadata and demonstrates same-AZ routing",
    });

    table.grantWriteData(routerFn);

    // Function URL for easy testing
    const fnUrl = routerFn.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.AWS_IAM,
    });

    new cdk.CfnOutput(this, "FunctionName", {
      value: routerFn.functionName,
    });
    new cdk.CfnOutput(this, "FunctionUrl", {
      value: fnUrl.url,
    });
    new cdk.CfnOutput(this, "TableName", {
      value: table.tableName,
    });
  }
}
