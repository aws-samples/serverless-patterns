import { Construct } from "constructs";
import { IRole, Role } from "aws-cdk-lib/aws-iam";
import { Fn, NestedStack, NestedStackProps } from "aws-cdk-lib";
import {
    BasePathMapping,
    DomainName,
    IModel,
    IRestApi,
    JsonSchemaType,
    JsonSchemaVersion,
    LambdaIntegration,
    MockIntegration,
    PassthroughBehavior,
    Resource,
    RestApi,
    TokenAuthorizer,
} from "aws-cdk-lib/aws-apigateway";
import { IFunction } from "aws-cdk-lib/aws-lambda";

interface ApiProps {
    role: Role;
    func: IFunction;
}

export class ApiGatewayConstruct extends Construct {
    constructor(scope: Construct, id: string, props: ApiProps) {
        super(scope, id);

        const api = new RestApi(this, "RestApi", {
            description: "CORS Sample API",
            restApiName: "CorsAPISample",
            deployOptions: {
                stageName: "main",
            },
        });

        api.root.addMethod(
            "GET",
            new MockIntegration({
                integrationResponses: [{ statusCode: "200" }],
                passthroughBehavior: PassthroughBehavior.NEVER,
                requestTemplates: {
                    "application/json": '{ "statusCode": 200 }',
                },
            }),
            {
                methodResponses: [{ statusCode: "200" }],
            }
        );
        api.root.addMethod(
            "OPTIONS",
            new LambdaIntegration(props.func, {
                credentialsRole: props.role,
                proxy: true,
            })
        );
    }
}
