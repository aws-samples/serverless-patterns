import { Duration, RemovalPolicy, Stack, StackProps } from "aws-cdk-lib";
import { Rule } from "aws-cdk-lib/aws-events";
import { LambdaFunction } from "aws-cdk-lib/aws-events-targets";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { LogGroup, RetentionDays } from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";
import * as path from "path";

export class EventBridgeLambdaStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

     // Lambda function
    const lambdaFn = new NodejsFunction(this, 'lambdaPutDynamoDBHandler', {
      runtime: Runtime. NODEJS_20_X,
      memorySize: 1024,
      timeout: Duration.seconds(3),
      entry: path.join(__dirname, '../src/app.ts'),
      handler: 'main',
    });


    // Set Lambda Logs Retention and Removal Policy
    new LogGroup(this, 'logs', {
      logGroupName: `/aws/lambda/${lambdaFn.functionName}`,
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.ONE_DAY,
    });

    // EventBridge Rule
    const rule = new Rule(this, 'Rule');
    rule.addEventPattern({
      source: ['cdk.myApp'],
      detailType: ['transaction'],
    });
    rule.addTarget(new LambdaFunction(lambdaFn));


  }
}
