import * as apigw from "@aws-cdk/aws-apigateway";
import * as lambda from "@aws-cdk/aws-lambda";
import * as cdk from "@aws-cdk/core";
import { Tags } from "@aws-cdk/core";
import path from "path";
import config from "./config.json";


export class ApiStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string) {
    super(scope, id);

    const handler = new lambda.Function(this, "handler", {
      code: new lambda.AssetCode(path.resolve(__dirname, "dist")),
      handler: `index.${config.api.handler}`,
      runtime: lambda.Runtime.NODEJS_14_X,
    });
    
    new apigw.LambdaRestApi(this, config.apiName, {
      handler,
      description: config.apiDescription
    });


    const tags = config.tags

    tags.forEach(tag => {
      Tags.of(this).add(tag.key, tag.value)
      Tags.of(handler).add(tag.key, tag.value)
    })

  }
}
