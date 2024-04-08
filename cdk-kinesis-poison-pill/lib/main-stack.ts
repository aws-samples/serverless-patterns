import { Construct } from "constructs";
import * as cdk from "aws-cdk-lib";
import { OneLambda } from "./one-lambda";
import { StackProps } from "aws-cdk-lib";

export class MainStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props: StackProps) {
        super(scope, id, props);

        // creates the Lambda that will be exercised to demonstrate the failure
        new OneLambda(this, "OneLambdaConstruct");
    }
}
