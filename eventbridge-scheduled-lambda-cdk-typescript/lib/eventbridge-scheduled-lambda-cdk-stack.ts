import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import { Rule, Schedule } from "@aws-cdk/aws-events";
import {LambdaFunction} from "@aws-cdk/aws-events-targets";
import * as path from 'path';

export class EventbridgeScheduledLambdaCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // get interval in minutes from context (cdk deploy --context interval_in_minutes=<value>)
    const interval_in_minutes = this.node.tryGetContext('interval_in_minutes');

    // check if user enter --context value, if not application will terminate
    if (typeof interval_in_minutes === 'undefined') {
      console.log('example: cdk deploy --context internal_in_minutes=5')
      process.exit(1)
    }
    
    console.log("interval_in_minutes")
    console.log(interval_in_minutes)

    // The code that defines your stack goes here

    //Lambda function to run the scheduled task
    const myFunction = new lambda.Function(this, 'function-name', {
      runtime: lambda.Runtime.NODEJS_14_X,
      memorySize: 128,
      timeout: cdk.Duration.seconds(30),
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '/../src')),
      // create environment variable with the interval assigned with --context
      environment: {
        interval_in_minutes: interval_in_minutes
      },
    });

    //EventBridge rule that runs every <interval_in_minutes> minutes
    const cronRule = new Rule(this, 'CronRule', {
      schedule: Schedule.expression('cron(0/'+ interval_in_minutes +' * * * ? *)')
    })
    //Set Lambda function as target for EventBridge
    cronRule.addTarget(new LambdaFunction(myFunction))

    // end of the code
  }
}
