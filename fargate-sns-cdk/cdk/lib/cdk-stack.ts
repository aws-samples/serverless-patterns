import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Topic } from 'aws-cdk-lib/aws-sns';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const topic = new Topic(this, 'Topic', {
      displayName: 'demo topic',
      topicName: 'demoTopic',
    });
  }
}
