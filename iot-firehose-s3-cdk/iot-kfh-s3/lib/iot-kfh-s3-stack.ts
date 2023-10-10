/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { S3Buckets } from './s3buckets';
import { LogStream, LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs'
import { Effect, Role, ServicePrincipal, Policy, PolicyDocument, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { CfnDeliveryStream } from 'aws-cdk-lib/aws-kinesisfirehose'
import { CfnTopicRule } from 'aws-cdk-lib/aws-iot'

export class IotKfhS3Stack extends Stack {
  s3buckets: S3Buckets

  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const stack = Stack.of(this)
    const iotArnPrefix = `arn:aws:iot:${stack.region}:${stack.account}`

    // Create the S3 Bucket to be used as a Firehose destination 
    // in a nested stack. If you have a pre-existing bucket, you
    // can modify the nested stack to lookup and return the bucket.
    this.s3buckets = new S3Buckets(this, 's3-bucket')
    const { kfh_bucket } = this.s3buckets


    // Create a log group
    const logGroup = new LogGroup(this, 'kfh-log-group', {
      logGroupName: 'iot-kfh-s3-logs',
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.FIVE_DAYS,
    })

    // Create the Kinesis Firehose log stream.
    const firehoseLogStream = new LogStream(this, 'iot-kfh-s3-stream', {
        logGroup: logGroup,
        logStreamName: 'iot-kfh-s3-logstream',
        removalPolicy: RemovalPolicy.DESTROY,
    }) 

    // IAM Role for Kinesis Firehose
    const kfhDeliveryStreamRole = new Role(this,'KFHRawDeliveryStreamRole', {
        roleName: 'iot-kfh-s3-delivery-' + stack.region,
        assumedBy: new ServicePrincipal('firehose.amazonaws.com'),
        inlinePolicies: {
            cloudwatch: new PolicyDocument({
                statements: [
                    new PolicyStatement({
                        actions: ['logs:PutLogEvents'],
                        effect: Effect.ALLOW,
                        resources: [
                            logGroup.logGroupArn +
                                ':log-stream:' +
                                firehoseLogStream.logStreamName,
                        ],
                    }),
                ],
            }),
        },
        }
    )

    // Grant permissions to role for putting objects in S3
    kfh_bucket.grantPut(kfhDeliveryStreamRole)
    kfh_bucket.grantWrite(kfhDeliveryStreamRole)

    // Create a Kinesis Firehose data stream with dynamic partitioning
    // The messages should have the following fields - `deviceId` that
    // uniquely defined the IoT device sending data. For example this 
    // could be the MAC Address of the device.
    // Metadata extracted is from the field `timestamp` to give the following
    // folder structure"
    // S3Bucket/deviceId/year/month/day/hour

    const kfhDeliveryStream = new CfnDeliveryStream(this,'KFHDeliveryStream', {
          deliveryStreamName: 'iot-kfh-s3-DeliveryStream',
          deliveryStreamType: 'DirectPut',
          extendedS3DestinationConfiguration: {
              bucketArn: kfh_bucket.bucketArn as string,
              roleArn: kfhDeliveryStreamRole.roleArn,
              prefix: `!{partitionKeyFromQuery:deviceId}/!{partitionKeyFromQuery:year}/!{partitionKeyFromQuery:month}/!{partitionKeyFromQuery:day}/!{partitionKeyFromQuery:hour}/`,
              errorOutputPrefix: 'errors/!{firehose:error-output-type}',
              bufferingHints: {
                  // sizeInMBs: 1,
                  intervalInSeconds: 120,
              },
              dynamicPartitioningConfiguration: {
                  enabled: true,
              },
              processingConfiguration: {
                  enabled: true,
                  processors: [
                      {
                          type: 'MetadataExtraction',
                          parameters: [
                              {
                                  parameterName:'MetadataExtractionQuery',
                                  parameterValue: '{deviceId: .deviceId, year: .timestamp | strftime(\"%Y"\), month: .timestamp | strftime(\"%m"\), day: .timestamp | strftime(\"%d"\), hour: .timestamp | strftime(\"%H"\)}',
                              },
                              {
                                  parameterName: 'JsonParsingEngine',
                                  parameterValue: 'JQ-1.6',
                              },
                          ],
                      },

                      {
                          type: 'AppendDelimiterToRecord',
                          parameters: [
                              {
                                  parameterName: 'Delimiter',
                                  parameterValue: '\\n',
                              },
                          ],
                      },
                  ],
              },
              compressionFormat: 'UNCOMPRESSED',
              encryptionConfiguration: {
                  noEncryptionConfig: 'NoEncryption',
              },
              cloudWatchLoggingOptions: {
                  logGroupName: logGroup.logGroupName,
                  logStreamName: firehoseLogStream.logStreamName,
              },
          },
      }
    )

    const kfhActionIotRuleRole = new Role(this, 'kfhActionIoTRuleRole', {
      assumedBy: new ServicePrincipal('iot.amazonaws.com'),
    })

    const kfhIotActionsPolicy = new Policy(this, 'kfhIotActionsPolicy', {
          statements: [
              new PolicyStatement({
                  actions: ['firehose:PutRecord'],
                  resources: [kfhDeliveryStream.attrArn],
              }),
          ],
    })

    kfhIotActionsPolicy.attachToRole(kfhActionIotRuleRole)
    kfh_bucket.grantWrite(kfhActionIotRuleRole)

    const kfhDataStreamIotRule = new CfnTopicRule(this,'kfhDataStreamIotRule',{
        topicRulePayload: {
            ruleDisabled: false,
            awsIotSqlVersion: '2016-03-23',
            sql: "SELECT * FROM '#'",
            actions: [
              {
                  firehose: {
                      deliveryStreamName:'iot-kfh-s3-DeliveryStream',
                      roleArn: kfhActionIotRuleRole.roleArn,
                  }

              }
            ],
            errorAction: {
                s3: {
                    bucketName: kfh_bucket.bucketName as string,
                    key:
                        `errors/iot-rules/kfhDataStreamIotRule/` +
                        '${parse_time("yyyy/MM/dd", timestamp(), "UTC")}/' +
                        '${parse_time("yyyy-MM-dd.HH-mm-ss", timestamp(), "UTC")}.${newuuid()}.json',
                    roleArn: kfhActionIotRuleRole.roleArn,
                },
            },
        },
    })
  }
}
