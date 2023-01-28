import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib'
import { Table } from 'aws-cdk-lib/aws-dynamodb'
import { Construct } from 'constructs'
import * as path from 'path'

import { UserPool } from 'aws-cdk-lib/aws-cognito'
import { IRole } from 'aws-cdk-lib/aws-iam'
import { IdentityPool } from '@aws-cdk/aws-cognito-identitypool-alpha'
import {
	GraphqlApi,
	SchemaFile,
	AuthorizationType,
	FieldLogLevel,
	MappingTemplate,
	PrimaryKey,
	Values,
	Code,
	UserPoolDefaultAction,
	AppsyncFunction,
	FunctionRuntime,
	Resolver,
} from 'aws-cdk-lib/aws-appsync'

interface APIStackProps extends StackProps {
	userpool: UserPool
	sampleTable: Table
	unauthenticatedRole: IRole
	identityPool: IdentityPool
}

export class APIStack extends Stack {
	public readonly graphqlURL: string
	constructor(scope: Construct, id: string, props: APIStackProps) {
		super(scope, id, props)

		const api = new GraphqlApi(this, 'APISamples', {
			name: 'APISamples',
			schema: SchemaFile.fromAsset(
				path.join(__dirname, 'graphql/schema.graphql')
			),
			authorizationConfig: {
				defaultAuthorization: {
					authorizationType: AuthorizationType.USER_POOL,
					userPoolConfig: {
						defaultAction: UserPoolDefaultAction.ALLOW,
						userPool: props.userpool,
					},
				},
				additionalAuthorizationModes: [
					{ authorizationType: AuthorizationType.IAM },
				],
			},
			logConfig: {
				fieldLogLevel: FieldLogLevel.ALL,
			},
			xrayEnabled: true,
		})

		const ProductDataSource = api.addDynamoDbDataSource(
			'ProductDataSource',
			props.sampleTable
		)

		api.grantQuery(props.unauthenticatedRole, 'getProduct', 'listProducts')

		const getProductFunction = new AppsyncFunction(this, 'getProductFunction', {
			name: 'getProductFunction',
			api,
			dataSource: ProductDataSource,
			requestMappingTemplate: MappingTemplate.dynamoDbGetItem('id', 'id'),
			responseMappingTemplate: MappingTemplate.dynamoDbResultItem(),
		})

		const createProductFunction = new AppsyncFunction(
			this,
			'createProductFunction',
			{
				name: 'createProductFunction',
				api,
				dataSource: ProductDataSource,
				requestMappingTemplate: MappingTemplate.dynamoDbPutItem(
					PrimaryKey.partition('id').auto(),
					Values.projecting('input')
				),
				responseMappingTemplate: MappingTemplate.dynamoDbResultItem(),
			}
		)

		const listProductsFunction = new AppsyncFunction(
			this,
			'listProductsFunction',
			{
				name: 'listProductsFunction',
				api,
				dataSource: ProductDataSource,
				requestMappingTemplate: MappingTemplate.dynamoDbScanTable(),
				responseMappingTemplate: MappingTemplate.dynamoDbResultList(),
			}
		)

		const passThroughSteps = `
    // The before step
    export function request(...args) {
      console.log(args);
      return {}
    }

    // The after step
    export function response(ctx) {
      return ctx.prev.result
    }
  `
		new Resolver(this, 'getProductPipelineResolver', {
			api,
			typeName: 'Query',
			fieldName: 'getProduct',
			code: Code.fromInline(passThroughSteps),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [getProductFunction],
		})

		new Resolver(this, 'createProductPipelineResolver', {
			api,
			typeName: 'Mutation',
			fieldName: 'createProduct',
			code: Code.fromInline(passThroughSteps),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [createProductFunction],
		})

		new Resolver(this, 'listProductsPipelineResolver', {
			api,
			typeName: 'Query',
			fieldName: 'listProducts',
			code: Code.fromInline(passThroughSteps),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [listProductsFunction],
		})

		this.graphqlURL = api.graphqlUrl
		new CfnOutput(this, 'GraphQLAPIURL', {
			value: api.graphqlUrl,
		})

		new CfnOutput(this, 'GraphQLAPIID', {
			value: api.apiId,
		})
	}
}
