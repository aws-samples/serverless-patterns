import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as ecr from 'aws-cdk-lib/aws-ecr';
import * as opensearchserverless from 'aws-cdk-lib/aws-opensearchserverless';

export class AgentcoreOpensearchStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const collectionName = 'agentcore-search';
    const collectionGroupName = 'agentcore-search-group';

    // OpenSearch Serverless NextGen Collection Group
    const collectionGroup = new opensearchserverless.CfnCollectionGroup(this, 'CollectionGroup', {
      name: collectionGroupName,
      description: 'NextGen collection group for AgentCore search',
      standbyReplicas: 'DISABLED',
    });
    // CollectionGroup itself implies NextGen architecture

    // Encryption policy
    const encryptionPolicy = new opensearchserverless.CfnSecurityPolicy(this, 'EncryptionPolicy', {
      name: 'agentcore-search-enc',
      type: 'encryption',
      policy: JSON.stringify({
        Rules: [{ ResourceType: 'collection', Resource: [`collection/${collectionName}`] }],
        AWSOwnedKey: true,
      }),
    });

    // Network policy
    const networkPolicy = new opensearchserverless.CfnSecurityPolicy(this, 'NetworkPolicy', {
      name: 'agentcore-search-net',
      type: 'network',
      policy: JSON.stringify([{
        Rules: [
          { ResourceType: 'collection', Resource: [`collection/${collectionName}`] },
          { ResourceType: 'dashboard', Resource: [`collection/${collectionName}`] },
        ],
        AllowFromPublic: true,
      }]),
    });

    // OpenSearch Serverless Collection
    const collection = new opensearchserverless.CfnCollection(this, 'Collection', {
      name: collectionName,
      type: 'SEARCH',
      description: 'Search collection for AgentCore agent',
    });
    collection.addDependency(encryptionPolicy);
    collection.addDependency(networkPolicy);
    collection.addDependency(collectionGroup);

    // ECR Repository (pre-created, imported)
    const ecrRepo = ecr.Repository.fromRepositoryName(this, 'AgentEcrRepo', 'agentcore-opensearch-agent');

    // IAM Role for AgentCore Runtime (inlinePolicies ensures permissions exist before AgentCore validates)
    const runtimeRole = new iam.Role(this, 'AgentCoreRuntimeRole', {
      assumedBy: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com'),
      description: 'Role for AgentCore Runtime to access Bedrock and OpenSearch',
      inlinePolicies: {
        AgentCorePermissions: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: ['bedrock:InvokeModel'],
              resources: ['arn:aws:bedrock:*::foundation-model/*'],
            }),
            new iam.PolicyStatement({
              actions: ['aoss:APIAccessAll'],
              resources: ['*'],
            }),
            new iam.PolicyStatement({
              actions: ['ecr:GetAuthorizationToken'],
              resources: ['*'],
            }),
            new iam.PolicyStatement({
              actions: ['ecr:BatchGetImage', 'ecr:GetDownloadUrlForLayer'],
              resources: [ecrRepo.repositoryArn],
            }),
          ],
        }),
      },
    });

    // Data access policy
    new opensearchserverless.CfnAccessPolicy(this, 'DataAccessPolicy', {
      name: 'agentcore-search-access',
      type: 'data',
      policy: JSON.stringify([{
        Rules: [
          { ResourceType: 'collection', Resource: [`collection/${collectionName}`], Permission: ['aoss:*'] },
          { ResourceType: 'index', Resource: [`index/${collectionName}/*`], Permission: ['aoss:*'] },
        ],
        Principal: [runtimeRole.roleArn],
      }]),
    });

    // AgentCore Runtime
    const containerUri = cdk.Fn.sub(
      '${AWS::AccountId}.dkr.ecr.${AWS::Region}.amazonaws.com/agentcore-opensearch-agent:latest'
    );

    new cdk.CfnResource(this, 'AgentCoreRuntime', {
      type: 'AWS::BedrockAgentCore::Runtime',
      properties: {
        AgentRuntimeName: 'agentcore_opensearch_agent',
        AgentRuntimeArtifact: {
          ContainerConfiguration: {
            ContainerUri: containerUri,
          },
        },
        NetworkConfiguration: {
          NetworkMode: 'PUBLIC',
        },
        RoleArn: runtimeRole.roleArn,
      },
    });

    // Outputs
    new cdk.CfnOutput(this, 'CollectionEndpoint', {
      value: collection.attrCollectionEndpoint,
      description: 'OpenSearch Serverless Collection Endpoint',
    });

    new cdk.CfnOutput(this, 'EcrRepositoryUri', {
      value: ecrRepo.repositoryUri,
      description: 'ECR Repository URI for agent Docker image',
    });
  }
}
