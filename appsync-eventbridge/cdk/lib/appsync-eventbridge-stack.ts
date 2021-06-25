import * as cdk from '@aws-cdk/core';
import { GraphqlApi, Schema, FieldLogLevel, AuthorizationType, CfnDataSource, CfnResolver, MappingTemplate } from '@aws-cdk/aws-appsync';
import { Role, ServicePrincipal, PolicyStatement } from "@aws-cdk/aws-iam";
import {EventBus} from "@aws-cdk/aws-events";
import { join } from 'path'

export class AppsyncEventbridgeStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const eventBus = new EventBus(this, 'bus', {
      eventBusName: 'AppSyncEventBus'
    });

    const api = new GraphqlApi(this, 'Api', {
      name: 'AppSyncEventBridgeAPI',
      schema: Schema.fromAsset(join(__dirname, 'schema.graphql')),
      xrayEnabled: true,
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: FieldLogLevel.ALL,
      },
    });

    const appsyncEventBridgeRole = new Role(this, "AppSyncEventBridgeRole", {
      assumedBy: new ServicePrincipal("appsync.amazonaws.com")
    });
    appsyncEventBridgeRole.addToPolicy(
      new PolicyStatement({
        resources: ["*"],
        actions: ["events:PutEvents"]
      })
    );
    const endpoint = "https://events." + this.region + ".amazonaws.com/";
    const httpdatasource = new CfnDataSource(this, 'httpdatasource', {
        apiId: api.apiId,
        name: "EventBridgeDataSource",
        type: "HTTP",
        httpConfig:{
          authorizationConfig: {
            authorizationType: "AWS_IAM",
              awsIamConfig: {
                signingRegion: this.region,
                signingServiceName: "events"
              }
          },
          endpoint: "https://events." + this.region + ".amazonaws.com/",
        },
        serviceRoleArn: appsyncEventBridgeRole.roleArn
      }
    );
    //const datasource = api.addHttpDataSource(id: 'EventBridgeDataSource', endpoint: endpoint, );

    const putEventResolver = new CfnResolver(this, "PutEventMutationResolver", {
      apiId: api.apiId,
      typeName: "Mutation",
      fieldName: "putEvent",
      dataSourceName: httpdatasource.name,
      requestMappingTemplate: `{
        "version": "2018-05-29",
        "method": "POST",
        "resourcePath": "/",
        "params": {
          "headers": {
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target":"AWSEvents.PutEvents"
          },
          "body": {
            "Entries":[
              {
                "Source":"appsync",
                "EventBusName": "default",
                "Detail":"{ \\\"event\\\": \\\"$ctx.arguments.event\\\"}",
                "DetailType":"Event Bridge via GraphQL"
               }
            ]
          }
        }
      }`,
      responseMappingTemplate: `## Raise a GraphQL field error in case of a datasource invocation error
      #if($ctx.error)
        $util.error($ctx.error.message, $ctx.error.type)
      #end
      ## if the response status code is not 200, then return an error. Else return the body **
      #if($ctx.result.statusCode == 200)
          ## If response is 200, return the body.
          {
            "result": "$util.parseJson($ctx.result.body)"
          }
      #else
          ## If response is not 200, append the response to error block.
          $utils.appendError($ctx.result.body, $ctx.result.statusCode)
      #end`
    });
    putEventResolver.addDependsOn(httpdatasource);

    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'eventBus', {value: eventBus.eventBusArn})
  }
}
