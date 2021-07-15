import * as cdk from '@aws-cdk/core'
import { GraphqlApi, Schema, MappingTemplate, AuthorizationType } from '@aws-cdk/aws-appsync'
import * as Events from '@aws-cdk/aws-events'
import * as IAM from '@aws-cdk/aws-iam'
import { join } from 'path'

const requestTemplate = `
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
      name: 'TriggeredByEventBridge',
      schema: Schema.fromAsset(join(__dirname, 'schema.graphql')),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: AuthorizationType.API_KEY,
        },
      },
    })

    const noneDS = api.addNoneDataSource('NONE')
    noneDS.createResolver({
      typeName: 'Mutation',
      fieldName: 'updateTodo',
      requestMappingTemplate: MappingTemplate.fromString(requestTemplate),
      responseMappingTemplate: MappingTemplate.fromString(responseTemplate),
    })

    const bus = new Events.CfnEventBus(this, 'bus', { name: 'todos' })

    const connection = new Events.CfnConnection(this, 'connection', {
      authorizationType: 'API_KEY',
      authParameters: {
        ApiKeyAuthParameters: {
          ApiKeyName: 'x-api-key',
          ApiKeyValue: api.apiKey!,
        },
      },
    })

    const destination = new Events.CfnApiDestination(this, 'destination', {
      connectionArn: connection.attrArn,
      httpMethod: 'POST',
      invocationEndpoint: api.graphqlUrl,
    })

    const role = new IAM.Role(this, 'role', {
      assumedBy: new IAM.ServicePrincipal('events.amazonaws.com'),
      inlinePolicies: {
        invokeAPI: new IAM.PolicyDocument({
          statements: [
            new IAM.PolicyStatement({
              resources: [`arn:aws:events:${this.region}:${this.account}:api-destination/${destination.ref}/*`],
              actions: ['events:InvokeApiDestination'],
            }),
          ],
        }),
      },
    })

    const rule = new Events.CfnRule(this, 'rule', {
      name: 'default-todo-rule',
      eventBusName: bus.attrName,
      eventPattern: {
        source: ['todos.system'],
        'detail-type': ['todos update'],
      },
      targets: [
        {
          id: 'default-target-appsync',
          arn: destination.attrArn,
          roleArn: role.roleArn,
          inputTransformer: {
            inputPathsMap: {
              id: '$.detail.todo-id',
              name: '$.detail.name',
              description: '$.detail.description',
            },
            inputTemplate: `{
              "query": "mutation UpdateTodo($id:ID!, $name:String, $description:String) {
                updateTodo(id:$id, name:$name, description:$description) { id name description createdAt updatedAt }
              }",
              "variables": {
                "id": "<id>",
                "name": "<name>",
                "description": "<description>"
              }
            }`.replace(/\n\s*/g, ' '),
          },
        },
      ],
    })
    rule.addDependsOn(bus)

    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new cdk.CfnOutput(this, 'busName', { value: bus.attrName })
  }
}
