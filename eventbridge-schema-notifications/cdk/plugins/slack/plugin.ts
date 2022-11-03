import * as path from 'path';
import { Construct } from 'constructs';

import { Rule } from 'aws-cdk-lib/aws-events';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

import { aws_events_targets, CfnOutput, Duration } from 'aws-cdk-lib';
import { aws_lambda as lambda, Stack } from 'aws-cdk-lib';
import { PolicyStatement, Effect } from 'aws-cdk-lib/aws-iam';

interface PluginConfig {
  readonly rule: Rule;
}

export interface SlackNofiferProps {
  readonly API_KEY?: string;
  readonly CHANNEL_ID?: string;
}

export class SlackNotifier {
  constructor(config: SlackNofiferProps) {
    return class extends Construct {
      constructor(scope: Construct, id: string, pluginConfig: PluginConfig) {
        super(scope, id);

        const region = Stack.of(this).region;
        const account = Stack.of(this).account;

        if(!config.API_KEY || !config.CHANNEL_ID){
          throw new Error('Missing SLACK credentials')
        }

        // Example producer of an event using the enrichment metadata pattern.
        const slackNotificationFunction: NodejsFunction = new NodejsFunction(this, 'slackNotification', {
          memorySize: 1024,
          timeout: Duration.seconds(5),
          runtime: lambda.Runtime.NODEJS_16_X,
          handler: 'handler',
          entry: path.join(__dirname, './notify-slack-lambda.ts'),
          environment: {
            SLACK_API_KEY: config.API_KEY,
            CHANNEL_ID: config.CHANNEL_ID,
          },
        });

        // allow our slack notification function to get schemas from our event bus
        slackNotificationFunction.addToRolePolicy(
          new PolicyStatement({
            effect: Effect.ALLOW,
            actions: ['schemas:DescribeSchema'],
            // resources: ['*'],
            resources: [`arn:aws:schemas:${region}:${account}:schema/*`],
          })
        );

        pluginConfig.rule.addTarget(new aws_events_targets.LambdaFunction(slackNotificationFunction));

        new CfnOutput(this, 'slackNotificationARN', { value: slackNotificationFunction.functionArn });
      }
    };
  }
}
