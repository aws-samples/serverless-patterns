/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Effect, Role, ServicePrincipal, Policy, PolicyDocument, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { CfnTopicRule } from 'aws-cdk-lib/aws-iot'
import { CfnDatabase, CfnTable } from 'aws-cdk-lib/aws-timestream'
import { Timestream } from './timestream';
import * as Config from '../config.json';

export class IotTimestreamStack extends Stack {

  timestreamResources : Timestream

  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const stack = Stack.of(this)

    // Invoke nested stack to create the Timestream Database and Table
    this.timestreamResources = new Timestream(this, 'timestreamRsrcs')
    const { tstrm_database, tstrm_table } = this.timestreamResources

    const iotTimestreamRuleRole = new Role(this, 'tstrmActionIoTRuleRole', {
      assumedBy: new ServicePrincipal('iot.amazonaws.com'),
    });

    iotTimestreamRuleRole.addToPolicy(new PolicyStatement({
      effect: Effect.ALLOW,
      resources: [
        "*"
      ],
      actions: [
        'timestream:DescribeEndpoints'
      ]
    }));

    iotTimestreamRuleRole.addToPolicy(new PolicyStatement({
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:timestream:${stack.region}:${stack.account}:database/${Config.timestream.databaseName}/table/${Config.timestream.tableName}`
      ],
      actions: [
        'timestream:WriteRecords'
      ]
    }));

    const iotTimestreamRule = new CfnTopicRule(this, 'iotTimestreamRule', {
      topicRulePayload: {
        awsIotSqlVersion: Config.sql.version,
        sql: Config.sql.statement,
        ruleDisabled: false,
        actions: [
          {
            timestream: {
              databaseName: Config.timestream.databaseName,
              tableName: Config.timestream.tableName,
              dimensions: [
                {
                  name: 'deviceId',
                  value: '${deviceId}'
                }
              ],
              timestamp: {
                unit: 'MILLISECONDS',
                value: '${timestamp}'
              },
              roleArn: iotTimestreamRuleRole.roleArn
            }
          }
        ]
      }
    });
  }
}
