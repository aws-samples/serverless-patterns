import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import { aws_sns as sns } from 'aws-cdk-lib'
import * as appsync from 'aws-cdk-lib/aws-appsync'
import { join } from 'path'

export class CdkAppSyncSnSStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		const region = Stack.of(this).region

		const api = new appsync.GraphqlApi(this, 'Api', {
			name: 'ToSnSApi',
			schema: appsync.SchemaFile.fromAsset(
				join(__dirname, '../graphql/schema.graphql')
			),
		})

		const topic = new sns.Topic(this, 'topic')
		const datasource = api.addHttpDataSource(
			'sns',
			`https://sns.${region}.amazonaws.com`,
			{
				authorizationConfig: {
					signingRegion: region,
					signingServiceName: 'sns',
				},
			}
		)

		datasource.node.addDependency(topic)
		topic.grantPublish(datasource.grantPrincipal)

		const myJsFunction = new appsync.AppsyncFunction(this, 'function', {
			name: 'my_js_function',
			api,
			dataSource: datasource,
			code: appsync.Code.fromAsset(
				join(__dirname, '../graphql/Query.publish.js')
			),
			runtime: appsync.FunctionRuntime.JS_1_0_0,
		})

		const topicArnObj = JSON.stringify({ TOPIC_ARN: topic.topicArn })
		new appsync.Resolver(this, 'PipelineResolver', {
			api,
			typeName: 'Query',
			fieldName: 'publish',
			code: appsync.Code.fromInline(`
            // The before step
            export function request(...args) {
              console.log(args);
              
              return ${topicArnObj}
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
		new CfnOutput(this, 'topicName', { value: topic.topicName })
	}
}
