/*
 * Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 * SPDX-License-Identifier: MIT-0
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this
 * software and associated documentation files (the "Software"), to deal in the Software
 * without restriction, including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
import * as cdk from "@aws-cdk/core";
import {CfnParameter, Duration} from "@aws-cdk/core";
import {VpcStack} from "./vpc-stack";
import {NodejsFunction} from "@aws-cdk/aws-lambda-nodejs";
import {Effect, PolicyStatement} from "@aws-cdk/aws-iam";
import {KafkaStack} from "./kafka-stack";
import {KafkaTopicStack} from "./kafka-topic-stack";
import {Runtime, StartingPosition} from "@aws-cdk/aws-lambda"
import { ManagedKafkaEventSource } from "@aws-cdk/aws-lambda-event-sources";
import * as iam from '@aws-cdk/aws-iam';

export class LambdaStack extends cdk.Stack {
    constructor(vpcStack: VpcStack, scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const topicName = new CfnParameter(this, "topicName", {
            type: "String",
            description: "Kafka topic name",
        }).valueAsString;

        const kafkaClusterArn = new CfnParameter(this, "kafkaArn", {
          type: "String",
          description: "Kafka cluster ARN",
        }).valueAsString;

        let transactionHandler = new NodejsFunction(this, "TransactionHandler", {
            runtime: Runtime.NODEJS_14_X,
            entry: 'lambda/transaction-handler.js',
            handler: 'handler',
            vpc: vpcStack.vpc,
            securityGroups: [vpcStack.lambdaSecurityGroup],
            functionName: 'TransactionHandler',
            timeout: Duration.minutes(5),
        });

        // transactionHandler.addToRolePolicy(new PolicyStatement({
        //     effect: Effect.ALLOW,
        //     actions: ['kafka-cluster:*'],
        //     resources: ['*']
        // }));

      // Allow lambda to interact with MSK
        transactionHandler.role?.addManagedPolicy(
          iam.ManagedPolicy.fromAwsManagedPolicyName(
            'service-role/AWSLambdaMSKExecutionRole',
          ),
        );
      // // Event Source Mapping MSK -> Lambda
      // const s3PutEventSource = new ManagedKafkaEventSource(bucket, {
      //   events: [
      //     s3.EventType.OBJECT_CREATED_PUT
      //   ]
      // });

      // lambdaReadStream.addEventSource(s3PutEventSource);
      
      // Add MSK as event source to lambda
        transactionHandler.addEventSource(new ManagedKafkaEventSource({
          clusterArn: kafkaClusterArn,
          topic: 'transactions',
          batchSize: 100, // default
          startingPosition: StartingPosition.LATEST
        }));
    }
}