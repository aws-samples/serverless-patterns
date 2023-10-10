import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import { GraphqlApi, SchemaFile, FieldLogLevel } from 'aws-cdk-lib/aws-appsync'
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs'
import { join } from 'path'

export class MainStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props)

		const api = new GraphqlApi(this, 'Api', {
			name: 'AppsyncWithLambdaResolverApi',
			schema: SchemaFile.fromAsset(join(__dirname, 'schema.graphql')),
			xrayEnabled: true,
			logConfig: {
				excludeVerboseContent: false,
				fieldLogLevel: FieldLogLevel.ALL,
			},
		})

		const directLambda = new NodejsFunction(this, 'resolver')
		const datasource = api.addLambdaDataSource('directLambda', directLambda)

		const fields = [
			{ typeName: 'Query', fieldName: 'getTodo' },
			{ typeName: 'Query', fieldName: 'listTodos' },
			{ typeName: 'Mutation', fieldName: 'createTodo' },
			{ typeName: 'Mutation', fieldName: 'updateTodo' },
			{ typeName: 'Mutation', fieldName: 'deleteTodo' },
		]
		fields.forEach(({ typeName, fieldName }) =>
			datasource.createResolver(`${typeName}${fieldName}Resolver`, {
				typeName,
				fieldName,
			})
		)

		new CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
		new CfnOutput(this, 'apiKey', { value: api.apiKey! })
		new CfnOutput(this, 'apiId', { value: api.apiId })
		new CfnOutput(this, 'lambda', { value: directLambda.functionArn })
	}
}
