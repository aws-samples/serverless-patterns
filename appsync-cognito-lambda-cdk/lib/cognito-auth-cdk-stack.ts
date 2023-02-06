import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import {
	UserPool,
	UserPoolClient,
	AccountRecovery,
	VerificationEmailStyle,
} from 'aws-cdk-lib/aws-cognito'
import {
	AppsyncFunction,
	AuthorizationType,
	FieldLogLevel,
	GraphqlApi,
	SchemaFile,
	Resolver,
	Code,
	FunctionRuntime,
} from 'aws-cdk-lib/aws-appsync'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as path from 'path'
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs'
import { Tracing } from 'aws-cdk-lib/aws-lambda'

export class CognitoAuthCdkStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		/**
		 * UserPool and UserPool Client
		 */
		const userPool = new UserPool(this, 'CognitoUserPool', {
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

		const userPoolClient = new UserPoolClient(this, 'UserPoolClient', {
			userPool,
		})

		const userLambda = new NodejsFunction(this, 'CognitoUserHandler', {
			tracing: Tracing.ACTIVE,
			runtime: lambda.Runtime.NODEJS_18_X,
			handler: 'handler',
			entry: path.join(__dirname, '/lambda-fns/app.ts'),
			memorySize: 1024,
		})

		const appsyncAPI = new GraphqlApi(this, 'Api', {
			name: 'severlessLandAPI',
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
					{ authorizationType: AuthorizationType.API_KEY },
				],
			},
			logConfig: {
				fieldLogLevel: FieldLogLevel.ALL,
			},
			xrayEnabled: true,
		})

		const appsyncFunction = new AppsyncFunction(this, 'function', {
			name: 'appsync_function',
			api: appsyncAPI,
			dataSource: appsyncAPI.addLambdaDataSource('myLambda', userLambda),
		})

		const pipelineResolver = new Resolver(this, 'pipeline', {
			api: appsyncAPI,
			runtime: FunctionRuntime.JS_1_0_0,
			typeName: 'Query',
			fieldName: 'getUserAccount',
			pipelineConfig: [appsyncFunction],
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
		})

		/**
		 * Outputs
		 */

		new CfnOutput(this, 'UserPoolId', {
			value: userPool.userPoolId,
		})
		new CfnOutput(this, 'UserPoolClientId', {
			value: userPoolClient.userPoolClientId,
		})

		new CfnOutput(this, 'GraphQLAPI ID', {
			value: appsyncAPI.apiId,
		})
	}
}
