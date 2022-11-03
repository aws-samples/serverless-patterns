import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnOutput, RemovalPolicy, Stack } from 'aws-cdk-lib';

import { EventBus, EventPattern, Rule } from 'aws-cdk-lib/aws-events';
import { LogGroup } from 'aws-cdk-lib/aws-logs';

export interface SchemaNotifierProps {
  readonly eventPattern?: EventPattern;
  readonly type?: 'Changed' | 'New' | 'All';
  readonly schemas?: string[];
  readonly sources?: string[];
  plugins: any[];
}

const getEventPatternForTypeOfNotification = (type: string, schemas?: string[], sources?: string[]) => {
  let pattern = {};

  if (schemas && schemas.length > 0) {
    pattern = {
      detail: {
        SchemaName: schemas
      },
    };
  }

  if(sources && sources.length > 0){
    pattern = {
      detail: {
        SchemaName: sources.map(source => ({ prefix: source }))
      },
    };
  }

  switch (type) {
    case 'Changed':
      pattern = {
        ...pattern,
        detailType: ['Schema Version Created'],
        source: ['aws.schemas'],
      };
      break;
    case 'New': {
      pattern = {
        ...pattern,
        detailType: ['Schema Created'],
        source: ['aws.schemas'],
      };
      break;
    }
    default:
      pattern = {
        ...pattern,
        detailType: ['Schema Created', 'Schema Version Created'],
        source: ['aws.schemas'],
      };
  }

  return pattern;
};

export class SchemaNotifier extends Construct {
  constructor(scope: Construct, id: string, config: SchemaNotifierProps) {
    super(scope, id);

    const typeOfNotification = config.type || 'All';

    // have to listen for schema changes on the default event bus
    const defaultEventBus = EventBus.fromEventBusName(this, 'EventBus', 'default');

    // useful for debugging
    const logGroup = new LogGroup(this, 'SchemaNotifierLogGroup', {
      logGroupName: `/aws/events/schema-listeners/${id}/schema-notification-logs`,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    // Setup Rule on the bus....
    const rule = new Rule(this, 'Rule', {
      eventBus: defaultEventBus,
      // dynamicly generate event pattern based on consumer inputs
      eventPattern: getEventPatternForTypeOfNotification(typeOfNotification, config.schemas, config.sources),
      ruleName: `${id}-listen-to-schema-changes`,
    });

    rule.addTarget(new cdk.aws_events_targets.CloudWatchLogGroup(logGroup));

    // go through all user defined plugins and add them to the stack, this is for future plugins
    config.plugins.map((Plugin) => {
      new Plugin(this, 'Plugin', {
        rule: rule,
        test: true,
      });
    });

    new CfnOutput(this, 'LogGroup', { value: logGroup.logGroupName });
  }
}
