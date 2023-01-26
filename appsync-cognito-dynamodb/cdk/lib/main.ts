import { CfnOutput, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib'
import {
	AccountRecovery,
	UserPool,
	UserPoolClient,
	VerificationEmailStyle,
} from 'aws-cdk-lib/aws-cognito'

import {
	IdentityPool,
	UserPoolAuthenticationProvider,
} from '@aws-cdk/aws-cognito-identitypool-alpha'
import { AttributeType, BillingMode, Table } from 'aws-cdk-lib/aws-dynamodb'
import {
	AppsyncFunction,
	AuthorizationType,
	Code,
	FieldLogLevel,
	FunctionRuntime,
	GraphqlApi,
	Resolver,
	SchemaFile,
} from 'aws-cdk-lib/aws-appsync'
import { Construct } from 'constructs'
import * as path from 'path'

export class CdkStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		// create the user pool
		const userPool = new UserPool(this, 'UserDemoPool', {
			selfSignUpEnabled: true,
			accountRecovery: AccountRecovery.PHONE_AND_EMAIL,
			userVerification: {
				emailStyle: VerificationEmailStyle.CODE,
			},
			autoVerify: {
				email: true,
			},
			standardAttributes: {
				email: {
					required: true,
					mutable: true,
				},
			},
		})

		// create the user pool client for the frontend
		const userPoolClient = new UserPoolClient(this, 'UserListPoolClient', {
			userPool,
		})

		// create the identity pool
		const identityPool = new IdentityPool(this, 'IdentityDemoPool', {
			identityPoolName: 'identityDemoForUserData',
			allowUnauthenticatedIdentities: true,
			authenticationProviders: {
				userPools: [
					new UserPoolAuthenticationProvider({ userPool, userPoolClient }),
				],
			},
		})

		// create the dynamodb table
		const userTable = new Table(this, 'UsersAPITable', {
			removalPolicy: RemovalPolicy.DESTROY,
			billingMode: BillingMode.PAY_PER_REQUEST,
			partitionKey: { name: 'userId', type: AttributeType.STRING },
		})

		// create an API that defaults to userpools, but also uses IAM
		const api = new GraphqlApi(this, 'UsersAPI', {
			name: 'UsersAPI',
			schema: SchemaFile.fromAsset(
				path.join(__dirname, '../graphql/schema.graphql')
			),
			authorizationConfig: {
				defaultAuthorization: {
					authorizationType: AuthorizationType.USER_POOL,
					userPoolConfig: {
						userPool,
					},
				},
				additionalAuthorizationModes: [
					{
						authorizationType: AuthorizationType.IAM,
					},
				],
			},
			logConfig: {
				fieldLogLevel: FieldLogLevel.ALL,
			},
			xrayEnabled: true,
		})

		// allow unauthenticated access to the `listUsers` query
		api.grantQuery(identityPool.unauthenticatedRole, 'listUsers')

		// add our DynamoDB table as a datasource for our API
		const userTableDS = api.addDynamoDbDataSource('userTableDS', userTable)

		// Create the listUsers function and add it to its pipeline
		const listUsersFunction = new AppsyncFunction(this, 'listUsersFunction', {
			name: 'listUsersFunction',
			api,
			dataSource: userTableDS,
			code: Code.fromAsset(
				path.join(__dirname, '../graphql/Query.listUsers.js')
			),
			runtime: FunctionRuntime.JS_1_0_0,
		})

		new Resolver(this, 'listUsersPipelineResolver', {
			api,
			typeName: 'Query',
			fieldName: 'listUsers',
			code: Code.fromAsset(
				path.join(__dirname, '../graphql/Pipeline.simple.js')
			),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [listUsersFunction],
		})

		// create the createUserFunction and add it to its pipeline
		const createUserFunction = new AppsyncFunction(this, 'createUser', {
			name: 'createUserFunction',
			api,
			dataSource: userTableDS,
			code: Code.fromAsset(
				path.join(__dirname, '../graphql/Mutation.createUser.js')
			),
			runtime: FunctionRuntime.JS_1_0_0,
		})

		new Resolver(this, 'createUserPipelineResolver', {
			api,
			typeName: 'Mutation',
			fieldName: 'createUser',
			code: Code.fromAsset(
				path.join(__dirname, '../graphql/Pipeline.simple.js')
			),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [createUserFunction],
		})

		// outputs
		new CfnOutput(this, 'UserPoolId', {
			value: userPool.userPoolId,
		})

		new CfnOutput(this, 'UserPoolClientId', {
			value: userPoolClient.userPoolClientId,
		})

		new CfnOutput(this, 'IdentityPoolId', {
			value: identityPool.identityPoolId,
		})

		new CfnOutput(this, 'GraphQLAPIID', {
			value: api.apiId,
		})

		new CfnOutput(this, 'GraphQLURL', {
			value: api.graphqlUrl,
		})
	}
}
