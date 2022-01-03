import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { EventBus } from 'aws-cdk-lib/aws-events';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const bus = new EventBus(this, 'bus', {
      eventBusName: 'DemoEventBus'
    });
  }
}
