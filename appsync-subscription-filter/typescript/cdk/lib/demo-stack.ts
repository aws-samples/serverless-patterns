import * as esbuild from 'esbuild';
import * as path from 'path';

import { Construct } from 'constructs';
import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { AuthorizationType, Code, FieldLogLevel, FunctionRuntime, GraphqlApi, SchemaFile } from 'aws-cdk-lib/aws-appsync';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';

export class DemoStack extends Stack {
    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props);

        // Create AppSync instance
        const api = new GraphqlApi(this, 'Api', {
            name: 'DemoApi',
            definition: {
                schema: SchemaFile.fromAsset('lib/graphql/schema.graphql'),
            },
            authorizationConfig: {
                defaultAuthorization: {
                    authorizationType: AuthorizationType.IAM,
                },
            },
            logConfig: {
                fieldLogLevel: FieldLogLevel.ALL,
                retention: RetentionDays.ONE_DAY,
            },
        });
        new CfnOutput(Stack.of(this), 'ApiEndpointUrl', {
            value: api.graphqlUrl,
        });

        // Add NONE data-source
        const noneDS = api.addNoneDataSource('NoneDataSource', {});

        // Add resolvers
        noneDS.createResolver('IdentityResolver', {
            typeName: 'Query',
            fieldName: 'identity',
            code: Code.fromAsset(this.buildTransform('lib/graphql/resolvers/Query.identity.ts')),
            runtime: FunctionRuntime.JS_1_0_0,
        });

        noneDS.createResolver('SendResponseResolver', {
            typeName: 'Mutation',
            fieldName: 'sendResponse',
            code: Code.fromAsset(this.buildTransform('lib/graphql/resolvers/Mutation.sendResponse.ts')),
            runtime: FunctionRuntime.JS_1_0_0,
        });

        noneDS.createResolver('OnResponseReceivedResolver', {
            typeName: 'Subscription',
            fieldName: 'onResponseReceived',
            code: Code.fromAsset(this.buildTransform('lib/graphql/resolvers/Subscription.onResponseReceived.ts')),
            runtime: FunctionRuntime.JS_1_0_0,
        });
    }

    // This function uses esbuild to convert TypeScript code to JavaScript
    // NOTE: TypeScript code functionality must be limited to the `FunctionRuntime.JS_1_0_0` supported one!!!
    private buildTransform(typeScriptFilePath: string): string {
        // Gitignored temporary folder for storing the transpilation results
        const outDir = '.build';

        esbuild.buildSync({
            entryPoints: [typeScriptFilePath],
            bundle: true,
            platform: 'neutral',
            outdir: outDir,
            sourcemap: 'inline',
            sourcesContent: false,
            minify: false,
            external: ['@aws-appsync/utils'],
        });

        return path.format({
            ...path.parse(typeScriptFilePath),
            dir: outDir,
            base: undefined,
            ext: '.js',
        });
    }
}
