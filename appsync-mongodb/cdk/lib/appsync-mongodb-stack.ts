import * as cdk from 'aws-cdk-lib'
import { Construct } from 'constructs'
import * as path from 'path'
import * as appsync from 'aws-cdk-lib/aws-appsync'
import { PolicyStatement } from 'aws-cdk-lib/aws-iam'

interface AppsyncMongoStackProps extends cdk.StackProps {
	MONGO_SECRET_ARN: string
}

export class AppsyncMongoStack extends cdk.Stack {
	constructor(scope: Construct, id: string, props: AppsyncMongoStackProps) {
		super(scope, id, props)

		//create our API
		const api = new appsync.GraphqlApi(this, 'AppSyncToMongoAPI', {
			name: 'AppSyncToMongoAPI',
			schema: appsync.SchemaFile.fromAsset(
				path.join(__dirname, 'graphql/schema.graphql')
			),
			authorizationConfig: {
				defaultAuthorization: {
					authorizationType: appsync.AuthorizationType.API_KEY,
				},
			},
			logConfig: {
				fieldLogLevel: appsync.FieldLogLevel.ALL,
			},
			xrayEnabled: true,
		})

		// Create our 2 datasources

		// Secrets Manager
		const secretsManagerDS = api.addHttpDataSource(
			'secretsManager',
			`https://secretsmanager.${process.env.CDK_DEFAULT_REGION}.amazonaws.com`,
			{
				authorizationConfig: {
					signingRegion: `${process.env.CDK_DEFAULT_REGION}`,
					signingServiceName: 'secretsmanager',
				},
			}
		)

		// The MongoDB API
		const mongoDataAPIDS = api.addHttpDataSource(
			'mongoDBAtlasCluster',
			'https://data.mongodb-api.com'
		)

		// policy to permit an http datasource to get a secret in Secrets Manager
		secretsManagerDS.grantPrincipal.addToPrincipalPolicy(
			new PolicyStatement({
				resources: [props.MONGO_SECRET_ARN],
				actions: ['secretsmanager:GetSecretValue'],
			})
		)
		///////////////
		// Create a function that gets the secret
		const getMongoSecretFunc = new appsync.AppsyncFunction(
			this,
			'getMongoSecretFunc',
			{
				api,
				dataSource: secretsManagerDS,
				name: 'getMongoSecretFromSSM',
				code: appsync.Code.fromAsset(
					path.join(__dirname, '/graphql/mappings/getMongoSecret.js')
				),
				runtime: appsync.FunctionRuntime.JS_1_0_0,
			}
		)

		////////////////

		// Create a function that will list the Applicants from MongoDB
		const listApplicantsFunction = new appsync.AppsyncFunction(
			this,
			'listApplicantsFunction',
			{
				api,
				dataSource: mongoDataAPIDS,
				name: 'listApplicantsFunction',
				code: appsync.Code.fromAsset(
					path.join(__dirname, '/graphql/mappings/listApplicants.js')
				),
				runtime: appsync.FunctionRuntime.JS_1_0_0,
			}
		)

		////////////////////
		// Create a function that will add an Applicant to MongoDB
		const addApplicantFunction = new appsync.AppsyncFunction(
			this,
			'addApplicantFunction',
			{
				api,
				dataSource: mongoDataAPIDS,
				name: 'addApplicantFunction',
				code: appsync.Code.fromAsset(
					path.join(__dirname, '/graphql/mappings/addApplicant.js')
				),
				runtime: appsync.FunctionRuntime.JS_1_0_0,
			}
		)
		///////////////

		// Create a pipeline that has a "before" and "after" step + our fns
		const listApplicantsPipelineResolver = new appsync.Resolver(
			this,
			'listApplicantsPipelineResolver',
			{
				api,
				typeName: 'Query',
				fieldName: 'listApplicants',
				runtime: appsync.FunctionRuntime.JS_1_0_0,
				code: appsync.Code.fromAsset(
					path.join(__dirname, '/graphql/mappings/pipeline.js')
				),
				pipelineConfig: [getMongoSecretFunc, listApplicantsFunction],
			}
		)

		///////////////////

		// Create a pipeline that has a "before" and "after" step + our fns
		const addApplicantPipelineResolver = new appsync.Resolver(
			this,
			'addApplicantPipelineResolver',
			{
				api,
				typeName: 'Mutation',
				fieldName: 'addApplicant',
				runtime: appsync.FunctionRuntime.JS_1_0_0,
				code: appsync.Code.fromAsset(
					path.join(__dirname, '/graphql/mappings/pipeline.js')
				),
				pipelineConfig: [getMongoSecretFunc, addApplicantFunction],
			}
		)

		//////////////////////////
		new cdk.CfnOutput(this, 'appsync api key', {
			value: api.apiKey!,
		})

		new cdk.CfnOutput(this, 'appsync endpoint', {
			value: api.graphqlUrl,
		})

		new cdk.CfnOutput(this, 'appsync apiId', {
			value: api.apiId,
		})
	}
}
