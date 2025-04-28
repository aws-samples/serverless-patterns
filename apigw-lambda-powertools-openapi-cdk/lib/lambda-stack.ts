// lib/lambda-stack.ts
import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambdaNodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as secretsmanager from "aws-cdk-lib/aws-secretsmanager";
import { Construct } from "constructs";

export interface LambdaStackProps extends cdk.NestedStackProps {
  stageName: string;
  apiKey: secretsmanager.Secret;
  table: dynamodb.TableV2;
}

export class LambdaStack extends cdk.NestedStack {
  public readonly crudLambda: lambda.Function;
  public readonly searchLambda: lambda.Function;

  constructor(scope: Construct, id: string, props: LambdaStackProps) {
    super(scope, id, props);

    const powertoolsLayer = lambda.LayerVersion.fromLayerVersionArn(
      this,
      "powertools-layer",
      `arn:aws:lambda:${
        cdk.Stack.of(this).region
      }:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:3`
    );

    this.crudLambda = new lambdaNodejs.NodejsFunction(this, "crudLambda", {
      runtime: lambda.Runtime.NODEJS_22_X,
      functionName: "orderCRUD",
      handler: "handler",
      entry: "lib/lambda/ordersCRUD/index.ts",
      environment: {
        POWERTOOLS_SERVICE_NAME: "ordersCRUD",
        POWERTOOLS_LOG_LEVEL: "INFO",
        POWERTOOLS_METRICS_NAMESPACE: "OrderService",
        POWERTOOLS_METRICS_FUNCTION_NAME: "handle",
        POWERTOOLS_TRACE_ENABLED: "true",
        POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS: "true",
        POWERTOOLS_TRACER_CAPTURE_RESPONSE: "true",
        POWERTOOLS_TRACER_CAPTURE_ERROR: "true",
        POWERTOOLS_DEV: String(props.stageName === "dev"),
        POWERTOOLS_LOGGER_LOG_EVENT: String(props.stageName === "dev"),
        STAGE: props.stageName,
        API_KEY_SECRET_ARN: props.apiKey.secretArn,
        DYNAMODB_TABLE_NAME: props.table.tableName,
      },
      tracing: lambda.Tracing.ACTIVE,
      layers: [powertoolsLayer],
      timeout: cdk.Duration.seconds(5),
    });

    props.apiKey.grantRead(this.crudLambda);
    props.table.grantReadWriteData(this.crudLambda);

    this.searchLambda = new lambdaNodejs.NodejsFunction(this, "searchLambda", {
      runtime: lambda.Runtime.NODEJS_22_X,
      functionName: "orderSearch",
      handler: "handler",
      entry: "lib/lambda/ordersSearch/index.ts",
      environment: {
        POWERTOOLS_SERVICE_NAME: "ordersSearch",
        POWERTOOLS_LOG_LEVEL: "INFO",
        POWERTOOLS_METRICS_NAMESPACE: "OrderService",
        POWERTOOLS_METRICS_FUNCTION_NAME: "search",
        POWERTOOLS_TRACE_ENABLED: "true",
        POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS: "true",
        POWERTOOLS_TRACER_CAPTURE_RESPONSE: "true",
        POWERTOOLS_TRACER_CAPTURE_ERROR: "true",
        POWERTOOLS_DEV: String(props.stageName === "dev"),
        POWERTOOLS_LOGGER_LOG_EVENT: String(props.stageName === "dev"),
        STAGE: props.stageName,
        DYNAMODB_TABLE_NAME: props.table.tableName,
      },
      tracing: lambda.Tracing.ACTIVE,
      layers: [powertoolsLayer],
      timeout: cdk.Duration.seconds(5),
    });
    props.table.grantReadData(this.searchLambda);
  }
}
