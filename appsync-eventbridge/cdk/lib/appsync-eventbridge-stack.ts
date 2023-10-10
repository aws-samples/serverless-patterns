import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import {
	GraphqlApi,
	SchemaFile,
	FieldLogLevel,
	AppsyncFunction,
	Code,
	FunctionRuntime,
	Resolver,
} from 'aws-cdk-lib/aws-appsync'

import { EventBus } from 'aws-cdk-lib/aws-events'
import { join } from 'path'

export class AppsyncEventbridgeStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		const eventBus = new EventBus(this, 'bus', {
			eventBusName: 'AppSyncEventBus',
		})

		const api = new GraphqlApi(this, 'Api', {
			name: 'AppSyncEventBridgeAPI',
			schema: SchemaFile.fromAsset(
				join(__dirname, '../graphql/schema.graphql')
			),
			xrayEnabled: true,
			logConfig: {
				excludeVerboseContent: false,
				fieldLogLevel: FieldLogLevel.ALL,
			},
		})

		const endpoint = 'https://events.' + this.region + '.amazonaws.com/'
		const httpdatasource = api.addHttpDataSource('putEventDS', endpoint, {
			authorizationConfig: {
				signingRegion: this.region,
				signingServiceName: 'events',
			},
		})

		eventBus.grantPutEventsTo(httpdatasource.grantPrincipal)

		const myJsFunction = new AppsyncFunction(this, 'function', {
			name: 'my_js_function',
			api,
			dataSource: httpdatasource,
			code: Code.fromAsset(join(__dirname, '../graphql/Mutation.putEvent.js')),
			runtime: FunctionRuntime.JS_1_0_0,
		})

		new Resolver(this, 'PipelineResolver', {
			api,
			typeName: 'Mutation',
			fieldName: 'putEvent',
			code: Code.fromInline(`
    // The before step
    export function request(...args) {
      console.log(args);
      return {}
    }

    // The after step
    export function response(ctx) {
      return ctx.prev.result
    }
  `),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [myJsFunction],
		})

		new CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
		new CfnOutput(this, 'apiKey', { value: api.apiKey! })
		new CfnOutput(this, 'apiId', { value: api.apiId })
		new CfnOutput(this, 'eventBus', { value: eventBus.eventBusArn })
	}
}
