import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import { LogLevel } from 'aws-cdk-lib/aws-stepfunctions';
import * as path from 'path';
import { EventBridgeConnectionNestedStack } from './eventbridge-connection-nestedstack';
import { CfnOutput } from "aws-cdk-lib";

export interface StateMachineStackProps extends cdk.StackProps {
  vpcId: string;
  onPremiseCidr: string;
  apiDomainName: string;
  apiKeySecretArn: string
}

export class StateMachineStack extends cdk.Stack {
  public readonly stateMachine: sfn.StateMachine;

  constructor(scope: cdk.App, id: string, props: StateMachineStackProps) {
    super(scope, id, props);

    // Create the EventBridge Connection Nested Stack
    const connectionStack = new EventBridgeConnectionNestedStack(this, 'EventBridgeConnectionStack', {
      vpcId: props.vpcId,
      onPremiseCidr: props.onPremiseCidr,
      apiDomainName: props.apiDomainName,
      apiKeySecretArn: props.apiKeySecretArn
    });

    const stateMachineRole = new iam.Role(this, 'StateMachineRole', {
      assumedBy: new iam.ServicePrincipal('states.amazonaws.com'),
      inlinePolicies: {
        'invokeHTTP' : iam.PolicyDocument.fromJson({
          Version: "2012-10-17",
          Statement: [
            {
              Sid: 'invokeHTTP',
              Effect: 'Allow',
              Action: 'states:InvokeHTTPEndpoint',
              Resource: '*',
              Condition: {
                StringLike: {
                  'states:HTTPEndpoint': `https://${props.apiDomainName}/*`
                }
              }
            },
            {
              Sid: 'retrieveEBConnection',
              Effect: 'Allow',
              Action: 'events:RetrieveConnectionCredentials',
              Resource: connectionStack.connection.attrArn
            },
            {
              Sid: 'retrieveEBSecretForConnection',
              Effect: 'Allow',
              Action: [
                'secretsmanager:GetSecretValue',
                'secretsmanager:DescribeSecret'
              ],
              Resource: connectionStack.connection.attrSecretArn
            }
          ]
        })
      }
    });

    // Create the Step Functions state machine
    this.stateMachine = new sfn.StateMachine(this, 'StateMachine', {
      definitionBody: sfn.ChainDefinitionBody.fromFile(path.join(__dirname, 'state-machine.asl.json')),
      definitionSubstitutions: {
        'EventBridgeConnectionArn': connectionStack.connection.attrArn,
        'GetHelloEndpoint': `https://${props.apiDomainName}/hello`
      },
      role: stateMachineRole,
      queryLanguage: sfn.QueryLanguage.JSONATA,
      stateMachineType: sfn.StateMachineType.EXPRESS,
      tracingEnabled: true,
      logs: {
        level: LogLevel.ALL,
        destination: new logs.LogGroup(this, 'StateMachineLogGroup', {retention: RetentionDays.ONE_MONTH})
      }
    });

    new CfnOutput(this, 'ConnectionArn', {
      key: 'ConnectionArn',
      value: connectionStack.connection.attrArn
    });
    new CfnOutput(this, 'StateMachineArn', {
      key: 'StateMachineArn',
      value: this.stateMachine.stateMachineArn
    });
  }
}
