import * as cdk from 'aws-cdk-lib';
import { Match, Template } from 'aws-cdk-lib/assertions';
import { BackendStack } from '../lib/backend-stack';

test('Lambda can stream only from the Claude inference profile and call only the send mutation', () => {
  const app = new cdk.App();
  const stack = new BackendStack(app, 'TestStack', { env: { account: '111111111111', region: 'us-east-1' } });
  const template = Template.fromStack(stack);
  const profile = 'arn:aws:bedrock:us-east-1:111111111111:inference-profile/global.anthropic.claude-haiku-5-5';

  template.hasResourceProperties('AWS::Lambda::Function', {
    Environment: { Variables: Match.objectLike({ MODEL_ID: 'global.anthropic.claude-haiku-5-5' }) },
  });
  template.hasResourceProperties('AWS::IAM::Role', {
    Policies: [Match.objectLike({
      PolicyDocument: Match.objectLike({
        Statement: Match.arrayWith([
          Match.objectLike({ Action: 'bedrock:InvokeModelWithResponseStream', Resource: profile }),
          Match.objectLike({
            Action: 'bedrock:InvokeModelWithResponseStream',
            Condition: { StringEquals: { 'bedrock:InferenceProfileArn': profile } },
            Resource: [
              'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-haiku-5-5',
              'arn:aws:bedrock:::foundation-model/anthropic.claude-haiku-5-5',
            ],
          }),
        ]),
      }),
    })],
  });
});
