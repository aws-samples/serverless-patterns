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
import {CfnParameter, CustomResource, Duration} from "@aws-cdk/core";
import {VpcStack} from "./vpc-stack";
import {KafkaStack} from "./kafka-stack";
import {NodejsFunction} from "@aws-cdk/aws-lambda-nodejs";
import {Runtime} from "@aws-cdk/aws-lambda";
import {Effect, PolicyStatement} from "@aws-cdk/aws-iam";
import {Provider} from "@aws-cdk/custom-resources";
import {RetentionDays} from "@aws-cdk/aws-logs";

export class KafkaTopicStack extends cdk.Stack {

    constructor(vpcStack: VpcStack, kafkaStack: KafkaStack, scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const bootstrapAddress = new CfnParameter(this, "bootstrapAddress", {
            type: "String",
            description: "Bootstrap address for Kafka broker. Corresponds to bootstrap.servers Kafka consumer configuration",
        }).valueAsString;

        let topicName = new CfnParameter(this, "topicName", {
            type: "String",
            description: "Name of the Kafka topic to be created",
        }).valueAsString;

        // Lambda function to support cloudformation custom resource to create kafka topics.
        const kafkaTopicHandler = new NodejsFunction(this, "KafkaTopicHandler", {
            runtime: Runtime.NODEJS_14_X,
            entry: 'lambda/kafka-topic-handler.ts',
            handler: 'handler',
            vpc: vpcStack.vpc,
            securityGroups: [vpcStack.lambdaSecurityGroup],
            functionName: 'KafkaTopicHandler',
            timeout: Duration.minutes(5),
            environment: {
                'BOOTSTRAP_ADDRESS': bootstrapAddress
            }
        });
        
        kafkaTopicHandler.addToRolePolicy(new PolicyStatement({
            effect: Effect.ALLOW,
            actions: ['kafka:*'],
            resources: [kafkaStack.kafkaCluster.ref]
        }));

        const kafkaTopicHandlerProvider = new Provider(this, 'KafkaTopicHandlerProvider', {
            onEventHandler: kafkaTopicHandler,
            logRetention: RetentionDays.TWO_WEEKS
        });

        const kafkaTopicResource = new CustomResource(this, 'KafkaTopicResource', {
            serviceToken: kafkaTopicHandlerProvider.serviceToken,
            properties: {
                topicConfig: {
                    topic: topicName,
                    numPartitions: 1,
                    replicationFactor: 2
                }
            }
        });
        
    }
}