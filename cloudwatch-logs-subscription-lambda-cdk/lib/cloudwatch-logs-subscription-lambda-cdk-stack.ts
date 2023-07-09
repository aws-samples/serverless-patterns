import { Stack, StackProps, aws_lambda_nodejs as nodejs_lambda, aws_lambda as lambda, Duration, aws_logs as logs, aws_logs_destinations as destinations, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';

export class CloudwatchLogsSubscriptionLambdaCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const logReceivingLambdaFunction = new nodejs_lambda.NodejsFunction(this, "LogReceivingLambdaFunction", {
      runtime: lambda.Runtime.NODEJS_14_X,
      entry: path.join(__dirname, `/../lambda/index.ts`),
      handler: "handler",
      retryAttempts: 0,
      timeout: Duration.seconds(30),
    });

    const myLogGroup = new logs.LogGroup(this, 'MyLogGroup');

    const myLogStream = new logs.LogStream(this, 'MyLogStream', {
      logGroup: myLogGroup
    });

    const logGroupLambdaSubscription = new logs.SubscriptionFilter(this, 'LogGroupLambdaSubscription', {
      logGroup: myLogGroup,
      destination: new destinations.LambdaDestination(logReceivingLambdaFunction),
      filterPattern: logs.FilterPattern.anyTerm("ERROR", "WARNING"),
    });

    new CfnOutput(this, 'logGroupName', {
      value: myLogGroup.logGroupName,
      description: 'Log group name',
      exportName: 'LogGroupName',
    });

    new CfnOutput(this, 'logStreamName', {
      value: myLogStream.logStreamName,
      description: 'Log stream name',
      exportName: 'LogStreamName',
    });
  }
}
