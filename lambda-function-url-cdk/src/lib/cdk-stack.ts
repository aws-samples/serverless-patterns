import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Function, Runtime, Code, FunctionUrlAuthType } from "aws-cdk-lib/aws-lambda";

export class CdkStack extends Stack {
    constructor(scope: Construct, id: string, props?: StackProps) {
      super(scope, id, props);
  
      // lambda function
      const myFunction = new Function(this, "myFunction", {
        runtime: Runtime.NODEJS_14_X,
        code: Code.fromAsset("functions"),
        handler: "handler.app"
      });
  
      const myFunctionUrl = myFunction.addFunctionUrl({
        authType: FunctionUrlAuthType.NONE,
        cors: {
          allowedOrigins: ['*'],
        }
      });
  
      new CfnOutput(this, 'FunctionUrl', {
        value: myFunctionUrl.url,
      });
    }
  }