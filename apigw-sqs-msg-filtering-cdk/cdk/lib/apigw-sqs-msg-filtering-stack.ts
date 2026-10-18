import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { ApiGwSqsConstruct } from './apigw-sqs-msg-filtering';

export class ApigwSqsMsgFilteringCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create custom sqs queue
    const sqsQueue = new cdk.aws_sqs.Queue(this, 'apigwSqs-queue', {
      queueName: 'MyQueueName',
    });

    // Create custom api gateway
    const apiGateway = new cdk.aws_apigateway.RestApi(this, 'apigwSqs-restApi', {
      description: 'APIGW-SQS REST API Gateway',
      restApiName: 'apiGatewayToSqs',
      deployOptions: {
        stageName: 'dev',
      },
      // Enable CORS
      defaultCorsPreflightOptions: {
        allowHeaders: [
          'Content-Type',
          'X-Amz-Date',
          'Authorization',
          'X-Api-Key',
        ],
        allowMethods: ['OPTIONS', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
        allowOrigins: ['*'],
      },
    });

    // https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html
    const vtlMappingTemplate = `
{
  #set($payload = $input.path('$'))
  #set($messageBody = $input.path('$.messageBody'))
  #if($messageBody.notNeededElement)
  #set($partToRemove = $messageBody.remove("notNeededElement"))
  #end
  #set($payload.filteredMessageBody = $messageBody)
  "MessageBody": "$util.escapeJavaScript($input.json('$.filteredMessageBody'))",
  #if($payload.delaySeconds > 0)
  "DelaySeconds": $payload.delaySeconds,
  #end
  #if($payload.messageAttributes && $payload.messageAttributes.size() > 0)
  "MessageAttributes": {
    #foreach($attrName in $payload.messageAttributes.keySet())
      #set($attr = $payload.messageAttributes.get($attrName))
      "$attrName": {
        "DataType": "$attr.dataType",
        #if($attr.dataType == "String" || $attr.dataType.startsWith("String."))
        "StringValue": "$attr.stringValue"
        #elseif($attr.dataType == "Binary" || $attr.dataType.startsWith("Binary."))
        "BinaryValue": "$attr.binaryValue"
        #else
        "StringValue": "$attr.stringValue"
        #end
      }#if($foreach.hasNext),#end
    #end
  },
  #end
  "QueueUrl": "${sqsQueue.queueUrl}"
}
`;

    new ApiGwSqsConstruct(this, 'apiGwSqs', {
      apiGateway: apiGateway,
      sqsQueue: sqsQueue,
      vtlMappingTemplate: vtlMappingTemplate,
    });

    new cdk.CfnOutput(this, 'ApiGatewayName', { value: apiGateway.restApiName });
    new cdk.CfnOutput(this, 'ApiGatewayUrl', { value: apiGateway.url });
    new cdk.CfnOutput(this, 'ApiGatewaySqsResourceEndpoint', { value: `${apiGateway.url}sqs` });
    new cdk.CfnOutput(this, 'SqsQueueName', { value: sqsQueue.queueName });
    new cdk.CfnOutput(this, 'SqsQueueUrl', { value: sqsQueue.queueUrl });
  }
}
