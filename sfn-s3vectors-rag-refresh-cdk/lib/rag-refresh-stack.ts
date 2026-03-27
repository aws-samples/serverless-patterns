import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3vectors from 'aws-cdk-lib/aws-s3vectors';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import * as path from 'path';
import { Construct } from 'constructs';

// Titan Text Embeddings V2 produces 1024-dimensional vectors by default
const EMBEDDING_DIMENSION = 1024;

export class RagRefreshStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // --- S3 bucket for source documents ---
    const documentBucket = new s3.Bucket(this, 'DocumentBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // --- S3 Vectors resources ---
    const vectorBucket = new s3vectors.CfnVectorBucket(this, 'VectorBucket', {
      vectorBucketName: `rag-vectors-${cdk.Aws.ACCOUNT_ID}-${cdk.Aws.REGION}`,
    });

    const vectorIndex = new s3vectors.CfnIndex(this, 'VectorIndex', {
      vectorBucketName: vectorBucket.vectorBucketName!,
      indexName: 'knowledge-base',
      dataType: 'float32',
      dimension: EMBEDDING_DIMENSION,
      distanceMetric: 'cosine',
    });
    vectorIndex.addDependency(vectorBucket);

    // --- Lambda: embed & store vectors ---
    const embedFunction = new NodejsFunction(this, 'EmbedFunction', {
      functionName: 'ragEmbedAndStore',
      runtime: lambda.Runtime.NODEJS_22_X,
      entry: path.join(__dirname, '../lambda/embed.ts'),
      handler: 'handler',
      timeout: cdk.Duration.minutes(5),
      memorySize: 512,
      environment: {
        DOCUMENT_BUCKET: documentBucket.bucketName,
        VECTOR_BUCKET_NAME: vectorBucket.vectorBucketName!,
        VECTOR_INDEX_NAME: vectorIndex.indexName!,
      },
    });

    documentBucket.grantRead(embedFunction);
    embedFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        'arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0',
      ],
    }));
    embedFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['s3vectors:PutVectors'],
      resources: ['*'],
    }));

    // --- Lambda: validate vectors via QueryVectors ---
    const validateFunction = new NodejsFunction(this, 'ValidateFunction', {
      functionName: 'ragValidateVectors',
      runtime: lambda.Runtime.NODEJS_22_X,
      entry: path.join(__dirname, '../lambda/validate.ts'),
      handler: 'handler',
      timeout: cdk.Duration.minutes(1),
      memorySize: 256,
      environment: {
        VECTOR_BUCKET_NAME: vectorBucket.vectorBucketName!,
        VECTOR_INDEX_NAME: vectorIndex.indexName!,
      },
    });

    documentBucket.grantRead(validateFunction);
    validateFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        'arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0',
      ],
    }));
    validateFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['s3vectors:QueryVectors', 's3vectors:GetVectors'],
      resources: ['*'],
    }));

    // --- Lambda: rollback (delete vectors) ---
    const rollbackFunction = new NodejsFunction(this, 'RollbackFunction', {
      functionName: 'ragRollbackVectors',
      runtime: lambda.Runtime.NODEJS_22_X,
      entry: path.join(__dirname, '../lambda/rollback.ts'),
      handler: 'handler',
      timeout: cdk.Duration.minutes(2),
      memorySize: 256,
      environment: {
        VECTOR_BUCKET_NAME: vectorBucket.vectorBucketName!,
        VECTOR_INDEX_NAME: vectorIndex.indexName!,
      },
    });

    rollbackFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['s3vectors:DeleteVectors'],
      resources: ['*'],
    }));

    // --- Step Functions workflow (JSONata) ---

    const definition = {
      QueryLanguage: 'JSONata',
      StartAt: 'ProcessDocuments',
      States: {
        ProcessDocuments: {
          Type: 'Map',
          ItemProcessor: {
            ProcessorConfig: {
              Mode: 'DISTRIBUTED',
              ExecutionType: 'STANDARD',
            },
            StartAt: 'EmbedAndStore',
            States: {
              EmbedAndStore: {
                Type: 'Task',
                Resource: 'arn:aws:states:::lambda:invoke',
                Arguments: {
                  FunctionName: embedFunction.functionArn,
                  Payload: '{% $states.input %}',
                },
                Output: {
                  vectorKey: '{% $states.result.Payload.vectorKey %}',
                  documentKey: '{% $states.result.Payload.documentKey %}',
                },
                End: true,
              },
            },
          },
          ItemReader: {
            Resource: 'arn:aws:states:::s3:listObjectsV2',
            Arguments: {
              Bucket: documentBucket.bucketName,
              Prefix: 'documents/',
            },
          },
          MaxConcurrency: 40,
          ResultWriter: {
            Resource: 'arn:aws:states:::s3:putObject',
            Arguments: {
              Bucket: documentBucket.bucketName,
              Prefix: 'results/',
            },
          },
          Next: 'ValidateIngestion',
        },
        ValidateIngestion: {
          Type: 'Task',
          Resource: 'arn:aws:states:::lambda:invoke',
          Arguments: {
            FunctionName: validateFunction.functionArn,
            Payload: '{% $states.input %}',
          },
          Output: {
            valid: '{% $states.result.Payload.valid %}',
            vectorKeys: '{% $states.result.Payload.vectorKeys %}',
          },
          Next: 'ValidationPassed',
        },
        ValidationPassed: {
          Type: 'Choice',
          Choices: [
            {
              Condition: '{% $states.input.valid %}',
              Next: 'IngestionSucceeded',
            },
          ],
          Default: 'RollbackVectors',
        },
        IngestionSucceeded: {
          Type: 'Succeed',
        },
        RollbackVectors: {
          Type: 'Task',
          Resource: 'arn:aws:states:::lambda:invoke',
          Arguments: {
            FunctionName: rollbackFunction.functionArn,
            Payload: {
              vectorKeys: '{% $states.input.vectorKeys %}',
            },
          },
          Next: 'IngestionFailed',
        },
        IngestionFailed: {
          Type: 'Fail',
          Cause: 'Validation failed — vectors rolled back',
        },
      },
    };

    const logGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      logGroupName: '/aws/stepfunctions/rag-refresh',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const stateMachine = new sfn.StateMachine(this, 'RagRefreshStateMachine', {
      stateMachineName: 'rag-knowledge-base-refresh',
      definitionBody: sfn.DefinitionBody.fromString(JSON.stringify(definition)),
      timeout: cdk.Duration.hours(1),
      logs: {
        destination: logGroup,
        level: sfn.LogLevel.ALL,
      },
    });

    // Grant the state machine permission to read the S3 bucket (for Distributed Map)
    documentBucket.grantRead(stateMachine);
    documentBucket.grantReadWrite(stateMachine);

    // Grant the state machine permission to invoke the Lambda functions
    embedFunction.grantInvoke(stateMachine);
    validateFunction.grantInvoke(stateMachine);
    rollbackFunction.grantInvoke(stateMachine);

    // Distributed Map (STANDARD child executions) needs StartExecution + DescribeExecution + StopExecution on itself
    // Use a constructed ARN to avoid circular dependency between the state machine and its role policy
    stateMachine.addToRolePolicy(new iam.PolicyStatement({
      actions: ['states:StartExecution', 'states:DescribeExecution', 'states:StopExecution'],
      resources: [`arn:aws:states:${this.region}:${this.account}:stateMachine:rag-knowledge-base-refresh`],
    }));

    // --- Outputs ---
    new cdk.CfnOutput(this, 'DocumentBucketName', {
      value: documentBucket.bucketName,
      description: 'Upload documents to s3://<bucket>/documents/',
    });

    new cdk.CfnOutput(this, 'VectorBucketName', {
      value: vectorBucket.vectorBucketName!,
      description: 'S3 Vectors bucket name',
    });

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
      description: 'Step Functions state machine ARN',
    });
  }
}
