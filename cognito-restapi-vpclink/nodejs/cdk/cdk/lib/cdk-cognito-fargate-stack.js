const { Stack, CfnOutput } = require("aws-cdk-lib");
const cognito = require("aws-cdk-lib/aws-cognito");
const ec2 = require("aws-cdk-lib/aws-ec2");
const ecs = require("aws-cdk-lib/aws-ecs");
const ecs_patterns = require("aws-cdk-lib/aws-ecs-patterns");
const apigateway = require("aws-cdk-lib/aws-apigateway");
const iam = require("aws-cdk-lib/aws-iam");
const logs = require("aws-cdk-lib/aws-logs");

class CdkCognitoFargateStack extends Stack {
  /**
   *
   * @param {Construct} scope
   * @param {string} id
   * @param {StackProps} props
   */
  constructor(scope, id, props) {
    super(scope, id, props);

    const pool = new cognito.UserPool(this, "UserPool", {
      signInAliases: {
        username: true,
        email: false,
        phone: false
      }
    });

    const domain = pool.addDomain("CognitoDomain", {
      cognitoDomain: {
        domainPrefix: "demo"
      }
    });

    const readOnlyScope = new cognito.ResourceServerScope({
      scopeName: "read",
      scopeDescription: "Read-only access"
    });
    const fullAccessScope = new cognito.ResourceServerScope({
      scopeName: "*",
      scopeDescription: "Full access"
    });

    const userServer = pool.addResourceServer("ResourceServer", {
      identifier: "finsys",
      scopes: [ readOnlyScope, fullAccessScope ],
    });

    const readOnlyClient = pool.addClient("read-only-client", {
      authFlows: {
        adminUserPassword: true
      },
      generateSecret: true,
      oAuth: {
        scopes: [
          cognito.OAuthScope.resourceServer(userServer, readOnlyScope)
        ],
        flows: {
          implicitCodeGrant: false,
          clientCredentials: true,
          authorizationCodeGrant: false
        }
      }
    });

    const fullAccessClient = pool.addClient("full-access-client", {
      authFlows: {
        adminUserPassword: true
      },
      generateSecret: true,
      oAuth: {
        scopes: [
          cognito.OAuthScope.resourceServer(userServer, readOnlyScope),
          cognito.OAuthScope.resourceServer(userServer, fullAccessScope)
        ],
        flows: {
          implicitCodeGrant: false,
          clientCredentials: true,
          authorizationCodeGrant: false
        }
      }
    });

    const vpc = new ec2.Vpc(this, "Vpc", {
      maxAzs: 2
    });

    const cluster = new ecs.Cluster(this, "Cluster", {
      vpc: vpc
    });

    const service = new ecs_patterns.NetworkLoadBalancedFargateService(this, "FargateService", {
      assignPublicIp: false,
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      circuitBreaker: {
        rollback: true
      },
      taskImageOptions: {
        image: ecs.ContainerImage.fromRegistry("amazon/amazon-ecs-sample")
      },
      memoryLimitMiB: 1024,
      publicLoadBalancer: false,
      recordType: ecs_patterns.NetworkLoadBalancedServiceRecordType.ALIAS
    });

    service.targetGroup.setAttribute("deregistration_delay.timeout_seconds", "0");
    service.service.connections.allowFrom(
      ec2.Peer.ipv4("10.0.0.0/16"),
      ec2.Port.tcp(80),
      "from 10.0.0.0/16:80"
    );

    const vpcEndpoint = new ec2.InterfaceVpcEndpoint(this, "ApiVpcEndpoint", {
      vpc,
      service: ec2.InterfaceVpcEndpointAwsService.APIGATEWAY,
      subnets: {
        subnets: vpc.privateSubnets
      },
      privateDnsEnabled: true
    });

    const logGroup = new logs.LogGroup(this, "ApiGatewayAccessLogs");

    const api = new apigateway.RestApi(this, "PrivateRestApi", {
      disableExecuteApiEndpoint: false,
      cloudWatchRole: true,
      deployOptions: {
        accessLogDestination: new apigateway.LogGroupLogDestination(logGroup),
        accessLogFormat: apigateway.AccessLogFormat.jsonWithStandardFields(),
        dataTraceEnabled: true,
        tracingEnabled: true
      },
      endpointConfiguration: {
        types: [apigateway.EndpointType.PRIVATE],
        vpcEndpoints: [vpcEndpoint]
      },
      policy: new iam.PolicyDocument({
        statements: [
          new iam.PolicyStatement({
            principals: [new iam.AnyPrincipal],
            actions: ["execute-api:Invoke"],
            resources: ["execute-api:/*"],
            effect: iam.Effect.DENY,
            conditions: {
              StringNotEquals: {
                "aws:SourceVpce": vpcEndpoint.vpcEndpointId
              }
            }
          }),
          new iam.PolicyStatement({
            principals: [new iam.AnyPrincipal],
            actions: ["execute-api:Invoke"],
            resources: ["execute-api:/*"],
            effect: iam.Effect.ALLOW
          })
        ]
      })
    });

    const link = new apigateway.VpcLink(this, "VpcLink", {
      targets: [service.loadBalancer]
    });
    
    const auth = new apigateway.CognitoUserPoolsAuthorizer(this, "Authorizer", {
      cognitoUserPools: [pool]
    });

    api.root.defaultIntegration = new apigateway.HttpIntegration(`http://${service.loadBalancer.loadBalancerDnsName}/`, {
      httpMethod: "ANY",
      options: {
        connectionType: apigateway.ConnectionType.VPC_LINK,
        vpcLink: link,
      }
    });

    api.root.defaultMethodOptions = {
      authorizer: auth,
      authorizationType: apigateway.AuthorizationType.COGNITO,
      authorizationScopes: [ "finsys/*" ],
    }

    api.root.addMethod("ANY");

    api.root.addMethod("GET", null, {
      authorizationScopes: [ "finsys/*", "finsys/read" ],
    });

    const proxy = api.root.addProxy({
      defaultIntegration: new apigateway.HttpIntegration(`http://${service.loadBalancer.loadBalancerDnsName}/{proxy}`, {
        httpMethod: "ANY",
        options: {
          connectionType: apigateway.ConnectionType.VPC_LINK,
          vpcLink: link,
          requestParameters: {
            "integration.request.path.proxy": "method.request.path.proxy"
          }
        }
      }),
      defaultMethodOptions: {
        authorizer: auth,
        authorizationType: apigateway.AuthorizationType.COGNITO,
        authorizationScopes: [ "finsys/*" ],
        requestParameters: {
          "method.request.path.proxy": true
        }
      }
    });

    proxy.addMethod("GET", null, {
      authorizationScopes: [ "finsys/*", "finsys/read" ],
    });

    new CfnOutput(this, "CognitoDomain", { value: `https://${domain.domainName}.auth.${this.region}.amazoncognito.com`});
    new CfnOutput(this, "PrivateRestApiEndpoint", { value: `https://${api.restApiId}-${vpcEndpoint.vpcEndpointId}.execute-api.${this.region}.amazonaws.com/prod`});
    new CfnOutput(this, "ReadOnlyClientId", { value: readOnlyClient.userPoolClientId });
    new CfnOutput(this, "ReadOnlyClientSecret", { value: readOnlyClient.userPoolClientSecret.unsafeUnwrap() });
    new CfnOutput(this, "FullAccessClientId", { value: fullAccessClient.userPoolClientId });
    new CfnOutput(this, "FullAccessClientSecret", { value: fullAccessClient.userPoolClientSecret.unsafeUnwrap() });
  }
}

module.exports = { CdkCognitoFargateStack }
