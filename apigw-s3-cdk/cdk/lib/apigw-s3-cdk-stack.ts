import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
//import * as s3 from "@aws-cdk/aws-s3";
import { aws_apigateway as apigw } from "aws-cdk-lib";
import { aws_iam as iam } from "aws-cdk-lib";

export class ApigwS3CdkStack extends Stack {
  public readonly apiGatewayRole: iam.Role;

  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    //Create REST API
    const restApi = new apigw.RestApi(this, 'S3ObjectsApi', {
      restApiName: 'S3 Proxy Service',
      description: "S3 Actions Proxy API",
      endpointConfiguration: {
        types: [apigw.EndpointType.EDGE]
      },
      binaryMediaTypes: ['application/octet-stream', 'image/jpeg']
    });

    //Create {folder} API resource to list objects in a given bucket
    const bucketResource = restApi.root.addResource("{folder}");

    //Create {item} API resource to read/write an object in a given bucket
    const bucketItemResource = bucketResource.addResource("{item}");

    // Create IAM Role for API Gateway
    this.apiGatewayRole = new iam.Role(this, 'api-gateway-role', {
      assumedBy: new iam.ServicePrincipal('apigateway.amazonaws.com')
    });

    //ListAllMyBuckets method
    this.addActionToPolicy("s3:ListAllMyBuckets");
    const listMyBucketsIntegration = new apigw.AwsIntegration({
      service: "s3",
      region: "us-east-1",
      path: '/',
      integrationHttpMethod: "GET",
      options: {
        credentialsRole: this.apiGatewayRole,
        passthroughBehavior: apigw.PassthroughBehavior.WHEN_NO_TEMPLATES,
        integrationResponses: [{
          statusCode: '200',
          responseParameters: { 'method.response.header.Content-Type': 'integration.response.header.Content-Type'}
        }]        
      }
    });
    //ListAllMyBuckets method options
    const listMyBucketsMethodOptions = {
      authorizationType: apigw.AuthorizationType.IAM,
      methodResponses: [
        {
          statusCode: '200',
          responseParameters: {
            'method.response.header.Content-Type': true
          }
        }]
    };
    restApi.root.addMethod("GET", listMyBucketsIntegration, listMyBucketsMethodOptions);

    //ListBucket (Objects) method
    this.addActionToPolicy("s3:ListBucket");
    const listBucketIntegration = new apigw.AwsIntegration({
      service: "s3",
      region: "us-east-1",
      path: '{bucket}',
      integrationHttpMethod: "GET",
      options: {
        credentialsRole: this.apiGatewayRole,
        passthroughBehavior: apigw.PassthroughBehavior.WHEN_NO_TEMPLATES,
        requestParameters: { 'integration.request.path.bucket': 'method.request.path.folder' },
        integrationResponses: [{
          statusCode: '200',
          responseParameters: { 'method.response.header.Content-Type': 'integration.response.header.Content-Type'}
        }]        
      }
    });
    //ListBucket (Objects) method options
    const listBucketMethodOptions = {
      authorizationType: apigw.AuthorizationType.IAM,
      requestParameters: {
        'method.request.path.folder': true
      },
      methodResponses: [
        {
          statusCode: '200',
          responseParameters: {
            'method.response.header.Content-Type': true
          }
        }]
    };
    bucketResource.addMethod("GET", listBucketIntegration, listBucketMethodOptions);

    //GetObject (Metadata) method
    this.addActionToPolicy("s3:GetObject");
    const getObjectMetadataIntegration = new apigw.AwsIntegration({
      service: "s3",
      region: "us-east-1",
      path: '{bucket}/{object}',
      integrationHttpMethod: "HEAD",
      options: {
        credentialsRole: this.apiGatewayRole,
        passthroughBehavior: apigw.PassthroughBehavior.WHEN_NO_TEMPLATES,
        requestParameters: { 
          'integration.request.path.bucket': 'method.request.path.folder',
          'integration.request.path.object': 'method.request.path.item',
          'integration.request.header.Accept': 'method.request.header.Accept' 
        },
        integrationResponses: [{
          statusCode: '200',
          responseParameters: { 'method.response.header.Content-Type': 'integration.response.header.Content-Type'}
        }]        
      }
    });

    //GetObject (Metadata) method options
    const getObjectMetadataMethodOptions = {
      authorizationType: apigw.AuthorizationType.IAM,
      requestParameters: {
        'method.request.path.folder': true,
        'method.request.path.item': true,
        'method.request.header.Accept': true
      },
      methodResponses: [
        {
          statusCode: '200',
          responseParameters: {
            'method.response.header.Content-Type': true
          }
        }]
    };
    bucketItemResource.addMethod("HEAD", getObjectMetadataIntegration, getObjectMetadataMethodOptions);

    //GetObject method
    this.addActionToPolicy("s3:GetObject");
    const getObjectIntegration = new apigw.AwsIntegration({
      service: "s3",
      region: "us-east-1",
      path: '{bucket}/{object}',
      integrationHttpMethod: "GET",
      options: {
        credentialsRole: this.apiGatewayRole,
        passthroughBehavior: apigw.PassthroughBehavior.WHEN_NO_TEMPLATES,
        requestParameters: { 
          'integration.request.path.bucket': 'method.request.path.folder',
          'integration.request.path.object': 'method.request.path.item',
          'integration.request.header.Accept': 'method.request.header.Accept' 
        },
        integrationResponses: [{
          statusCode: '200',
          responseParameters: { 'method.response.header.Content-Type': 'integration.response.header.Content-Type'}
        }]        
      }
    });

    //GetObject method options
    const getObjectMethodOptions = {
      authorizationType: apigw.AuthorizationType.IAM,
      requestParameters: {
        'method.request.path.folder': true,
        'method.request.path.item': true,
        'method.request.header.Accept': true
      },
      methodResponses: [
        {
          statusCode: '200',
          responseParameters: {
            'method.response.header.Content-Type': true
          }
        }]
    };
    bucketItemResource.addMethod("GET", getObjectIntegration, getObjectMethodOptions);

    //PutObject method
    this.addActionToPolicy("s3:PutObject");
    const putObjectIntegration = new apigw.AwsIntegration({
      service: "s3",
      region: "us-east-1",
      path: '{bucket}/{object}',
      integrationHttpMethod: "PUT",
      options: {
        credentialsRole: this.apiGatewayRole,
        passthroughBehavior: apigw.PassthroughBehavior.WHEN_NO_TEMPLATES,
        requestParameters: { 
          'integration.request.path.bucket': 'method.request.path.folder',
          'integration.request.path.object': 'method.request.path.item',
          'integration.request.header.Accept': 'method.request.header.Accept' 
        },
        integrationResponses: [{
          statusCode: '200',
          responseParameters: { 'method.response.header.Content-Type': 'integration.response.header.Content-Type'}
        }]        
      }
    });

    //PutObject method options
    const putObjectMethodOptions = {
      authorizationType: apigw.AuthorizationType.IAM,
      requestParameters: {
        'method.request.path.folder': true,
        'method.request.path.item': true,
        'method.request.header.Accept': true,
        'method.request.header.Content-Type': true
      },
      methodResponses: [
        {
          statusCode: '200',
          responseParameters: {
            'method.response.header.Content-Type': true
          }
        }]
    };
    bucketItemResource.addMethod("PUT", putObjectIntegration, putObjectMethodOptions);
  }
  private addActionToPolicy(action: string) {
    this.apiGatewayRole.addToPolicy(new iam.PolicyStatement({
        resources: [
            "*"
        ],
        actions: [`${action}`]
    }));
  }
}
