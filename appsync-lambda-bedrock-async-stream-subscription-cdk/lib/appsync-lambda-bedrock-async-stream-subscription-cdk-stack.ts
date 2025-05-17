import * as cdk from 'aws-cdk-lib';
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';
import * as path from 'path';

export class AppsyncLambdaBedrockAsyncStreamSubscriptionCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, {
      ...props,
      env: {
        account: process.env.CDK_DEFAULT_ACCOUNT,
        region: process.env.CDK_DEFAULT_REGION,
      },
    });

    const api = new appsync.GraphqlApi(this, 'Api', {
      name: 'bedrock-streaming-api',
      definition: appsync.Definition.fromFile(path.join(__dirname, '..', 'schema.graphql')),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.API_KEY,
        },
      },
      logConfig: {
        fieldLogLevel: appsync.FieldLogLevel.ALL, // Change to ALL to see resolver details
        excludeVerboseContent: false, // Include verbose content
        retention: logs.RetentionDays.ONE_WEEK
      },
      xrayEnabled: false
    });
    
    

    const invocationHandler = new NodejsFunction(this, 'InvocationHandler', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, 'lambda/invocation/index.ts'),
      timeout: cdk.Duration.minutes(15),
      environment: {
        APPSYNC_ENDPOINT: api.graphqlUrl,
        APPSYNC_API_KEY: api.apiKey || '',
      },
      logRetention: logs.RetentionDays.ONE_WEEK,
      tracing: lambda.Tracing.DISABLED,
      bundling: {
        minify: true,
        sourceMap: false // Disable source maps to reduce log size
      }
    });
    

    // Add Bedrock permissions to Lambda. Add IAM policies for all regions covered under the Inference profile
    invocationHandler.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModelWithResponseStream'],
      resources: [
        'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0',
        'arn:aws:bedrock:us-east-2::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0',
        'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0',
        `arn:aws:bedrock:us-east-1:${this.account}:inference-profile/us.anthropic.claude-3-5-sonnet-20241022-v2:0`
      ]
    }));
    
    // Add AppSync permissions to Lambda
    invocationHandler.addToRolePolicy(new iam.PolicyStatement({
      actions: ['appsync:GraphQL'],
      resources: [api.arn + '/types/Mutation/fields/sendChunk'],
    }));

    // Add CloudWatch Logs permissions to Lambda
    invocationHandler.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'logs:CreateLogStream',
        'logs:PutLogEvents'
      ],
      resources: [
        `arn:aws:logs:${this.region}:${this.account}:log-group:/aws/lambda/*`
      ]
    }));
    

    const invocationDS = api.addLambdaDataSource('InvocationDataSource', invocationHandler);


    invocationDS.createResolver('StartConversationResolver', {
      typeName: 'Mutation',
      fieldName: 'startConversation',
      requestMappingTemplate: appsync.MappingTemplate.fromString(`
        {
          "version": "2018-05-29",
          "operation": "Invoke",
          "invocationType": "Event",
          "payload": $util.toJson($context.arguments)
        }
      `),
      responseMappingTemplate: appsync.MappingTemplate.fromString(`
        #if($context.error)
          $util.error($context.error.message, $context.error.type)
        #end
        {
          "conversationId": "$context.arguments.input.conversationId",
          "status": "STARTED"
        }
      `)
    });
    
    const noneDS = api.addNoneDataSource('NoneDataSource');
    
    noneDS.createResolver('SendChunkResolver', {
      typeName: 'Mutation',
      fieldName: 'sendChunk',
      requestMappingTemplate: appsync.MappingTemplate.fromString(`
        {
          "version": "2018-05-29",
          "payload": {
            "conversationId": "$context.arguments.conversationId",
            "chunk": "$context.arguments.chunk"
          }
        }
      `),
      responseMappingTemplate: appsync.MappingTemplate.fromString(`
        #if($context.error)
          $util.error($context.error.message, $context.error.type)
        #end
        $util.toJson({
          "conversationId": "$context.arguments.conversationId",
          "chunk": "$context.arguments.chunk"
        })
      `)
    });

    noneDS.createResolver('SubscriptionResolver', {
      typeName: 'Subscription',
      fieldName: 'onReceiveChunk',
      requestMappingTemplate: appsync.MappingTemplate.fromString(`
        {
          "version": "2018-05-29",
          "payload": $util.toJson($context.arguments)
        }
      `),
      responseMappingTemplate: appsync.MappingTemplate.fromString(
        '$util.toJson($context.result)'
      ),
    });

    noneDS.createResolver('SendErrorResolver', {
      typeName: 'Mutation',
      fieldName: 'sendError',
      requestMappingTemplate: appsync.MappingTemplate.fromString(`
        #set($logMessage = "sendError invoked with arguments - Conversation ID: $context.arguments.conversationId, Error Message: $context.arguments.error")
        $util.log($logMessage)
        {
          "version": "2018-05-29",
          "payload": {
            "conversationId": "$context.arguments.conversationId",
            "error": "$context.arguments.error"
          }
        }
      `),
      responseMappingTemplate: appsync.MappingTemplate.fromString(`
        #if($context.error)
          $util.error($context.error.message, $context.error.type)
        #end
        $util.toJson($context.result)
      `),
    });

    noneDS.createResolver('CompleteStreamResolver', {
      typeName: 'Mutation',
      fieldName: 'completeStream',
      requestMappingTemplate: appsync.MappingTemplate.fromString(`
        {
          "version": "2017-02-28",
          "payload": {
            "conversationId": "$context.arguments.conversationId",
            "status": "COMPLETED"
          }
        }
      `),
      responseMappingTemplate: appsync.MappingTemplate.fromString(`
        #if($context.error)
          $util.error($context.error.message, $context.error.type)
        #end
        $util.toJson($context.result)
      `)
    });
    
    
    

    // Add CloudWatch dashboard for monitoring
    new cdk.CfnOutput(this, 'GraphQLAPIURL', {
      value: api.graphqlUrl
    });

    new cdk.CfnOutput(this, 'GraphQLAPIKey', {
      value: api.apiKey || ''
    });

    new cdk.CfnOutput(this, 'CloudWatchLogsURL', {
      value: `https://console.aws.amazon.com/cloudwatch/home?region=${this.region}#logsV2:log-groups`
    });
  }
}
