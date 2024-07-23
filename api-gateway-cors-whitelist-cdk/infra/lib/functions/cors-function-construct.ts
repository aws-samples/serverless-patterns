import { GoFunction } from "@aws-cdk/aws-lambda-go-alpha";
import { Duration, Tags } from "aws-cdk-lib";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as path from "path";
import { FuncProps } from "../../config/infra-options";
import { Effect, PolicyStatement } from "aws-cdk-lib/aws-iam";

export class CorsFunctionConstruct extends Construct {
    private _corsFunc: GoFunction;

    get CorsFunc(): IFunction {
        return this._corsFunc;
    }

    constructor(scope: Construct, id: string, props: FuncProps) {
        super(scope, id);
        this._corsFunc = new GoFunction(scope, `CorsLambdaFunction`, {
            entry: path.join(__dirname, `../../../src/cors-function`),
            functionName: `cors`,
            timeout: Duration.seconds(10),
            environment: {
                IS_LOCAL: "false",
                LOG_LEVEL: "debug",
            },
        });

        const ssmPolicy = new PolicyStatement({
            resources: [
                `arn:aws:ssm:${props.region}:${props.accountNumber}:parameter/cors/ALLOWED_ORIGINS`,
            ],
            actions: ["ssm:GetParameters", "ssm:GetParameter"],
            effect: Effect.ALLOW,
        });

        this._corsFunc.addToRolePolicy(ssmPolicy);
        Tags.of(this._corsFunc).add("version", props.version);
    }
}
