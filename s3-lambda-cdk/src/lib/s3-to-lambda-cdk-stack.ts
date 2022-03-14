import { Stack, StackProps, CfnOutput, RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_s3 as s3 } from 'aws-cdk-lib';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { S3EventSource} from 'aws-cdk-lib/aws-lambda-event-sources';

export class S3ToLambdaCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    //Change this if desired
    const BUCKET_NAME = 'demo-bucket-serverless-patterns'

    // S3 bucket
    const bucket = new s3.Bucket(this, BUCKET_NAME, {
      /**
       * The following properties ensure the bucket is properly 
       * deleted when we run cdk destroy */
      autoDeleteObjects: true,
      removalPolicy: RemovalPolicy.DESTROY
    });


    // Lambda Function to read from Stream
    const lambdaReadStream = new NodejsFunction(this, 'readStream', {
      entry: 'lambda-fns/readStream/handler.js',
      handler: 'handler'
    });

    // Event Source Mapping S3 -> Lambda
    const s3PutEventSource = new S3EventSource(bucket, {
      events: [
        s3.EventType.OBJECT_CREATED_PUT
      ]
    });

    lambdaReadStream.addEventSource(s3PutEventSource);

    // Outputs
    new CfnOutput(this, 'BucketArn', { value: bucket.bucketArn });
    new CfnOutput(this, 'LambdaFunctionArn', { value: lambdaReadStream.functionArn });
  }
}
