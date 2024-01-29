import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import * as cdk from 'aws-cdk-lib';
import { Architecture, Runtime, Tracing } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import { HttpApi, HttpMethod} from 'aws-cdk-lib/aws-apigatewayv2';
import { HttpLambdaIntegration} from 'aws-cdk-lib/aws-apigatewayv2-integrations';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export class NodeEsmStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // for more info on how to customise the props check https://github.com/aws/aws-cdk/blob/main/packages/aws-cdk-lib/aws-lambda-nodejs/README.md
    const helloESMLambda: NodejsFunction = new NodejsFunction(this, "hello-esm-ts", {
      handler: 'handler',
      entry: join(__dirname, '../src/hello-world.ts'),
      runtime: Runtime.NODEJS_20_X,
      memorySize: 512,
      tracing: Tracing.ACTIVE,
      architecture: Architecture.X86_64,
      timeout: cdk.Duration.seconds(5),
      logRetention: RetentionDays.ONE_DAY,
      bundling: {
        banner: "import { createRequire } from 'module';const require = createRequire(import.meta.url);",
        minify: true,
        format: OutputFormat.ESM,
        tsconfig: join(__dirname, '../tsconfig.json'),
        esbuildArgs:{
          "--tree-shaking": "true"
        },
        externalModules: [] // in this way you bundle the CDK modules with the code for better performance
      }
    });

    const httpApi: HttpApi = new HttpApi(this, 'PublicGateway');

    const lambdaIntegration = new HttpLambdaIntegration('APIGatewayToLambda', helloESMLambda);

    httpApi.addRoutes({
      path: '/',
      methods: [HttpMethod.GET],
      integration: lambdaIntegration,
    });

    new cdk.CfnOutput(this, 'publicEndpoint', {
      value: `${httpApi.url}`
    });
  }
}
