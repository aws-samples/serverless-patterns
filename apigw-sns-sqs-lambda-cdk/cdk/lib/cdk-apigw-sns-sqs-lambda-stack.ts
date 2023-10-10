/*!  Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  *  SPDX-License-Identifier: MIT-0
 */

import { Stack, StackProps, Aws } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_iam as iam } from 'aws-cdk-lib';
import { aws_lambda as lambda } from 'aws-cdk-lib';
import { SqsEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import { aws_sqs as sqs } from 'aws-cdk-lib';
import { aws_sns as sns } from 'aws-cdk-lib';
import { aws_sns_subscriptions as subscriptions } from 'aws-cdk-lib';
import { aws_apigateway as apigateway } from 'aws-cdk-lib';

import * as path from 'path';

export class CdkApigwSnsSqsLambdaStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const topic = new sns.Topic(this, 'topic')

    const subscriberQueueOne = new sqs.Queue(this, 'SubscriberQueueOne');    
    topic.addSubscription(new subscriptions.SqsSubscription(subscriberQueueOne));
    const workerLambdaTypeOne = new lambda.Function(this, 'workerLambdaTypeOneHandler',{
      runtime: lambda.Runtime.NODEJS_14_X,
      handler: 'app.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../src')),
      events: [new SqsEventSource(subscriberQueueOne)]
    });

    const subscriberQueueTwo = new sqs.Queue(this, 'SubscriberQueueTwo');
    topic.addSubscription(new subscriptions.SqsSubscription(subscriberQueueTwo));
    const workerLambdaTypeTwo = new lambda.Function(this, 'workerLambdaTypeTwoHandler',{
      runtime: lambda.Runtime.NODEJS_14_X,
      handler: 'app.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../src')),
      events: [new SqsEventSource(subscriberQueueTwo)]
    });

    const gatewayExecutionRole: any = new iam.Role(this, "GatewayExecutionRole", {
      assumedBy: new iam.ServicePrincipal("apigateway.amazonaws.com"),
      inlinePolicies: {
        "PublishMessagePolicy": new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({
            actions: ["sns:Publish"],
            resources: [topic.topicArn]
          })]
        })
      }
    });

    const api = new apigateway.RestApi(this, 'RestApi');
    api.root.addMethod('POST',
      new apigateway.AwsIntegration({
        service: 'sns',
        integrationHttpMethod: 'POST',
        path: `${Aws.ACCOUNT_ID}/${topic.topicName}`,
        options: {
          credentialsRole: gatewayExecutionRole, 
          passthroughBehavior: apigateway.PassthroughBehavior.NEVER,
          requestParameters: {
            "integration.request.header.Content-Type": `'application/x-www-form-urlencoded'`,
          },
          requestTemplates: {
            "application/json": `Action=Publish&TopicArn=$util.urlEncode('${topic.topicArn}')&Message=$util.urlEncode($input.body)`,
          },
          integrationResponses: [
            {
              statusCode: "200",
              responseTemplates: {
                "application/json": `{"status": "message added to topic"}`,
              },
            },
            {
              statusCode: "400",
              selectionPattern: "^\[Error\].*",
              responseTemplates: {
                "application/json": `{\"state\":\"error\",\"message\":\"$util.escapeJavaScript($input.path('$.errorMessage'))\"}`,
              },
            }
          ],
        }
      }),{ methodResponses: [{ statusCode: "200" }, { statusCode: "400" }] }
    );
  }
}
