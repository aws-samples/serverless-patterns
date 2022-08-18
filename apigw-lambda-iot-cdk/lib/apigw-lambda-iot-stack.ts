/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import {Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam'
import { LambdaRestApi } from 'aws-cdk-lib/aws-apigateway';

export class ApigwLambdaIotStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const stack = Stack.of(this);
    const iotArnPrefix = `arn:aws:iot:${stack.region}:${stack.account}`


    const iotPublishHandler = new Function(this, 'iotPublishHandler', {
      handler: 'handler.handler',
      code: Code.fromAsset('./src'),
      description: 'This function publishes a message to AWS IoT Core',
      runtime: Runtime.PYTHON_3_9,
    })

    const iotPublishHandlerPersmission = new PolicyStatement(({
      effect: Effect.ALLOW,
      resources: [
        "*"
      ],
      actions: [
        "iot:Connect",
        "iot:Publish"
      ]
    }));

    iotPublishHandler.role?.addToPrincipalPolicy(iotPublishHandlerPersmission);

    const iotApi = new LambdaRestApi(this, 'iotPublishApi', {
      handler: iotPublishHandler,
      proxy: false
    });
    const cmds = iotApi.root.addResource('cmds');
    cmds.addMethod('POST');

  }
}
