import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { SchemaNotifier } from '../src/schema-notifier';
import { SlackNotifier } from '../plugins/slack/plugin';

export class NotifyConsumersOfSchemaChangesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // consumer can setup a SchemaNotifier and subscribe to what they want to know.
    new SchemaNotifier(this, 'TeamXSchemaNotifications', {
      type: 'All', // changed schemas? new schemas or both?
      // schemas: ['myapp.users@UserCreated', 'myapp.users@UserDeleted'], // only listen for schema changes for particular schema
      sources: ['myapp.users', 'myapp.orders'], // listen for all schema changes by sources
      plugins: [
        new SlackNotifier({
          API_KEY: process.env.SLACK_API_KEY,
          CHANNEL_ID: process.env.SLACK_CHANNEL_ID,
        }),
      ],
    });
  }
}