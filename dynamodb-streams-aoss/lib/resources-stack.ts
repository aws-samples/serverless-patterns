import { Stack, StackProps, RemovalPolicy, Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Table, BillingMode, AttributeType, StreamViewType } from 'aws-cdk-lib/aws-dynamodb';
import { Function, Runtime, Code, StartingPosition, LayerVersion } from 'aws-cdk-lib/aws-lambda';
import { DynamoEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import { Role, ServicePrincipal, ManagedPolicy, PolicyStatement, Effect} from 'aws-cdk-lib/aws-iam';
import * as opensearchserverless from 'aws-cdk-lib/aws-opensearchserverless';

export class ResourcesStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);


    const userTable = new Table(this, "UserTable", {
      tableName: "table-opensearch",
      billingMode: BillingMode.PAY_PER_REQUEST,
      partitionKey: {name: "partitionKey", type: AttributeType.STRING},
      sortKey: {name: "sortKey", type: AttributeType.STRING},
      pointInTimeRecovery: true,
      stream: StreamViewType.NEW_IMAGE // This is the important line!
    });

    const lambdaExecRole = new Role(this, "lambdaExecRole", {
      assumedBy: new ServicePrincipal("lambda.amazonaws.com"),
      managedPolicies: [
        ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole")
      ]  
    })

    // build lambda execution role with full API access to AWS OpenSearch Serverless
    const lambdaExecRoleAossAccessPolicy = new PolicyStatement( {
      effect: Effect.ALLOW,
      actions: ['aoss:APIAccessAll',
        'aoss:BatchGetCollection',
        'aoss:List*'
      ],
      resources: ['*']
    });
    lambdaExecRole.addToPolicy(lambdaExecRoleAossAccessPolicy);

    const cfnCollection = new opensearchserverless.CfnCollection(this, 'MyCfnCollection', {
      name: "serverless-collection",
      type: "SEARCH"
    });


    const opensearchDataAccessPolicy = [
      {
        "Rules": [
          {
            "Resource": [
              "collection/serverless-collection"
            ],
            "Permission": [
              "aoss:CreateCollectionItems",
              "aoss:DeleteCollectionItems",
              "aoss:UpdateCollectionItems",
              "aoss:DescribeCollectionItems"
            ],
            "ResourceType": "collection"
          },
          {
            "Resource": [
              "index/serverless-collection/*"
            ],
            "Permission": [
              "aoss:CreateIndex",
              "aoss:DeleteIndex",
              "aoss:UpdateIndex",
              "aoss:DescribeIndex",
              "aoss:ReadDocument",
              "aoss:WriteDocument"
            ],
            "ResourceType": "index"
          }
        ],
        "Principal": [
          lambdaExecRole.roleArn
        ],
        "Description": "Rule 1"
      }
    ];

    const opensearchSecurityPolicy = [{
      "Rules":[
        {
          "ResourceType":"collection",
          "Resource":[
            "collection/serverless-collection"
          ]
        }, 
        {
          "ResourceType":"dashboard",
          "Resource":[
            "collection/serverless-collection"
          ]
        }
      ],
      "AllowFromPublic":true
    }];

    const opensearchEncryptionPolicy = {
      "Rules":[
        {
          "ResourceType":"collection",
          "Resource":[
            "collection/serverless-collection"
          ]
        }
      ],
      "AWSOwnedKey":true
    };

    const cfnAccessPolicy = new opensearchserverless.CfnAccessPolicy(this, 'MyCfnAccessPolicy', {
      name: 'accesspolicy',
      policy: JSON.stringify(opensearchDataAccessPolicy),
      type: 'data',
      description: 'description',
    });

    const cfnSecurityPolicy = new opensearchserverless.CfnSecurityPolicy(this, 'MyCfnSecurityPolicy', {
      name: 'securitypolicy',
      policy: JSON.stringify(opensearchSecurityPolicy),
      type: 'network',
      description: 'description',
    });

    const cfnEncryptionPolicy = new opensearchserverless.CfnSecurityPolicy(this, "MyCfnEncryptionPolicy",{
      name: "encryptionpolicy",
      policy: JSON.stringify(opensearchEncryptionPolicy),
      type: "encryption",
    });
    
    cfnCollection.addDependency(cfnAccessPolicy);
    cfnCollection.addDependency(cfnSecurityPolicy);
    cfnCollection.addDependency(cfnEncryptionPolicy);


    const layer = new LayerVersion(this, 'opensearchpy', {
      code: Code.fromAsset('./resources/layers/opensearchpy'),
      description: 'urllib3<2, opensearch-py',
      compatibleRuntimes: [Runtime.PYTHON_3_10],
      removalPolicy: RemovalPolicy.DESTROY
    });

    const userTableIndexingFunction = new Function(this, "UserTableIndexingFunction", {
      code: Code.fromAsset("./resources/lambda"),
      runtime: Runtime.PYTHON_3_10,
      handler: "app.handler",
      timeout: Duration.seconds(30),
      environment: {
        "AOSS_ENDPOINT": cfnCollection.attrCollectionEndpoint,
      },
      role: lambdaExecRole,
      layers: [layer]
    });

    userTableIndexingFunction.addEventSource(new DynamoEventSource(userTable, {
      startingPosition: StartingPosition.TRIM_HORIZON,
      batchSize: 1,
      retryAttempts: 3
    }));    
  };
  
}
