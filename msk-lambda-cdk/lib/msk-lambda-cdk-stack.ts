/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
import { Stack, StackProps, Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_iam as iam } from 'aws-cdk-lib';
import { aws_lambda as lambda } from 'aws-cdk-lib';
import * as msk from '@aws-cdk/aws-msk-alpha';
import { aws_ec2 as ec2 } from 'aws-cdk-lib';
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { ManagedKafkaEventSource } from "aws-cdk-lib/aws-lambda-event-sources";

import path = require('path');





export class MskLambdaCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    let topicName: string;
    topicName = "transactions";

    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2
    });

    const cluster = new msk.Cluster(this, "Cluster", {
      clusterName: 'myclusterviasimplecdk',
      kafkaVersion: msk.KafkaVersion.V2_8_1,
      vpc: vpc,
      ebsStorageInfo: {
        volumeSize: 50,
      },
    })


    let transactionHandler = new NodejsFunction(this, "TransactionHandler", {
      runtime: Runtime.NODEJS_14_X,
      entry: 'lambda/transaction-handler.js',
      handler: 'handler',
      vpc: vpc,
      functionName: 'TransactionHandler',
      timeout: Duration.minutes(1),
    });

    
    // Allow lambda to interact with MSK
    transactionHandler.role?.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        'service-role/AWSLambdaMSKExecutionRole',
      ),
    );

    transactionHandler.addEventSource(new ManagedKafkaEventSource({
      clusterArn: cluster.clusterArn,
      topic: topicName,
      batchSize: 100, // default
      startingPosition: lambda.StartingPosition.LATEST
    }));

    // It was found that MSK needs to allow inbound traffic from anywhere on all ports.
        cluster.connections.allowFromAnyIpv4(ec2.Port.allTraffic(), "allow all from anywhere");

  }
}
