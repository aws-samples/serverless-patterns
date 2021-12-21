/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import * as lambda from '@aws-cdk/aws-lambda';
import * as msk from "@aws-cdk/aws-msk"
import {NodejsFunction} from "@aws-cdk/aws-lambda-nodejs";
import {Runtime} from "@aws-cdk/aws-lambda";

import * as ec2 from '@aws-cdk/aws-ec2';

import { ManagedKafkaEventSource } from "@aws-cdk/aws-lambda-event-sources";

import path = require('path');

import * as iam from '@aws-cdk/aws-iam';

import * as cdk from '@aws-cdk/core';

export class MskLambdaCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
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
      timeout: cdk.Duration.minutes(1),
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
