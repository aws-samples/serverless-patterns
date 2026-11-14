import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import { aws_sqs as sqs } from 'aws-cdk-lib'
import * as appsync from 'aws-cdk-lib/aws-appsync'
import { join } from 'path'

const REQUEST_TEMPLATE = (accountId: String, queue: sqs.Queue) => {
	return `
#set ($body = "Action=SendMessage&Version=2012-11-05")
#set ($messageBody = $util.urlEncode($util.toJson($ctx.args)))
#set ($queueUrl = $util.urlEncode("${queue.queueUrl}"))
#set ($body = "$body&MessageBody=$messageBody&QueueUrl=$queueUrl")

{
  "version": "2018-05-29",
  "method": "POST",
  "resourcePath": "/${accountId}/${queue.queueName}",
  "params": {
    "body": "$body",
    "headers": {
      "content-type": "application/x-www-form-urlencoded"
    }
  }
}
`
}

const RESPONSE_TEMPLATE = `
#if($ctx.result.statusCode == 200)
    ##if response is 200
    ## Because the response is of type XML, we are going to convert
    ## the result body as a map and only get the User object.
    $utils.toJson($utils.xml.toMap($ctx.result.body).SendMessageResponse.SendMessageResult)
#else
    ##if response is not 200, append the response to error block.
    $utils.appendError($ctx.result.body, "$ctx.result.statusCode")
    null
#end
`

export class CdkAppSyncSqSStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		const region = Stack.of(this).region
		const account = Stack.of(this).account

		const api = new appsync.GraphqlApi(this, 'Api', {
			name: 'ToSqSApi',
			schema: appsync.SchemaFile.fromAsset(
				join(__dirname, '../graphql/schema.graphql')
			),
		})

		const queue = new sqs.Queue(this, 'queue')
		const datasource = api.addHttpDataSource(
			'sqs',
			`https://sqs.${region}.amazonaws.com`,
			{
				authorizationConfig: {
					signingRegion: region,
					signingServiceName: 'sqs',
				},
			}
		)
		datasource.node.addDependency(queue)
		queue.grantSendMessages(datasource.grantPrincipal)

		const myJsFunction = new appsync.AppsyncFunction(this, 'function', {
			name: 'my_js_function',
			api,
			dataSource: datasource,
			code: appsync.Code.fromAsset(
				join(__dirname, '../graphql/Query.sendMessage.js')
			),
			runtime: appsync.FunctionRuntime.JS_1_0_0,
		})

		const pipelineVars = JSON.stringify({
			accountId: account,
			queueUrl: queue.queueUrl,
			queueName: queue.queueName,
		})
		new appsync.Resolver(this, 'PipelineResolver', {
			api,
			typeName: 'Query',
			fieldName: 'sendMessage',
			code: appsync.Code.fromInline(`
            // The before step
            export function request(...args) {
              console.log(args);
              return ${pipelineVars}
            }
        
            // The after step
            export function response(ctx) {
              return ctx.prev.result
            }
          `),
			runtime: appsync.FunctionRuntime.JS_1_0_0,
			pipelineConfig: [myJsFunction],
		})

		new CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
		new CfnOutput(this, 'apiKey', { value: api.apiKey! })
		new CfnOutput(this, 'apiId', { value: api.apiId })
		new CfnOutput(this, 'queueUrl', { value: queue.queueUrl })
	}
}
