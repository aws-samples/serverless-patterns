import * as cdk from 'aws-cdk-lib'
import { CfnOutput } from 'aws-cdk-lib'
import {
	AppsyncFunction,
	AuthorizationType,
	Code,
	FieldLogLevel,
	FunctionRuntime,
	GraphqlApi,
	HttpDataSource,
	Resolver,
	SchemaFile,
} from 'aws-cdk-lib/aws-appsync'

import {
	PolicyDocument,
	PolicyStatement,
	Role,
	ServicePrincipal,
} from 'aws-cdk-lib/aws-iam'
import { Topic } from 'aws-cdk-lib/aws-sns'
import { Construct } from 'constructs'
import * as path from 'path'

export class AppsyncEbschedulerSnsStack extends cdk.Stack {
	constructor(scope: Construct, id: string, props?: cdk.StackProps) {
		super(scope, id, props)
		// create the SNS topic
		const reminderTopic = new Topic(this, 'reminderTopic', {
			topicName: 'reminderTopic',
		})

		// create the role used for the scheduler
		const schedulerRole = new Role(this, 'schedulerRole', {
			roleName: 'allowSchedulerToPublishToSNS',
			assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
			inlinePolicies: {
				publishToSNS: new PolicyDocument({
					statements: [
						new PolicyStatement({
							actions: ['sns:publish'],
							resources: [reminderTopic.topicArn],
						}),
					],
				}),
			},
		})

		// create appsync api
		const api = new GraphqlApi(this, 'ReminderAPI', {
			name: 'ReminderAPI',
			schema: SchemaFile.fromAsset(
				path.join(__dirname, '/graphql/schema.graphql')
			),
			authorizationConfig: {
				defaultAuthorization: {
					authorizationType: AuthorizationType.API_KEY,
				},
			},
			logConfig: {
				fieldLogLevel: FieldLogLevel.ALL,
			},
		})

		// create the http datasource
		const EBSchedulerDS = new HttpDataSource(this, 'EBSchedulerDS', {
			name: 'EBSchedulerDS',
			api,
			endpoint: `https://scheduler.${this.region}.amazonaws.com`,
			authorizationConfig: {
				signingRegion: this.region,
				signingServiceName: 'scheduler',
			},
		})

		// let the datasource create a scheduler
		EBSchedulerDS.grantPrincipal.addToPrincipalPolicy(
			new PolicyStatement({
				actions: ['scheduler:CreateSchedule'],
				resources: [
					`arn:aws:scheduler:${this.region}:${this.account}:schedule/default/*`,
				],
			})
		)

		// let the datasource pass and IAM role (see inline pipeline code below)
		EBSchedulerDS.grantPrincipal.addToPrincipalPolicy(
			new PolicyStatement({
				actions: ['iam:PassRole'],
				resources: [schedulerRole.roleArn],
			})
		)
		// Create the AppSync function that will create the scheduler
		const createScheduleFunction = new AppsyncFunction(
			this,
			'createScheduleFunction',
			{
				name: 'createScheduleFunction',
				api,
				dataSource: EBSchedulerDS,
				code: Code.fromAsset(
					path.join(__dirname, '/graphql/mappings/Mutation.createSchedule.js')
				),
				runtime: FunctionRuntime.JS_1_0_0,
			}
		)

		//Create the pipeline that will include setup code
		new Resolver(this, 'PipelineResolver', {
			api,
			typeName: 'Mutation',
			fieldName: 'createSchedule',
			code: Code.fromInline(`
    // The before step (no before steps)
    export function request(ctx) {
      ctx.stash.SNS_TOPIC_ARN = "${reminderTopic.topicArn}"
      ctx.stash.SCHEDULER_ROLE_ARN = "${schedulerRole.roleArn}"
      return {}
    }
    // The after step (simply return the result)
    export function response(ctx) {
      return ctx.prev.result
    }
  `),
			runtime: FunctionRuntime.JS_1_0_0,
			pipelineConfig: [createScheduleFunction],
		})

		new CfnOutput(this, 'GraphQLAPIID', {
			value: api.apiId,
		})
		new CfnOutput(this, 'GraphQLAPIKey', {
			value: api.apiKey!,
		})

		new CfnOutput(this, 'GraphQLURL', {
			value: api.graphqlUrl,
		})
	}
}
