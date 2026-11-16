import { aws_stepfunctions_tasks as tasks, aws_stepfunctions as sfn, CfnParameter, aws_iam as iam, CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class StepfunctionSesCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    var sesFromEmail = new CfnParameter(this, 'sesFromEmail', { type: 'String' });

    const SES_FROM_EMAIL = sesFromEmail.valueAsString;

    const sendEmail = new tasks.CallAwsService(this, 'SendEmail', {
      service: 'sesv2',
      action: 'sendEmail',
      parameters: {
        "Destination": {
          "ToAddresses": sfn.JsonPath.array(sfn.JsonPath.stringAt('$.email'))
        },
        "FromEmailAddress": SES_FROM_EMAIL,
        "Content": {
          "Simple": {
            "Body": {
              "Html": {
                "Charset": "UTF-8",
                "Data": "<h2>Visit ServerlessLand</h2><p>https://serverlessland.com</p>",
              },
            },
            "Subject": {
              "Charset": "UTF-8",
              "Data": "Hello from ServerlessLand"
            }
          }
        }
      },
      iamResources: ['arn:aws:ses:' + Stack.of(this).region + ':' + Stack.of(this).account + ':identity/' + SES_FROM_EMAIL],
    });

    const myStateMachine = new sfn.StateMachine(this, 'MyStateMachine', {
      definition: sendEmail,
      stateMachineType: sfn.StateMachineType.STANDARD,
    });

    myStateMachine.role?.attachInlinePolicy(
      new iam.Policy(this, 'SESPermissions', {
        statements: [
          new iam.PolicyStatement({
            actions: ['ses:SendEmail'],
            resources: ['arn:aws:ses:' + Stack.of(this).region + ':' + Stack.of(this).account + ':identity/' + SES_FROM_EMAIL],
          }),
        ],
      }),
    )

    // Output
    new CfnOutput(this, 'StateMachine', {
      value: myStateMachine.stateMachineName,
      description: 'State machine',
      exportName: 'StateMachine',
    });
  }
}
