import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as glue from 'aws-cdk-lib/aws-glue';
import * as athena from 'aws-cdk-lib/aws-athena';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import * as path from 'path';

export class PatternStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket for failed Lambda events
    const failedEventsBucket = new s3.Bucket(this, 'FailedEventsBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
    });

    // S3 bucket for Athena query results
    const athenaResultsBucket = new s3.Bucket(this, 'AthenaResultsBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
    });

    // Lambda function with S3 failed-event destination
    // Note: S3Destination automatically grants only necessary write permissions (PutObject)
    // to the Lambda function for failed event delivery
    const processorFunction = new lambda.Function(this, 'ProcessorFunction', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'processor.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../lambda')),
      timeout: cdk.Duration.seconds(30),
      onFailure: new cdk.aws_lambda_destinations.S3Destination(failedEventsBucket),
    });

    // Glue Database for Athena
    const glueDatabase = new glue.CfnDatabase(this, 'FailedEventsDatabase', {
      catalogId: cdk.Aws.ACCOUNT_ID,
      databaseInput: {
        name: 'failed_events_db',
        description: 'Database for failed Lambda events',
      },
    });

    // Glue Table for failed events (simplified without partitioning)
    const glueTable = new glue.CfnTable(this, 'FailedEventsTable', {
      catalogId: cdk.Aws.ACCOUNT_ID,
      databaseName: glueDatabase.ref,
      tableInput: {
        name: 'failed_events',
        description: 'Table for failed Lambda events stored in S3',
        tableType: 'EXTERNAL_TABLE',
        storageDescriptor: {
          columns: [
            { name: 'version', type: 'string' },
            { name: 'timestamp', type: 'string' },
            { name: 'requestcontext', type: 'struct<requestid:string,functionarn:string,condition:string,approximateinvokecoun:int>' },
            { name: 'requestpayload', type: 'struct<body:string,resource:string,path:string,httpmethod:string,headers:map<string,string>,queryparam:map<string,string>>' },
            { name: 'responsepayload', type: 'struct<errortype:string,errormessage:string,trace:array<string>>' },
          ],
          location: `s3://${failedEventsBucket.bucketName}/`,
          inputFormat: 'org.apache.hadoop.mapred.TextInputFormat',
          outputFormat: 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
          serdeInfo: {
            serializationLibrary: 'org.openx.data.jsonserde.JsonSerDe',
            parameters: {
              'case.insensitive': 'true',
            },
          },
        },
      },
    });

    glueTable.addDependency(glueDatabase);

    // Athena Workgroup
    const athenaWorkgroup = new athena.CfnWorkGroup(this, 'FailedEventsWorkgroup', {
      name: 'failed-events-workgroup',
      workGroupConfiguration: {
        resultConfiguration: {
          outputLocation: `s3://${athenaResultsBucket.bucketName}/`,
        },
      },
    });

    // IAM role for Athena queries
    const athenaRole = new iam.Role(this, 'AthenaQueryRole', {
      assumedBy: new iam.ServicePrincipal('athena.amazonaws.com'),
    });

    failedEventsBucket.grantRead(athenaRole);
    athenaResultsBucket.grantReadWrite(athenaRole);

    // Outputs
    new cdk.CfnOutput(this, 'LambdaFunctionName', {
      value: processorFunction.functionName,
      description: 'Lambda function name for CLI invocation',
    });

    new cdk.CfnOutput(this, 'LambdaFunctionArn', {
      value: processorFunction.functionArn,
      description: 'Lambda function ARN',
    });

    new cdk.CfnOutput(this, 'FailedEventsBucketName', {
      value: failedEventsBucket.bucketName,
      description: 'S3 bucket for failed Lambda events',
    });

    new cdk.CfnOutput(this, 'AthenaResultsBucketName', {
      value: athenaResultsBucket.bucketName,
      description: 'S3 bucket for Athena query results',
    });

    new cdk.CfnOutput(this, 'GlueDatabaseName', {
      value: glueDatabase.ref,
      description: 'Glue database name',
    });

    new cdk.CfnOutput(this, 'GlueTableName', {
      value: 'failed_events',
      description: 'Glue table name',
    });

    new cdk.CfnOutput(this, 'AthenaWorkgroupName', {
      value: athenaWorkgroup.name!,
      description: 'Athena workgroup name',
    });
  }
}
