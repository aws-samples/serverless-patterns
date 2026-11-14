import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import {
	Pass,
	StateMachine,
	StateMachineType,
} from 'aws-cdk-lib/aws-stepfunctions'
import {
	GraphqlApi,
	SchemaFile,
	FieldLogLevel,
	AppsyncFunction,
	Code,
	FunctionRuntime,
	Resolver,
} from 'aws-cdk-lib/aws-appsync'
import { Role, ServicePrincipal, PolicyStatement } from 'aws-cdk-lib/aws-iam'
import { join } from 'path'

export class AppsyncExpressWorkflowStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		// The code that defines your stack goes here
		const stateMachineDefinition = new Pass(this, 'passState', {
			result: { value: 'Hello from StepFunctions!' },
		})

		const stateMachine = new StateMachine(this, 'SyncStateMachine', {
			definition: stateMachineDefinition,
			stateMachineType: StateMachineType.EXPRESS,
		})

		const api = new GraphqlApi(this, 'Api', {
			name: 'SyncStateMachineAPI',
			schema: SchemaFile.fromAsset(
				join(__dirname, '../graphql/schema.graphql')
			),
			xrayEnabled: true,
			logConfig: {
				excludeVerboseContent: false,
				fieldLogLevel: FieldLogLevel.ALL,
			},
		})

		const appsyncStepFunctionsRole = new Role(this, 'SyncStateMachineRole', {
			assumedBy: new ServicePrincipal('appsync.amazonaws.com'),
		})
		appsyncStepFunctionsRole.addToPolicy(
			new PolicyStatement({
				resources: ['*'],
				actions: ['states:StartSyncExecution'],
			})
		)

		const endpoint = 'https://sync-states.' + this.region + '.amazonaws.com/'
		const httpdatasource = api.addHttpDataSource(
			'StepFunctionsStateMachine',
			endpoint,
			{
				authorizationConfig: {
					signingRegion: this.region,
					signingServiceName: 'states',
				},
			}
		)

		stateMachine.grant(
			httpdatasource.grantPrincipal,
			'states:StartSyncExecution'
		)

		const myJsFunction = new AppsyncFunction(this, 'function', {
			name: 'my_js_function',
			api,
			dataSource: httpdatasource,
			code: Code.fromAsset(
				join(__dirname, '../graphql/Mutation.startExecution.js')
			),
			runtime: FunctionRuntime.JS_1_0_0,
		})

		const pipelineVars = JSON.stringify({
			STATE_MACHINE_ARN: stateMachine.stateMachineArn,
		})
		new Resolver(this, 'PipelineResolver', {
			api,
			typeName: 'Mutation',
			fieldName: 'startExecution',
			code: Code.fromInline(`
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
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [myJsFunction],
		})

		new CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
		new CfnOutput(this, 'apiKey', { value: api.apiKey! })
		new CfnOutput(this, 'apiId', { value: api.apiId })
		new CfnOutput(this, 'stateMachine', { value: stateMachine.stateMachineArn })
	}
}
