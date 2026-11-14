import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { GraphqlApi, Schema, MappingTemplate, AuthorizationType } from '@aws-cdk/aws-appsync-alpha';
import { aws_events as Events } from 'aws-cdk-lib';
import {aws_iam as IAM } from 'aws-cdk-lib';
import { join } from 'path';

const requestTemplate = `
#set( $createdAt = $util.time.nowISO8601() )
$util.qr($context.args.put("createdAt", $createdAt))
$util.qr($context.args.put("updatedAt", $createdAt))
{
  "version": "2017-02-28",
  "payload": $util.toJson($ctx.args)
}`

const responseTemplate = `$util.toJson($context.result)`

export class MainStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
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
        apiKeyAuthParameters: {
          apiKeyName: 'x-api-key',
          apiKeyValue: api.apiKey!,
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

    new CfnOutput(this, 'apiId', { value: api.apiId })
    new CfnOutput(this, 'apiName', { value: api.name })
    new CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new CfnOutput(this, 'busName', { value: bus.attrName })
  }
}
