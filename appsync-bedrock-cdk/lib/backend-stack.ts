import * as cdk from 'aws-cdk-lib';
import { GraphqlApi, SchemaFile, AuthorizationType, FieldLogLevel, AppsyncFunction, Code, FunctionRuntime, Resolver } from 'aws-cdk-lib/aws-appsync';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class BackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const api = new GraphqlApi(this, 'Api', {
      name: 'AppsyncBedrockApi',
      schema: SchemaFile.fromAsset("src/api/schema.gql"),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: AuthorizationType.API_KEY
        }
      },
      xrayEnabled: true,
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: FieldLogLevel.ALL
      },
    })

    const bedrockDataSource = api.addHttpDataSource('BedrockDataSource', `https://bedrock-runtime.${this.region}.amazonaws.com`, {
      authorizationConfig: {
        signingRegion: this.region,
        signingServiceName: 'bedrock'
      },
    })

    bedrockDataSource.grantPrincipal.addToPrincipalPolicy(new PolicyStatement({
      actions: ["bedrock:*"],
      resources: ["*"]
    }))

    const invokeModelFunction = new AppsyncFunction(this, 'InvokeModelFunction', {
      api: api,
      dataSource: bedrockDataSource,
      name: 'invokeModelFunction',
      runtime: FunctionRuntime.JS_1_0_0,
      code: Code.fromAsset("src/api/mappings/Mutation.invokeModel.js")
    })


    const invokeResolver = new Resolver(this, "InvokeResolver", {
      api: api,
      typeName: 'Mutation',
      fieldName: 'invoke',
      runtime: FunctionRuntime.JS_1_0_0,
      pipelineConfig: [invokeModelFunction],
      code: Code.fromInline(`
        // Before
        export function request(...args) {
          console.log(args);
          return {}
        }

        // After
        export function response(ctx) {
          return ctx.prev.result
        }
      `)
    })

    new cdk.CfnOutput(this, "GraphQLApiURL", {
      value: api.graphqlUrl
    })
    new cdk.CfnOutput(this, "GraphQLApiKey", {
      value: api.apiKey || ""
    })
    new cdk.CfnOutput(this, "GraphQLApiID", {
      value: api.apiId
    })
    new cdk.CfnOutput(this, "Region", {
      value: this.region
    })
  }
}
