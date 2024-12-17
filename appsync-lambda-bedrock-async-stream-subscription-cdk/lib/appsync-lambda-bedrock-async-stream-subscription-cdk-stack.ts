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
    super(scope, id, props);

    const api = new appsync.GraphqlApi(this, 'Api', {
      name: 'bedrock-streaming-api',
      schema: appsync.SchemaFile.fromAsset('schema.graphql'),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.API_KEY,
        },
      },
      logConfig: {
        fieldLogLevel: appsync.FieldLogLevel.ALL,
        excludeVerboseContent: false,
        retention: logs.RetentionDays.ONE_WEEK
      },
      xrayEnabled: true
    });    

    const invocationHandler = new NodejsFunction(this, 'InvocationHandler', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, 'lambda/invocation/index.ts'),
      timeout: cdk.Duration.seconds(300),
      environment: {
        APPSYNC_ENDPOINT: api.graphqlUrl,
        APPSYNC_API_KEY: api.apiKey || '',
      },
      logRetention: logs.RetentionDays.ONE_WEEK,
      tracing: lambda.Tracing.ACTIVE
    });

    // Add Bedrock permissions to Lambda
    invocationHandler.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModelWithResponseStream'],
      resources: ['arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2'],
    }));

    // Add AppSync permissions to Lambda
    invocationHandler.addToRolePolicy(new iam.PolicyStatement({
      actions: ['appsync:GraphQL'],
      resources: [api.arn + '/types/Mutation/fields/sendChunk'],
    }));

    // Add CloudWatch Logs permissions to Lambda
    invocationHandler.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents'
      ],
      resources: ['*']
    }));

    const invocationDS = api.addLambdaDataSource('InvocationDataSource', invocationHandler);
    const noneDS = api.addNoneDataSource('NoneDataSource');

    invocationDS.createResolver('StartConversationResolver', {
      typeName: 'Mutation',
      fieldName: 'startConversation',
    });

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
