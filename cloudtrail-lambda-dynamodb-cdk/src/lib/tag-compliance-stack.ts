import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Duration } from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudtrail from 'aws-cdk-lib/aws-cloudtrail';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as eventsources from 'aws-cdk-lib/aws-lambda-event-sources';

export class TagComplianceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new dynamodb.Table(this, 's3ObjectsTable', {
      tableName: 's3-objects-table',
      partitionKey: {
        name: 'object_arn', 
        type: dynamodb.AttributeType.STRING
      },
      stream: dynamodb.StreamViewType.NEW_IMAGE,
      removalPolicy: cdk.RemovalPolicy.DESTROY 
    });

    const cloudtrail_bucket = new s3.Bucket(this, 'objectCreationLogs', {// name may be changed, need to make sure bucket name doesn't already exist
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      enforceSSL: true
    });
    new cdk.CfnOutput(this, 'BucketName', {value: cloudtrail_bucket.bucketName});

    const cloudtrailPrincipal = new iam.ServicePrincipal("cloudtrail.amazonaws.com");

    // policy that allows cloudtrail to store logs in the s3 bucket created
    const bucket_policy_statements = [
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        principals: [cloudtrailPrincipal],
        actions:["s3:GetBucketAcl"],
        resources:[cloudtrail_bucket.bucketArn],
      }),
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        principals:[cloudtrailPrincipal],
        actions:["s3:PutObject"],
        resources: [cloudtrail_bucket.arnForObjects(`AWSLogs/*`)],
        conditions: {
          "StringEquals": {
            "s3:x-amz-acl": "bucket-owner-full-control"
          }
        }
      })
    ]

    // adding the IAM statements to the bucket policy
    for(const statement of bucket_policy_statements) {
      cloudtrail_bucket.addToResourcePolicy(statement);
    }

    const trail = new cloudtrail.Trail(this, 'objectCreationTrail', {
      trailName: 'object-creation-trail',
      bucket: cloudtrail_bucket,
      isMultiRegionTrail: true,
      includeGlobalServiceEvents: true
    });


    trail.addEventSelector(
      cloudtrail.DataResourceType.S3_OBJECT, 
      ['arn:aws:s3:::'],
      {
        readWriteType: cloudtrail.ReadWriteType.WRITE_ONLY,
        includeManagementEvents: false
      }
    )

    // function that gets cloudtrail events from the s3 bucket and populates to dynamo table
    const populateDynamoFn = new lambda.Function(this, 'populateDynamoFunction', {
      functionName: 'populate-dynamo',
      runtime: lambda.Runtime.PYTHON_3_10,
      handler: 'index.lambda_handler',
      code: lambda.Code.fromAsset('lib/lambda/populate_dynamo'),
      environment: {
        'TABLE_NAME': table.tableName,
        'CLOUDTRAIL_BUCKET_NAME': cloudtrail_bucket.bucketName
      },
      events: [
        new eventsources.S3EventSource(cloudtrail_bucket, {
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
        cloudtrail_bucket.bucketArn,
        cloudtrail_bucket.bucketArn + "/*"
      ]
    });

    // adds the created policies to the populate-dynamo lambda function role
    populateDynamoFn.addToRolePolicy(lambdaDynamoWrite);
    populateDynamoFn.addToRolePolicy(lambdaS3Read);

    // function that checks the resources put into Dynamo for the tags specified in this function (go to function code to edit)
    const objectTagCheckerFn = new lambda.Function(this, 'objectTagCheckerFunction', {
      functionName: 'object-tag-checker',
      runtime: lambda.Runtime.PYTHON_3_10,
      handler: 'index.lambda_handler',
      code: lambda.Code.fromAsset('lib/lambda/object_tag_checker'),
      environment: {
        'TABLE_NAME': table.tableName
      },
      events: [
        new eventsources.DynamoEventSource(table, {
          startingPosition: lambda.StartingPosition.LATEST,
          batchSize: 100,
          retryAttempts: 1,
          maxRecordAge: Duration.seconds(300)
        })
      ]
    });

    // allows lambda to get the tags for specified resources
    const lambdaGetObjectTags = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "s3:GetObjectTagging",
      ],
      resources: [
        'arn:aws:s3:::*',
      ]
    });

    // allows lambda to scan and update the dynamodb table
    const lambdaUpdateDynamo = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "dynamodb:UpdateItem"
      ],
      resources: [table.tableArn]
    });

    objectTagCheckerFn.addToRolePolicy(lambdaGetObjectTags);
    objectTagCheckerFn.addToRolePolicy(lambdaUpdateDynamo);
    objectTagCheckerFn.role?.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaDynamoDBExecutionRole'));
  }
}