import * as cdk from 'aws-cdk-lib';
import * as apigw from 'aws-cdk-lib/aws-apigateway';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class ApigwDynamodbBulkPutStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Table that receives the items.
    const table = new dynamodb.Table(this, 'Table', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      encryption: dynamodb.TableEncryption.AWS_MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // demo only: cdk destroy deletes the table and its items
    });

    // Input files under input/, ERROR and CONDITION_CHECK_FAILURE reports under reports/.
    const bucket = new s3.Bucket(this, 'Bucket', {
      encryption: s3.BucketEncryption.S3_MANAGED,
      enforceSSL: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // demo only
      autoDeleteObjects: true, // lets cdk destroy empty the bucket (adds an AWS CDK helper function that runs on AWS Lambda; requests do not use it)
    });

    // The IAM actions are named after the bulk operation, not after the API: StartBulkPutItems is authorized
    // by dynamodb:StartBulkOperation (plus dynamodb:BulkPutItems on the table).
    const bulkOperations = this.formatArn({ service: 'dynamodb', resource: 'bulk-operation', resourceName: '*' });
    // No condition on the trust policy: with an aws:SourceAccount condition, Amazon API Gateway failed the call with
    // "API Gateway does not have permission to assume the provided role" (aws:SourceArn was not tried).
    const apiRole = new iam.Role(this, 'ApiRole', { assumedBy: new iam.ServicePrincipal('apigateway.amazonaws.com') });
    apiRole.addToPolicy(new iam.PolicyStatement({ actions: ['dynamodb:StartBulkOperation'], resources: [bulkOperations] }));
    apiRole.addToPolicy(new iam.PolicyStatement({ actions: ['dynamodb:BulkPutItems'], resources: [table.tableArn] }));
    apiRole.addToPolicy(new iam.PolicyStatement({ actions: ['dynamodb:DescribeBulkOperation'], resources: [bulkOperations] }));
    apiRole.addToPolicy(
      new iam.PolicyStatement({
        actions: ['s3:ListBucket'],
        resources: [bucket.bucketArn],
        conditions: { StringLike: { 's3:prefix': 'input/*' } },
      }),
    );
    apiRole.addToPolicy(new iam.PolicyStatement({ actions: ['s3:GetObject'], resources: [bucket.arnForObjects('input/*')] }));
    apiRole.addToPolicy(
      new iam.PolicyStatement({ actions: ['s3:PutObject', 's3:AbortMultipartUpload'], resources: [bucket.arnForObjects('reports/*')] }),
    );

    const api = new apigw.RestApi(this, 'Api', {
      cloudWatchRole: false, // do not create the account-wide API Gateway logging role
      deployOptions: { stageName: 'v1', throttlingRateLimit: 5, throttlingBurstLimit: 10 },
      defaultMethodOptions: { authorizationType: apigw.AuthorizationType.IAM },
      // Callers must sign with SigV4 and need execute-api:Invoke in an identity policy. This policy also refuses principals of other accounts.
      policy: new iam.PolicyDocument({
        statements: [
          new iam.PolicyStatement({
            effect: iam.Effect.DENY,
            principals: [new iam.AnyPrincipal()],
            actions: ['execute-api:Invoke'],
            resources: ['execute-api:/*'],
            conditions: { StringNotEquals: { 'aws:PrincipalAccount': this.account } },
          }),
        ],
      }),
    });

    const validator = api.addRequestValidator('BodyValidator', { validateRequestBody: true });
    const startModel = api.addModel('StartModel', {
      contentType: 'application/json',
      schema: {
        schema: apigw.JsonSchemaVersion.DRAFT4,
        type: apigw.JsonSchemaType.OBJECT,
        required: ['prefix'],
        additionalProperties: false,
        // The pattern keeps quotes and backslashes out of the key prefix that the mapping template copies into JSON.
        properties: { prefix: { type: apigw.JsonSchemaType.STRING, minLength: 1, maxLength: 200, pattern: '^[A-Za-z0-9/_.=-]+$' } },
      },
    });

    const errorResponses = [
      { statusCode: '400', selectionPattern: '4\\d{2}', responseTemplates: { 'application/json': '{"message": $input.json(\'$.message\')}' } },
      { statusCode: '500', selectionPattern: '5\\d{2}', responseTemplates: { 'application/json': '{"message": "DynamoDB returned an error"}' } },
    ];
    const methodResponses = [{ statusCode: '200' }, { statusCode: '400' }, { statusCode: '500' }];

    const operations = api.root.addResource('operations');

    // POST /operations {"prefix": "daily/"}: start a bulk put items operation for the files under input/daily/.
    operations.addMethod(
      'POST',
      new apigw.AwsIntegration({
        service: 'dynamodb',
        action: 'StartBulkPutItems',
        integrationHttpMethod: 'POST',
        options: {
          credentialsRole: apiRole,
          passthroughBehavior: apigw.PassthroughBehavior.NEVER,
          requestTemplates: {
            'application/json': `{
  "TableName": "${table.tableName}",
  "InputS3Configuration": {
    "S3Bucket": "${bucket.bucketName}",
    "S3KeyPrefix": "input/$input.path('$.prefix')",
    "InputFormat": "DYNAMODB_JSON",
    "InputCompressionType": "NONE"
  },
  "OutputS3Configuration": {
    "S3Bucket": "${bucket.bucketName}",
    "S3KeyPrefix": "reports/",
    "OutputType": ["ERROR", "CONDITION_CHECK_FAILURE"]
  },
  "ClientToken": "$context.requestId"
}`,
          },
          integrationResponses: [
            {
              statusCode: '200',
              responseTemplates: {
                // The operation id is the part of the operation ARN after "bulk-operation/". VTL does not allow
                // arithmetic inside a method call, so the index is computed with #set first.
                'application/json': `#set($op = $input.path('$.BulkOperationDescription'))
#set($arn = $op.BulkOperationArn)
#set($start = $arn.lastIndexOf('/') + 1)
{"operationId": "$arn.substring($start)", "status": "$op.BulkOperationStatus"}`,
              },
            },
            ...errorResponses,
          ],
        },
      }),
      { requestValidator: validator, requestModels: { 'application/json': startModel }, methodResponses },
    );

    // GET /operations/{operationId}: progress and outcome of one operation.
    operations.addResource('{operationId}').addMethod(
      'GET',
      new apigw.AwsIntegration({
        service: 'dynamodb',
        action: 'DescribeBulkOperation',
        integrationHttpMethod: 'POST',
        options: {
          credentialsRole: apiRole,
          passthroughBehavior: apigw.PassthroughBehavior.NEVER,
          requestTemplates: {
            'application/json': `{"BulkOperationArn": "arn:${this.partition}:dynamodb:${this.region}:${this.account}:bulk-operation/$util.escapeJavaScript($input.params('operationId'))"}`,
          },
          integrationResponses: [
            {
              statusCode: '200',
              responseTemplates: {
                'application/json': `#set($d = $input.path('$.BulkOperationDescription'))
{
  "status": "$d.BulkOperationStatus",
  "processedItemCount": #if($d.ProcessedItemCount)$d.ProcessedItemCount#{else}0#end,
  "failedItemCount": #if($d.FailedItemCount)$d.FailedItemCount#{else}0#end,
  "failureCode": "$util.escapeJavaScript("$!d.FailureCode")"
}`,
              },
            },
            ...errorResponses,
          ],
        },
      }),
      { methodResponses },
    );

    new cdk.CfnOutput(this, 'ApiUrl', { value: api.url });
    new cdk.CfnOutput(this, 'TableName', { value: table.tableName });
    new cdk.CfnOutput(this, 'BucketName', { value: bucket.bucketName });
  }
}
