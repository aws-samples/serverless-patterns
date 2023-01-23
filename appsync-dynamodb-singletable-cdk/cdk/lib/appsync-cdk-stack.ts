import { Stack, StackProps } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import { Table, BillingMode, AttributeType } from 'aws-cdk-lib/aws-dynamodb'
import {
	AppsyncFunction,
	Code,
	FunctionRuntime,
	GraphqlApi,
	InlineCode,
	Resolver,
	SchemaFile,
} from 'aws-cdk-lib/aws-appsync'
import { join } from 'path'

export class AppsyncCdkStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		// DynamoDB Table
		const DDBTable = new Table(this, 'MDDBTable', {
			partitionKey: { name: 'PK', type: AttributeType.STRING },
			sortKey: { name: 'SK', type: AttributeType.STRING },
			billingMode: BillingMode.PAY_PER_REQUEST,
		})

		// AppSync GraphQL API
		const AppSyncApi = new GraphqlApi(this, 'AppSyncApi', {
			name: 'SingleTableApiCDK',
			schema: SchemaFile.fromAsset(join(__dirname, 'schema.graphql')),
		})

		// AppSync Data Source -> DynamoDB table
		const DDBDataSource = AppSyncApi.addDynamoDbDataSource(
			'DDBDataSource',
			DDBTable
		)

		const getParentWithChildrenFunc = new AppsyncFunction(
			this,
			'getParentWithChildrenFunction',
			{
				name: 'getParentWithChildrenFunction',
				api: AppSyncApi,
				dataSource: DDBDataSource,
				code: Code.fromAsset(
					join(__dirname, '/mappings/Query.getParentWithChildren.js')
				),
				runtime: FunctionRuntime.JS_1_0_0,
			}
		)

		const createItemFunction = new AppsyncFunction(this, 'createItemFunction', {
			name: 'createItemFunction',
			api: AppSyncApi,
			dataSource: DDBDataSource,
			code: Code.fromAsset(join(__dirname, '/mappings/Mutation.createItem.js')),
			runtime: FunctionRuntime.JS_1_0_0,
		})

		const passthrough = InlineCode.fromInline(`
        // The before step
        export function request(...args) {
          console.log(args);
          return {}
        }

        // The after step
        export function response(ctx) {
          return ctx.prev.result
        }
    `)

		const parentWithChildrenResolver = new Resolver(
			this,
			'parentWithChildrenResolver',
			{
				api: AppSyncApi,
				typeName: 'Query',
				fieldName: 'getParentWithChildren',
				runtime: FunctionRuntime.JS_1_0_0,
				pipelineConfig: [getParentWithChildrenFunc],
				code: passthrough,
			}
		)
		const createParentResolver = new Resolver(this, 'createParentResolver', {
			api: AppSyncApi,
			typeName: 'Mutation',
			fieldName: 'createParentItem',
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [createItemFunction],
			code: passthrough,
		})

		const createChildResolver = new Resolver(this, 'createChildResolver', {
			api: AppSyncApi,
			typeName: 'Mutation',
			fieldName: 'createChildItem',
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [createItemFunction],
			code: passthrough,
		})
	}
}
