import { Stack, StackProps, CfnOutput } from "aws-cdk-lib";
import * as appsync from "aws-cdk-lib/aws-appsync";
import * as iam from "aws-cdk-lib/aws-iam";
import { EventBus } from "aws-cdk-lib/aws-events";
import { Construct } from "constructs";
import { readFileSync } from "fs";

export class AppSyncEventBridgeStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);


    // Create Event bus
    const eventBus = new EventBus(this, 'bus', {
      eventBusName: 'CustomEventBus'
    });

    // AppSync stack
    const appSyncApi = this.createAppSyncStack();

    // Event resolver
    this.eventBridgeResolver(appSyncApi, eventBus);


    new CfnOutput(this, 'AppsyncGraphqlUrl', {
      value: appSyncApi.graphqlUrl,
      description: 'The Appsync Stack graphqlUrl',
      exportName: 'GraphqlUrl',
    });

    new CfnOutput(this, 'AppsyncApiKey', {
      value: appSyncApi.apiKey ? appSyncApi.apiKey : "Undefined",
      description: 'The Appsync ApiKey',
      exportName: 'ApiKey',
    });


  }

  private createAppSyncStack() {
    return new appsync.GraphqlApi(this, "AppSyncEventBridgeAPI", {
      name: "AppSyncEventBridgeAPI",
      schema: appsync.SchemaFile.fromAsset("graphql/schema.graphql"),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.IAM,
        },
        additionalAuthorizationModes: [
          {
            authorizationType: appsync.AuthorizationType.API_KEY,
          },
        ],
      },
      xrayEnabled: false,
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: appsync.FieldLogLevel.ALL,
      },
    });
  }

  private eventBridgeResolver(api: appsync.GraphqlApi, eventBus: EventBus) {

    const eventsDataSource = this.createCfEventBridgeDataSource(
      api,
      eventBus,
      "EventBridgeDataSource"
    );

    //Put Event Resolver
    const cfnFunctionConfiguration = new appsync.CfnFunctionConfiguration(
      this,
      "EventBridgePutEventFunction",
      {
        apiId: api.apiId,
        dataSourceName: eventsDataSource.name,
        name: "PutEventFunction",
        code: readFileSync('graphql/function/putEvent.js').toString(),
        runtime: {
          name: "APPSYNC_JS",
          runtimeVersion: "1.0.0",
        },
      }
    );

    cfnFunctionConfiguration.addDependency(eventsDataSource);

    return new appsync.CfnResolver(this, "EventBridgePipelineResolver", {
      apiId: api.apiId,
      typeName: "Mutation",
      fieldName: "putEvent",
      kind: "PIPELINE",
      code: readFileSync("graphql/resolver/getPipelineResolver.js").toString(),
      pipelineConfig: {
        functions: [cfnFunctionConfiguration.attrFunctionId],
      },
      runtime: {
        name: "APPSYNC_JS",
        runtimeVersion: "1.0.0",
      },
    });
  }

  private createCfEventBridgeDataSource(
    api: appsync.GraphqlApi,
    eventBus: EventBus,
    dataSourceName: string
  ) {
    const role = new iam.Role(
      this,
      "AppSyncEventBridgeDataSourceRole",
      {
        roleName: "appsync-api-eventbridge-datasource",
        assumedBy: new iam.ServicePrincipal("appsync.amazonaws.com"),
      }
    );
    role.addToPolicy(
      new iam.PolicyStatement({
        resources: [eventBus.eventBusArn],
        actions: ["events:PutEvents"],
      })
    );
    return new appsync.CfnDataSource(this, dataSourceName, {
      apiId: api.apiId,
      name: "EventBridgeDataSource",
      type: "AMAZON_EVENTBRIDGE",
      eventBridgeConfig: {
        eventBusArn: eventBus.eventBusArn,
      },
      serviceRoleArn: role.roleArn,
    });
  }
}
