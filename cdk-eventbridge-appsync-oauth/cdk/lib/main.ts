import { Stack, StackProps, CfnParameter, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { GraphqlApi, Schema, MappingTemplate, AuthorizationType } from '@aws-cdk/aws-appsync-alpha'
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha'
import { Runtime } from 'aws-cdk-lib/aws-lambda'
import { aws_events as Events } from 'aws-cdk-lib'
import { aws_iam as IAM } from 'aws-cdk-lib'
import { join } from 'path'
import { Auth } from './auth'

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

    const authDomainParameter = new CfnParameter(this, "authDomainName", {
      type: "String",
      description: "Unique domain name for auth"
    })

    const auth = new Auth(this, "Auth", {
      authDomainPrefix: authDomainParameter.valueAsString
    });

    const authorizerFunction = new PythonFunction(this, "AuthorizerFunction", {
      entry: join(__dirname, "authorizer"),
      index: "app.py",
      runtime: Runtime.PYTHON_3_8,
      environment: {
        USER_POOL_ID: auth.userPoolId,
        APP_CLIENT_ID: auth.destinationClientId
      }
    })

    const api = new GraphqlApi(this, 'Api', {
      name: 'TriggeredByEventBridge',
      schema: Schema.fromAsset(join(__dirname, 'schema.graphql')),
      authorizationConfig: {
        // for the time being, use API key for default
        defaultAuthorization: {
          authorizationType: AuthorizationType.API_KEY,
        },
        additionalAuthorizationModes: [
          {
            authorizationType: AuthorizationType.LAMBDA,
            lambdaAuthorizerConfig: {
              handler: authorizerFunction
            }
          }
        ]
      }
    }) 

    authorizerFunction.addPermission("AppSyncInvokeLambdaPermission", {
      principal: new IAM.ServicePrincipal("appsync.amazonaws.com"),
      sourceArn: api.arn,
      sourceAccount: process.env.CDK_DEPLOYED_ACCOUNT || process.env.CDK_DEFAULT_ACCOUNT
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
      authorizationType: "OAUTH_CLIENT_CREDENTIALS",
      authParameters: {
        oAuthParameters: {
          authorizationEndpoint: `${auth.authEndpoint}/oauth2/token`,
          clientParameters: {
            clientId: auth.destinationClientId,
            clientSecret: auth.destinationClientSecret
          },
          httpMethod: "POST",
          oAuthHttpParameters: {
            bodyParameters: [
              {
                key: "grant_type",
                value: "client_credentials"
              }
            ]
          }
        }
      }
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
  }
}
