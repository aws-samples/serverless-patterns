import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as nodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as cdk from "aws-cdk-lib/core";
import { Construct } from "constructs";
import path from "path";

export class LambdaDurableFunctionChainingCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const productCatalogTable = new dynamodb.Table(this, "ProductCatalogTable", {
      partitionKey: {
        name: "productId",
        type: dynamodb.AttributeType.STRING,
      },
    });

    const validateOrderFunction = new nodejs.NodejsFunction(this, "ValidateOrderFunction", {
      runtime: lambda.Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "functions", "validateOrder", "index.ts"),
      durableConfig: {
        executionTimeout: cdk.Duration.hours(1),
        retentionPeriod: cdk.Duration.days(7),
      },
    });

    const authorizePaymentFunction = new nodejs.NodejsFunction(this, "AuthorizePaymentFunction", {
      runtime: lambda.Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "functions", "authorizePayment", "index.ts"),
      environment: {
        PRODUCT_CATALOG_TABLE: productCatalogTable.tableName,
      },
      timeout: cdk.Duration.seconds(30),
    });

    validateOrderFunction.addEnvironment("AUTHORIZE_PAYMENT_FUNCTION", authorizePaymentFunction.functionName);
    authorizePaymentFunction.grantInvoke(validateOrderFunction);
    productCatalogTable.grantReadData(authorizePaymentFunction);

    const allocateInventoryFunction = new nodejs.NodejsFunction(this, "AllocateInventoryFunction", {
      runtime: lambda.Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "functions", "allocateInventory", "index.ts"),
      environment: {
        PRODUCT_CATALOG_TABLE: productCatalogTable.tableName,
      },
      timeout: cdk.Duration.seconds(30),
    });

    validateOrderFunction.addEnvironment("ALLOCATE_INVENTORY_FUNCTION", allocateInventoryFunction.functionName);
    allocateInventoryFunction.grantInvoke(validateOrderFunction);

    const fulfillOrderFunction = new nodejs.NodejsFunction(this, "FulfillOrderFunction", {
      runtime: lambda.Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "functions", "fulfillOrder", "index.ts"),
      timeout: cdk.Duration.seconds(30),
    });

    validateOrderFunction.addEnvironment("FULFILL_ORDER_FUNCTION", fulfillOrderFunction.functionName);
    fulfillOrderFunction.grantInvoke(validateOrderFunction);

    productCatalogTable.grantReadWriteData(allocateInventoryFunction);

    // Outputs
    new cdk.CfnOutput(this, "ProductCatalogTableName", {
      value: productCatalogTable.tableName,
    });

    new cdk.CfnOutput(this, "ValidateOrderFunctionName", {
      value: validateOrderFunction.functionName,
    })
  }
}
