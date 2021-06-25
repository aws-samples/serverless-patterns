import * as cdk from '@aws-cdk/core';
import { GraphqlApi, Schema, FieldLogLevel, AuthorizationType, MappingTemplate } from '@aws-cdk/aws-appsync';
import { Role, ServicePrincipal, PolicyStatement } from "@aws-cdk/aws-iam";
import {EventBus} from "@aws-cdk/aws-events";
import { join } from 'path';

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
    const httpdatasource = api.addHttpDataSource('events', endpoint, {
      authorizationConfig: { signingRegion: this.region, signingServiceName: 'events' },
    });
    eventBus.grantPutEventsTo(httpdatasource.grantPrincipal);

    httpdatasource.createResolver({
      typeName: 'Mutation',
      fieldName: 'putEvent',
      requestMappingTemplate: MappingTemplate.fromFile(join(__dirname, 'request.vtl')),
      responseMappingTemplate: MappingTemplate.fromFile(join(__dirname, 'response.vtl'))
    })

    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'eventBus', {value: eventBus.eventBusArn})
  }
}
