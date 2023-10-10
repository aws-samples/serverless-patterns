import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import {
	GraphqlApi,
	SchemaFile,
	AuthorizationType,
	AppsyncFunction,
	Code,
	FunctionRuntime,
	Resolver,
} from 'aws-cdk-lib/aws-appsync'
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs'
import { join } from 'path'
import { Runtime } from 'aws-cdk-lib/aws-lambda'

export class MainStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		const api = new GraphqlApi(this, 'Api', {
			name: 'TriggeredByLambda',
			schema: SchemaFile.fromAsset(
				join(__dirname, '../graphql/schema.graphql')
			),
			authorizationConfig: {
				defaultAuthorization: {
					authorizationType: AuthorizationType.IAM,
				},
			},
		})

		const createTodoFunc = new AppsyncFunction(this, 'createTodoFunction', {
			name: 'createTodoFunction',
			api,
			dataSource: api.addNoneDataSource('none'),
			code: Code.fromAsset(
				join(__dirname, '../graphql/Mutation.createTodo.js')
			),
			runtime: FunctionRuntime.JS_1_0_0,
		})

		new Resolver(this, 'PipelineResolver', {
			api,
			typeName: 'Mutation',
			fieldName: 'createTodo',
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
			pipelineConfig: [createTodoFunc],
		})

		const lambda = new NodejsFunction(this, 'trigger', {
			runtime: Runtime.NODEJS_16_X,
			bundling: {
				target: 'es2020',

				commandHooks: {
					beforeInstall: (inputDir: string, outputDir: string) => [],
					beforeBundling: (inputDir: string, outputDir: string) => [
						`cd graphql`,
						`amplify codegen`,
					],
					afterBundling: (inputDir: string, outputDir: string) => [],
				},
			},
			environment: {
				GRAPHQL_URL: api.graphqlUrl,
			},
		})
		api.grantMutation(lambda)

		new CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
		new CfnOutput(this, 'apiId', { value: api.apiId })
		new CfnOutput(this, 'functionArn', { value: lambda.functionArn })
		new CfnOutput(this, 'functionName', { value: lambda.functionName })
	}
}
