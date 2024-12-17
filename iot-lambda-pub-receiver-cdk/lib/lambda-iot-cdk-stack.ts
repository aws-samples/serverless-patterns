import { CloudWatchLogsAction, LambdaFunctionAction } from '@aws-cdk/aws-iot-actions-alpha';
import { IotSql, TopicRule } from '@aws-cdk/aws-iot-alpha';
import { CfnOutput, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Effect, PolicyStatement, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Architecture, Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs';
import { AwsCustomResource, AwsCustomResourcePolicy, PhysicalResourceId } from 'aws-cdk-lib/custom-resources';
import { Construct } from 'constructs';

export class LambdaIotCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    let mqttTopicName = "my/mqtt/topic"
    let mqttTopicRegion = Stack.of(this).region
    let mqttTopicAccount = Stack.of(this).account
    let iotEndpointAddress = this.getIoTEndpoint().getResponseField('endpointAddress')

    // Publisher lambda function. 
    // Remark - if the Lambda is in the same account and region as the IoT Core endpoint, then setting the endpoint is optional.
    const iotPubPermission = new PolicyStatement(({
      effect: Effect.ALLOW,
      resources: [ `arn:aws:iot:${mqttTopicRegion}:${mqttTopicAccount}:topic/${mqttTopicName}` ],
      actions: [ "iot:Publish" ]
    }));
    const iotPubLambda = new Function(this, 'iotPubHandler', {
      handler: 'publisher_function.handler',
      code: Code.fromAsset('./src'),
      description: 'This function publishes a message to AWS IoT Core - MTTQ',
      runtime: Runtime.PYTHON_3_12,
      architecture: Architecture.ARM_64,
      logGroup: this.addLogGroup(`/aws/lambda/pub-lambda`),
      environment: {
        MQTT_TOPIC_REGION: mqttTopicRegion,
        MQTT_TOPIC_NAME: mqttTopicName
      }
    })
    iotPubLambda.addToRolePolicy(iotPubPermission)

    // Receiver lambda function
    const iotReceiverPermission = new PolicyStatement(({
      effect: Effect.ALLOW,
      resources: [ `arn:aws:iot:${mqttTopicRegion}:${mqttTopicAccount}:topic/${mqttTopicName}` ],
      actions: [
        "iot:Receive"
      ]
    }));
    const iotReceiverLambda = new Function(this, 'iotReceiverHandler', {
      handler: 'receiver_function.handler',
      description: 'This function get invoked by AWS IoT Core through the action-rule',
      code: Code.fromAsset('./src', {
        bundling: {
          image: Runtime.PYTHON_3_12.bundlingImage,
          command: [
            'bash', '-c',
            'pip install -r receiver_requirements.txt -t /asset-output && cp -au . /asset-output'
          ],
        },
      }),
      runtime: Runtime.PYTHON_3_12,
      architecture: Architecture.ARM_64,
      logGroup: this.addLogGroup(`/aws/lambda/receiver-lambda`)
    })
    iotReceiverLambda.addToRolePolicy(iotReceiverPermission)

    // Topic rule
    const errorLogGroup = new LogGroup(this, 'RuleErrorLogGroup', {
      logGroupName: '/aws/iot/rule-error-logs',
      retention: RetentionDays.FIVE_DAYS,
      removalPolicy: RemovalPolicy.DESTROY 
    })
    let topicRule = new TopicRule(this, 'IoTTopicRule', {
      topicRuleName: 'ProcessIoTMessages',
      description: 'Invokes the lambda function',
      sql: IotSql.fromStringAsVer20160323("SELECT * FROM 'my/mqtt/topic'"),
      actions: [ new LambdaFunctionAction(iotReceiverLambda) ],
      errorAction: new CloudWatchLogsAction(errorLogGroup)
    })

    // Grant permission for AWS IoT to invoke the Lambda function
    const iotServicePrincipal = new ServicePrincipal('iot.amazonaws.com');
    iotReceiverLambda.grantInvoke(iotServicePrincipal);

    // Outputs
    new CfnOutput(this, "IoT Endpoint Address", {
      value: iotEndpointAddress ?? "Error: can't get the IoT Endpoint Address!",
    });
  }

  // Utility function to return a log-group object
  private addLogGroup(logGroupName: string) {
    const retentionDays = RetentionDays.FIVE_DAYS
    const removalPolicy = RemovalPolicy.DESTROY
    const props = { logGroupName, retentionDays, removalPolicy }
    return new LogGroup(this, `${logGroupName}`, props)
  }

  // Get the current account IoT-Endpoint 
  private getIoTEndpoint() {
    const ioTEndpoint = new AwsCustomResource(this, 'IoTEndpoint', {
      onCreate: {
          service: 'Iot',
          action: 'describeEndpoint',
          physicalResourceId: PhysicalResourceId.fromResponse('endpointAddress'),
          parameters: {
          "endpointType": "iot:Data-ATS"
          }
      },
      policy: AwsCustomResourcePolicy.fromSdkCalls({resources: AwsCustomResourcePolicy.ANY_RESOURCE})
    })
    const IOT_ENDPOINT = ioTEndpoint.getResponseField('endpointAddress')
    return ioTEndpoint
  }
}
