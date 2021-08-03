import * as cdk from '@aws-cdk/core'
import { GraphqlApi, Schema, MappingTemplate, AuthorizationType } from '@aws-cdk/aws-appsync'
import { NodejsFunction } from '@aws-cdk/aws-lambda-nodejs'
import { join } from 'path'

const requestTemplate = `
$util.qr($ctx.args.put("id", $util.defaultIfNull($ctx.args.id, $util.autoId())))
#set( $createdAt = $util.time.nowISO8601() )
$util.qr($context.args.put("createdAt", $createdAt))
$util.qr($context.args.put("updatedAt", $createdAt))
{
  "version": "2017-02-28",
  "payload": $util.toJson($ctx.args)
}`

const responseTemplate = `$util.toJson($context.result)`

export class MainStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const api = new GraphqlApi(this, 'Api', {
      name: 'TriggeredByLambda',
      schema: Schema.fromAsset(join(__dirname, 'schema.graphql')),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: AuthorizationType.IAM,
        },
      },
    })
    const noneDS = api.addNoneDataSource('NONE')
    noneDS.createResolver({
      typeName: 'Mutation',
      fieldName: 'createTodo',
      requestMappingTemplate: MappingTemplate.fromString(requestTemplate),
      responseMappingTemplate: MappingTemplate.fromString(responseTemplate),
    })

    const lambda = new NodejsFunction(this, 'trigger', {
      bundling: {
        target: 'es2020',
        commandHooks: {
          beforeInstall: (inputDir: string, outputDir: string) => [],
          beforeBundling: (inputDir: string, outputDir: string) => [`cd lib`, `amplify codegen`],
          afterBundling: (inputDir: string, outputDir: string) => [],
        },
      },
      environment: {
        GRAPHQL_URL: api.graphqlUrl,
      },
    })
    api.grantMutation(lambda)

    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'functionArn', { value: lambda.functionArn })
    new cdk.CfnOutput(this, 'functionName', { value: lambda.functionName })
  }
}
