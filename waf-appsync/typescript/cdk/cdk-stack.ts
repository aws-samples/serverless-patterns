import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";

import * as appsync from "@aws-cdk/aws-appsync-alpha";
import * as waf from "aws-cdk-lib/aws-wafv2";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // AppSync graphql API with dynamodb resolvers using L2 alpha construct
    const api = new appsync.GraphqlApi(this, "DemoApi", {
      name: "demo",
      schema: appsync.Schema.fromAsset("schema.graphql"),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.API_KEY,
          apiKeyConfig: {
            expires: cdk.Expiration.after(cdk.Duration.days(30)),
            name: "API Key",
          },
        },
      },
    });

    const demoTable = new dynamodb.Table(this, "DemoTable", {
      partitionKey: {
        name: "id",
        type: dynamodb.AttributeType.STRING,
      },
    });

    const demoDS = api.addDynamoDbDataSource("DemoDataSource", demoTable);

    // Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
    demoDS.createResolver({
      typeName: "Query",
      fieldName: "getDemos",
      requestMappingTemplate: appsync.MappingTemplate.dynamoDbScanTable(),
      responseMappingTemplate: appsync.MappingTemplate.dynamoDbResultList(),
    });

    // Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
    demoDS.createResolver({
      typeName: "Mutation",
      fieldName: "addDemo",
      requestMappingTemplate: appsync.MappingTemplate.dynamoDbPutItem(
        appsync.PrimaryKey.partition("id").auto(),
        appsync.Values.projecting("input")
      ),
      responseMappingTemplate: appsync.MappingTemplate.dynamoDbResultItem(),
    });

    // WAF2 WebACL with managed rule set for IP reputation list and a custom rule to block graphql schema introspection queries
    const webAcl = new waf.CfnWebACL(this, "DemoWebACL", {
      defaultAction: { allow: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: "demo-waf",
        sampledRequestsEnabled: false,
      },
      scope: "REGIONAL",
      rules: [
        {
          name: "AWS-AWSManagedRulesAmazonIpReputationList",
          priority: 10,
          statement: {
            managedRuleGroupStatement: {
              vendorName: "AWS",
              name: "AWSManagedRulesAmazonIpReputationList",
            },
          },
          overrideAction: {
            none: {},
          },
          visibilityConfig: {
            sampledRequestsEnabled: true,
            cloudWatchMetricsEnabled: true,
            metricName: "AWSManagedRulesAmazonIpReputationList",
          },
        },
        {
          name: "GraphQLIntrospection",
          priority: 2,
          action: {
            block: {},
          },
          visibilityConfig: {
            sampledRequestsEnabled: true,
            cloudWatchMetricsEnabled: true,
            metricName: "BodyGraphQLIntrospectionRule",
          },
          statement: {
            byteMatchStatement: {
              fieldToMatch: { body: { oversizeHandling: "CONTINUE" } },
              searchString: "__schema",
              positionalConstraint: "CONTAINS",
              textTransformations: [{ priority: 0, type: "LOWERCASE" }],
            },
          },
        },
      ],
    });

    // WebACL association with AppSync GraphQL API.
    new waf.CfnWebACLAssociation(this, "DemoWebACLAssociation", {
      webAclArn: webAcl.attrArn,
      resourceArn: api.arn,
    });
  }
}
