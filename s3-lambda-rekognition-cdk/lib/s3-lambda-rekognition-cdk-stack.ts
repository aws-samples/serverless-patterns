import {
  aws_lambda as lambda,
  aws_lambda_nodejs as nodejs_lambda,
  aws_s3 as s3,
  aws_rekognition as rekognition,
  aws_lambda_event_sources as eventSource,
  aws_iam as iam,
  CfnOutput,
  Stack,
  StackProps
} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';

export class S3LambdaRekognitionCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const myS3Bucket = new s3.Bucket(this, 'MyS3Bucket');

    const myFacesCollection = new rekognition.CfnCollection(this, 'MyFacesCollection', {
      collectionId: 'myFacesCollection',
    });

    const faceIndexLambda = new nodejs_lambda.NodejsFunction(this, "FaceIndexLambda", {
      runtime: lambda.Runtime.NODEJS_14_X,
      entry: path.join(__dirname, `/../lambda/IndexFace/index.ts`),
      handler: "handler",
      retryAttempts: 0,
      environment: {
        FACES_COLLECTION_ID: myFacesCollection.ref
      }
    });

    faceIndexLambda.addEventSource(new eventSource.S3EventSource(myS3Bucket, {
      events: [s3.EventType.OBJECT_CREATED],
    }));

    myS3Bucket.grantRead(faceIndexLambda);

    faceIndexLambda.role?.attachInlinePolicy(
      new iam.Policy(this, 'rekognitionFaceIndexPermission', {
        statements: [
          new iam.PolicyStatement({
            actions: ['rekognition:IndexFaces'],
            resources: [myFacesCollection.attrArn],
          })
        ],
      }),
    );

    //Output
    new CfnOutput(this, 'S3BucketName', {
      value: myS3Bucket.bucketName,
      description: 'S3 Bucket Name',
      exportName: 'S3BucketName',
    });

    new CfnOutput(this, 'FacesCollectionId', {
      value: myFacesCollection.ref,
      description: 'Faces Collection',
      exportName: 'RekognitionFacesCollection',
    });
  }
}
