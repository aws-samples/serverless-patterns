import { Construct } from "constructs";
import { Stack, StackProps, Tags } from "aws-cdk-lib";

import * as apigw from "aws-cdk-lib/aws-apigateway"
import * as lambda from "aws-cdk-lib/aws-lambda";

import path from "node:path";
import config from "./config.json";

export class ApiStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id,props);

    const handler = new lambda.Function(this, "handler", {
      code: new lambda.AssetCode(path.resolve(__dirname, "dist")),
      handler: `index.${config.api.handler}`,
      runtime: lambda.Runtime.NODEJS_16_X,
      architecture: lambda.Architecture.ARM_64
    });

    new apigw.LambdaRestApi(this, config.apiName, {
      handler,
      description: config.apiDescription,
      proxy: true, // defines a greedy proxy ("{proxy+}")
    });

    const tags = config.tags

    tags.forEach(tag => {
      Tags.of(this).add(tag.key, tag.value)
      Tags.of(handler).add(tag.key, tag.value)
    })
  }
}
