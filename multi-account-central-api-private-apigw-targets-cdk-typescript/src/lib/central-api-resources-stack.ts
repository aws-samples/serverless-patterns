import { CfnOutput, Fn, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import {
  AuthorizationType,
  ConnectionType,
  Deployment,
  Integration,
  IntegrationType,
  RestApi,
  VpcLink,
} from 'aws-cdk-lib/aws-apigateway';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { StringParameter } from 'aws-cdk-lib/aws-ssm';
import {
  AwsCustomResource,
  PhysicalResourceId,
} from 'aws-cdk-lib/custom-resources';
import { Construct } from 'constructs';

export interface CentralApiResourcesStackProps extends StackProps {
  svcAUriParamId: string;
  svcAUriParam: string;
  svcBUriParamId: string;
  svcBUriParam: string;
  svcAAccount: string;
  svcBAccount: string;
  stage: string;
}

export class CentralApiResourcesStack extends Stack {
  constructor(
    scope: Construct,
    id: string,
    props: CentralApiResourcesStackProps
  ) {
    super(scope, id, props);

    // Get RestApi from imported value
    const restApi = RestApi.fromRestApiAttributes(this, 'RestApi', {
      restApiId: Fn.importValue('RestApiId'),
      rootResourceId: Fn.importValue('RestApiRootResourceId'),
    });

    // Get VPCLink from imported value
    const vpcLink = VpcLink.fromVpcLinkId(
      this,
      'VpcLink',
      Fn.importValue('VPCLinkId')
    );

    // Get the Application Servce URIs from Parameter Store
    const svcAUriParamArn = `arn:aws:ssm:${this.region}:${props.svcAAccount}:parameter${props.svcAUriParam}`;
    const svcAUri = StringParameter.fromStringParameterArn(
      this,
      `${props.svcAUriParamId}Share`,
      svcAUriParamArn
    );

    const svcBUriParamArn = `arn:aws:ssm:${this.region}:${props.svcBAccount}:parameter${props.svcBUriParam}`;
    const svcBUri = StringParameter.fromStringParameterArn(
      this,
      `${props.svcBUriParamId}Share`,
      svcBUriParamArn
    );

    // Create integrations for each backend application service
    const svcAIntegration = new Integration({
      type: IntegrationType.HTTP_PROXY,
      integrationHttpMethod: 'ANY',
      uri: `${svcAUri.stringValue}{proxy}`,
      options: {
        connectionType: ConnectionType.VPC_LINK,
        vpcLink: vpcLink,
        requestParameters: {
          'integration.request.path.proxy': 'method.request.path.proxy',
        },
      },
    });

    const svcBIntegration = new Integration({
      type: IntegrationType.HTTP_PROXY,
      integrationHttpMethod: 'ANY',
      uri: `${svcBUri.stringValue}{proxy}`,
      options: {
        connectionType: ConnectionType.VPC_LINK,
        vpcLink: vpcLink,
        requestParameters: {
          'integration.request.path.proxy': 'method.request.path.proxy',
        },
      },
    });

    // Define proxy resources for each backend application service
    const svcAResource = restApi.root.addResource('svca');
    svcAResource.addProxy({
      defaultIntegration: svcAIntegration,
      defaultMethodOptions: {
        authorizationType: AuthorizationType.NONE,
        requestParameters: {
          'method.request.path.proxy': true,
        },
      },
      anyMethod: true,
    });

    const svcBResource = restApi.root.addResource('svcb');
    svcBResource.addProxy({
      defaultIntegration: svcBIntegration,
      defaultMethodOptions: {
        authorizationType: AuthorizationType.NONE,
        requestParameters: {
          'method.request.path.proxy': true,
        },
      },
      anyMethod: true,
    });

    // Create a deployment to deploy the new changes to the RestAPI
    const deployment = new Deployment(this, 'Deployment', {
      api: restApi,
      stageName: props.stage,
    });

    deployment.node.addDependency(svcAResource);
    deployment.node.addDependency(svcBResource);

    // AWS Custom Resource to create a new deployment after the integrations and resources are deleted.
    // This is needed so that the deployed stage does not include the integrations and resoruces that were deleted.
    const createDeployment = new AwsCustomResource(this, 'CreateDeployment', {
      onDelete: {
        service: 'ApiGateway',
        action: 'createDeployment',
        parameters: {
          restApiId: restApi.restApiId,
          stageName: props.stage,
        },
        physicalResourceId: PhysicalResourceId.of(Date.now().toString()),
      },
      policy: {
        statements: [
          new PolicyStatement({
            actions: ['apigateway:POST'],
            resources: ['*'],
          }),
        ],
      },
    });

    // When destroying the stack, the API Resources need to be deleted first
    svcAResource.node.addDependency(createDeployment);
    svcBResource.node.addDependency(createDeployment);

    //Outputs
    new CfnOutput(this, 'ServiceAEndpoint', {
      exportName: 'ServiceAEndpoint',
      value: `https://${restApi.restApiId}.execute-api.${this.region}.amazonaws.com/${props.stage}/svca`,
      description: 'Service A API Gateway Endpoint',
    });

    new CfnOutput(this, 'ServiceBEndpoint', {
      exportName: 'ServiceBEndpoint',
      value: `https://${restApi.restApiId}.execute-api.${this.region}.amazonaws.com/${props.stage}/svcb`,
      description: 'Service B API Gateway Endpoint',
    });
  }
}
