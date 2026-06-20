/*!  Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  *  SPDX-License-Identifier: MIT-0
 */

import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs'
import * as path from 'path'


export class ApigwLambdaDynamodbCdkTsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const dynamodb_table = new dynamodb.Table(this, "Table", {
      partitionKey: { name: "id", type: dynamodb.AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY
      }
    )

    const lambda_backend = new NodejsFunction(this, "lambdaFunction", {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: "handler",
      entry: path.join(__dirname, '../src/index.ts'),
      tracing: lambda.Tracing.ACTIVE,
      environment: {
        DYNAMODB: dynamodb_table.tableName
      },
      bundling: {
        externalModules: ['@aws-sdk/*'],
      },
    })

    dynamodb_table.grantReadData(lambda_backend.role!)

    const api = new apigateway.RestApi(this, "RestAPI", {
      deployOptions: {
        dataTraceEnabled: true,
        tracingEnabled: true
      },
    })


    const endpoint = api.root.addResource("scan")
    const endpointMethod = endpoint.addMethod("GET", new apigateway.LambdaIntegration(lambda_backend))

  }
}
