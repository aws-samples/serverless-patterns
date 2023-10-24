const cdk = require('aws-cdk-lib');
const {Construct} = require('constructs');
const apigateway = require('aws-cdk-lib/aws-apigateway');
const lambda = require('aws-cdk-lib/aws-lambda');

class BasicAuthorizerConstruct extends Construct {
    constructor(scope, id, props) {
        super(scope, id);

        // Lambda authorizer implementation
        const authFunction = new lambda.Function(this, 'authFunction', {
            code: lambda.Code.fromAsset('lambda/authorizer'),
            handler: 'index.handler',
            functionName: 'basic-authorizer',
            architecture: lambda.Architecture.ARM_64,
            runtime: lambda.Runtime.NODEJS_18_X
        });

        // API Gateway Lambda Authorizer
        const basicAuthorizer = new apigateway.TokenAuthorizer(this, 'basicAuthorizer', {
            name: 'BasicAuthorizer',
            handler: authFunction,
            identitySources: [apigateway.IdentitySource.header('Authorization')],
            resultsCacheTtl: cdk.Duration.seconds(300)
        });

        // Hello world Lambda function protected by the authorizer
        const protectedFunction = new lambda.Function(this, 'protectedFunction', {
            code: lambda.Code.fromAsset('lambda/protected'),
            handler: 'index.handler',
            functionName: 'basic-authorizer-protected-resource',
            architecture: lambda.Architecture.ARM_64,
            runtime: lambda.Runtime.NODEJS_18_X
        });

        // The API Gateway REST API
        const api = new apigateway.RestApi(this, 'BasicAuthProtectedAPI', {
            restApiName: 'BasicAuthProtectedAPI',
            endpointTypes: [apigateway.EndpointType.REGIONAL]
        });

        const methodResponses = [{
            statusCode: '200',
            responseModels: {
                'application/json': apigateway.Model.EMPTY_MODEL
            }
        }];

        api.root.addMethod('ANY', new apigateway.LambdaIntegration(protectedFunction), {
            methodResponses: methodResponses,
            authorizer: basicAuthorizer
        });

        // Tells the browser to use Basic auth
        const gatewayResponse = new apigateway.GatewayResponse(this, 'GatewayResponse', {
            restApi: api,
            type: apigateway.ResponseType.UNAUTHORIZED,
            responseHeaders: {
                'method.response.header.WWW-Authenticate': "'Basic'",
            },
            statusCode: '401',
            templates: {
                'application/json': '{"message":$context.error.messageString}',
            },
        });
    }
}

module.exports = {BasicAuthorizerConstruct};