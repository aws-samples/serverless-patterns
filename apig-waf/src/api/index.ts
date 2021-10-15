
import { LambdaRestApi } from "@aws-cdk/aws-apigateway";
import * as lambda from "@aws-cdk/aws-lambda";
import * as cdk from "@aws-cdk/core";
import path from "path";
import config from "./config.json";
import {PolicyStatement, ServicePrincipal, Effect, PolicyDocument, AnyPrincipal } from '@aws-cdk/aws-iam';

export class ApiStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string) {
    super(scope, id);

    const handler = new lambda.Function(this, "handler", {
      code: new lambda.AssetCode(path.resolve(__dirname, "dist")),
      handler: `index.${config.api.handler}`,
      runtime: lambda.Runtime.NODEJS_14_X,
    });

    //Grant api gateway invoke permission on lambda
    handler.grantInvoke(new ServicePrincipal('apigateway.amazonaws.com'));
    
    const apiResourcePolicy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['execute-api:Invoke'],
          principals: [new AnyPrincipal()],
          resources: ['execute-api:/*/*/*'],
        })
      ]
    });
    
    const restapi  = new LambdaRestApi(this, config.prefix, {
      handler,
      description: config.description,
      policy: apiResourcePolicy
    });

    const tags = config.tags

    tags.forEach(tag => {
      cdk.Tags.of(this).add(tag.key, tag.value)
      cdk.Tags.of(handler).add(tag.key, tag.value)
    })

    new cdk.CfnOutput(this, 'ApiUrl', {
      value: 'https://' + restapi.restApiId +  ".execute-api." +  this.region + ".amazonaws.com/prod",
      exportName: "ApiUrl",
      description: 'This is the api url that needs to be invoked',
    });

    new cdk.CfnOutput(this, 'demorestapiid', {
      value:  restapi.restApiId ,
      exportName: "demorestapiid",
      description: 'This is the api url that needs to be invoked',
    });
  }
}