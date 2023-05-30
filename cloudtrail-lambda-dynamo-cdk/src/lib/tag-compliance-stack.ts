import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudtrail from 'aws-cdk-lib/aws-cloudtrail';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as eventsources from 'aws-cdk-lib/aws-lambda-event-sources';

export class TagComplianceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Aws.REGION;
    const accountId = cdk.Aws.ACCOUNT_ID;

    const table = new dynamodb.Table(this, 'resourceCreationTable', {
      tableName: 'resource-creation-table',
      partitionKey: {
        name: 'resource_arn', // name may be changed
        type: dynamodb.AttributeType.STRING
      },
      stream: dynamodb.StreamViewType.NEW_IMAGE,
      removalPolicy: cdk.RemovalPolicy.DESTROY // can be adjusted as deemed necessary
    });

    // random generated number appended to bucket name, to create unique name
    const generatedNum = Math.ceil(Math.random() * 10);

    const bucket = new s3.Bucket(this, 'resourceCreationLogs', {
      bucketName: `resource-creation-logs-${generatedNum}`, // name may be changed, need to make sure bucket name already doesn't exist
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true
    });

    const cloudtrailPrincipal = new iam.ServicePrincipal("cloudtrail.amazonaws.com");

    // policy that allows cloudtrail to store logs in the s3 bucket created
    const bucket_policy_statements = [
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        principals: [cloudtrailPrincipal],
        actions:["s3:GetBucketAcl"],
        resources:[bucket.bucketArn],
      }),
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        principals:[cloudtrailPrincipal],
        actions:["s3:PutObject"],
        resources: [bucket.arnForObjects(`AWSLogs/*`)],
        conditions: {
          "StringEquals": {
            "s3:x-amz-acl": "bucket-owner-full-control"
          }
        }
      })
    ]

    // adding the IAM statements to the bucket policy
    for(const statement of bucket_policy_statements) {
      bucket.addToResourcePolicy(statement);
    }

    new cloudtrail.Trail(this, 'resourceCreationTrail', {
      trailName: 'resource-creation-trail',
      bucket: bucket,
      isMultiRegionTrail: true,
      includeGlobalServiceEvents: true,
      managementEvents: cloudtrail.ReadWriteType.WRITE_ONLY
    });

    // function that gets cloudtrail events from the s3 bucket and populates to dynamo table
    const populateDynamoFn = new lambda.Function(this, 'populateDynamoFunction', {
      functionName: 'populate-dynamo',
      runtime: lambda.Runtime.PYTHON_3_10,
      handler: 'index.lambda_handler',
      code: lambda.Code.fromAsset('lib/lambda/populate_dynamo'),
      environment: {
        'TABLE_NAME': table.tableName,
        'BUCKET_NAME': bucket.bucketName
      },
      events: [
        new eventsources.S3EventSource(bucket, {
          events: [s3.EventType.OBJECT_CREATED]
        })
      ]
    });

    // allows lambda to write into the dynamodb table created
    const lambdaDynamoWrite = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ["dynamodb:BatchWriteItem"],
      resources: [table.tableArn]
    });

    // allows lambda to read s3 bucket objects 
    const lambdaS3Read = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      resources: [
        bucket.bucketArn,
        bucket.bucketArn + "/*"
      ]
    });

    // adds the created policies to the populate-dynamo lambda function role
    populateDynamoFn.addToRolePolicy(lambdaDynamoWrite);
    populateDynamoFn.addToRolePolicy(lambdaS3Read);

    // function that checks the resources put into Dynamo for the tags specified in this function (go to function code to edit)
    const resourceTagCheckerFn = new lambda.Function(this, 'resourceTagCheckerFunction', {
      functionName: 'resource-tag-checker',
      runtime: lambda.Runtime.PYTHON_3_10,
      handler: 'index.lambda_handler',
      code: lambda.Code.fromAsset('lib/lambda/resource_tag_checker'),
      environment: {
        'TABLE_NAME': table.tableName
      },
      events: [
        new eventsources.DynamoEventSource(table, {
          startingPosition: lambda.StartingPosition.LATEST,
          batchSize: 100
        })
      ]
    });

    // allows lambda to get the tags for specified resources
    const lambdaGetTags = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "s3:GetBucketTagging",
        "lambda:ListTags",
        "dynamodb:ListTagsOfResource",
        "dax:ListTags"
      ],
      resources: [
        `arn:aws:dynamodb:${region}:${accountId}:table/*`,
        'arn:aws:s3:::*',
        `arn:aws:lambda:${region}:${accountId}:function:*`,
        `arn:aws:dax:${region}:${accountId}:cache/*`
      ]
    });

    // allows lambda to scan and update the dynamodb table
    const lambdaScanUpdateDynamo = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "dynamodb:Scan",
        "dynamodb:UpdateItem"
      ],
      resources: [table.tableArn]
    });

    resourceTagCheckerFn.addToRolePolicy(lambdaGetTags);
    resourceTagCheckerFn.addToRolePolicy(lambdaScanUpdateDynamo);
    resourceTagCheckerFn.role?.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaDynamoDBExecutionRole'));
  }
}
