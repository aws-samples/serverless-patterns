import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Effect, Role, ServicePrincipal, Policy, PolicyDocument, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { CfnTopicRule } from 'aws-cdk-lib/aws-iot'
import { Table } from 'aws-cdk-lib/aws-dynamodb';
import { DynamoDB } from './dynamodb';
import * as Config from '../config.json'

export class IotDdbv2Stack extends Stack {

  dynamoDb : DynamoDB
  
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const stack = Stack.of(this)

    // Invoke the nested stack to create the DynamoDB table
    this.dynamoDb = new DynamoDB(this, 'iotDDBv2Table')
    const { iotDDB } = this.dynamoDb

    const ItemTTL = Config.dynamodb.ttlTimeVaue

    const sqlStatement = `SELECT *, (timestamp() + ${ItemTTL}) as ttl FROM 'dt/#'`

    const iotDDBv2RuleRole = new Role(this, 'iotDDBv2RuleRole', {
      assumedBy: new ServicePrincipal('iot.amazonaws.com')
    })

    iotDDBv2RuleRole.applyRemovalPolicy(RemovalPolicy.DESTROY)

    iotDDBv2RuleRole.addToPolicy(new PolicyStatement({
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:iot:${stack.region}:${stack.account}:*`
      ],
      actions: [
        'iot:Publish'
      ]
    }))

    iotDDB.grantWriteData(iotDDBv2RuleRole)

    const iotDDBV2Rule = new CfnTopicRule(this, 'iotDDBv2Rule', {
        topicRulePayload: {
          ruleDisabled: false,
          awsIotSqlVersion: '2016-03-23',
          sql: sqlStatement,
          actions: [
              { 
                republish: {
                  topic: "ttlupdate",
                  roleArn: iotDDBv2RuleRole.roleArn
                }
              },
              {
                  dynamoDBv2: {
                      putItem: {
                          tableName: iotDDB.tableName
                      },
                      roleArn: iotDDBv2RuleRole.roleArn
                  }
              }
          ]
        },
      });
      iotDDBV2Rule.applyRemovalPolicy(RemovalPolicy.DESTROY)
  }
}
