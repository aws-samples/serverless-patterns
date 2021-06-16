import * as cdk from '@aws-cdk/core'
import { GraphqlApi, Schema, FieldLogLevel, AuthorizationType } from '@aws-cdk/aws-appsync'
import { NodejsFunction } from '@aws-cdk/aws-lambda-nodejs'
import { join } from 'path'

export class MainStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const api = new GraphqlApi(this, 'Api', {
      name: 'AppsyncWithLambdaResolverApi',
      schema: Schema.fromAsset(join(__dirname, 'schema.graphql')),
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
    fields.forEach(({ typeName, fieldName }) => datasource.createResolver({ typeName, fieldName }))

    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'lambda', { value: directLambda.functionArn })
  }
}
