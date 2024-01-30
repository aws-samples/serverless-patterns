/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import * as cdk from "aws-cdk-lib";
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as kms from "aws-cdk-lib/aws-kms";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambda_event_source from "aws-cdk-lib/aws-lambda-event-sources";
import * as sqs from "aws-cdk-lib/aws-sqs";
import { Construct } from "constructs";
import { TABLE_CONFIG } from "./config/tables.config";
import { CfnOutput } from "aws-cdk-lib";

export interface TableConfig {
  readonly name: string,
  readonly writeCapacity: number,
  readonly sqsMaxConcurrency: number,
  readonly retryAttempts: number,
  readonly lambdaRetryAttempts: number,
}

export class SqsLambdaDynamoStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // constants used for table/lambda creation
    const TABLE_PROPS = TABLE_CONFIG;

    // for each desired table
    TABLE_PROPS.map((table) => {
      // create dynamodb table
      const ddbTable = new dynamodb.Table(this, table.name, {
        partitionKey: {
          name: "id",
          type: dynamodb.AttributeType.STRING,
        },
        encryption: dynamodb.TableEncryption.AWS_MANAGED,
        writeCapacity: table.writeCapacity,
        removalPolicy: cdk.RemovalPolicy.DESTROY // destroy table on stack delete
      });

      // create DLQ
      const dlq = new sqs.Queue(
        this,
        `${table.name}-DLQ`,
        {
          encryption: sqs.QueueEncryption.SQS_MANAGED
        }
      )

      // create SQS queue
      const sqsQueue = new sqs.Queue(
        this,
        `${table.name}-Queue`,
        {
          deadLetterQueue: {
            maxReceiveCount: table.retryAttempts,
            queue: dlq,
          },
          encryption: sqs.QueueEncryption.SQS_MANAGED,
        }
      );


      // create Lambda environment variable encryption key
      const lambdaEnvKey = new kms.Key(this, `${table.name}-LambdaEnvKey`, {
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      });

      // create Lambda function
      const lambdaFunction = new lambda.Function(
        this,
        `${table.name}-Lambda`,
        {
          runtime: lambda.Runtime.NODEJS_18_X,
          code: lambda.Code.fromAsset("lib/lambda"),
          handler: "index.handler",
          environment: {
            DESTINATION_TABLE_NAME: ddbTable.tableName, // need the actual generated name of the table
          },
          environmentEncryption: lambdaEnvKey,
          retryAttempts: table.lambdaRetryAttempts,
        }
      );

      // grant Lambda access to decrypt using kms key
      lambdaEnvKey.grantDecrypt(lambdaFunction);

      // granting Lambda permissions to write to dynamodb table
      ddbTable.grantWriteData(lambdaFunction);

      // setting up the SQS as a trigger for Lambda
      lambdaFunction.addEventSource(
        new lambda_event_source.SqsEventSource(sqsQueue, {
          batchSize: 1,
          maxConcurrency: table.sqsMaxConcurrency,
        })
      );

      // print the SQS Queue URL for use with testing script
      new CfnOutput(this, `${table.name}-Queue-URL`, { value: sqsQueue.queueUrl });
    });
  }
}
