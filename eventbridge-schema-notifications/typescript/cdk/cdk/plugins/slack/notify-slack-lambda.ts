import { ChatPostMessageArguments, WebClient } from '@slack/web-api';
import { SchemasClient, DescribeSchemaCommand } from '@aws-sdk/client-schemas';
import { EventBridgeEvent } from 'aws-lambda'
import diffString from 'variable-diff';

const schemaClient = new SchemasClient({});

const client = new WebClient(process.env.SLACK_API_KEY, {});

const buildURLForSchema = (event: any, version: string) => {
  return `https://${event.region}.console.aws.amazon.com/events/home?region=${event.region}#/registries/${event.detail.RegistryName}/schemas/${event.detail.SchemaName}/version/${version}`;
};


export async function handler(event: EventBridgeEvent<'Schema Version Created' | 'Schema Created', any>) {
  let blocks;

  if (!process.env.CHANNEL_ID) {
    throw Error('No Channel ID found');
  }

  if (event['detail-type'] === 'Schema Version Created') {
    blocks = await buildBlocksForSchemaChanged(event);
  } else {
    blocks = await buildBlocksForNewSchema(event);
  }

  try {
    // write message to slack
    await client.chat.postMessage(blocks as ChatPostMessageArguments);
  } catch (error) {
    console.log(error);
  }
}

const buildBlocksForSchemaChanged = async (event: any) => {
  const [source, detailType] = event.detail.SchemaName.split('@');
  const newVersion = event.detail.Version;
  const oldVersion = newVersion - 1;

  const { Content: oldVersionSchema } = await schemaClient.send(
    new DescribeSchemaCommand({
      RegistryName: event.detail.RegistryName,
      SchemaName: event?.detail.SchemaName,
      SchemaVersion: oldVersion.toString(),
    })
  );

  const { Content: newVersionSchema } = await schemaClient.send(
    new DescribeSchemaCommand({
      RegistryName: event.detail.RegistryName,
      SchemaName: event?.detail.SchemaName,
      SchemaVersion: newVersion,
    })
  );

  if (!oldVersionSchema || !newVersionSchema) {
    throw new Error('Cannot find old and new version of schema');
  }

  const { text: diff } = diffString(JSON.parse(oldVersionSchema), JSON.parse(newVersionSchema), {
    color: false,
  });

  return {
    channel: process.env.CHANNEL_ID,
    blocks: [
      {
        type: 'divider',
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `🚨 New schema found for event *"${detailType}"*`,
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Previous Version:*\n<${buildURLForSchema(event, oldVersion.toString())}|version ${oldVersion}>`,
          },
          {
            type: 'mrkdwn',
            text: `*New Version:*\n<${buildURLForSchema(event, newVersion.toString())}|version ${newVersion}>`,
          },
        ],
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Event Source:*\n${source}`,
          },
          {
            type: 'mrkdwn',
            text: `*Creation Date:*\n${event.detail.CreationDate}`,
          },
        ],
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `*Diff (v${oldVersion}:v${newVersion})* \`\`\`${diff}\`\`\``,
        },
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: '_What am I seeing this? A new version of an event has been created. You may have downstream consumers that may break due to contract changes._',
          },
        ],
      },
      {
        type: 'divider',
      },
    ],
  };
};

const buildBlocksForNewSchema = async (event: any) => {
  const [source, detailType] = event.detail.SchemaName.split('@');
  const newVersion = event.detail.Version;

  const { Content: schema } = await schemaClient.send(
    new DescribeSchemaCommand({
      RegistryName: event.detail.RegistryName,
      SchemaName: event?.detail.SchemaName,
      SchemaVersion: newVersion,
    })
  );

  if (!schema) {
    throw new Error('No schema found for event');
  }

  return {
    channel: process.env.CHANNEL_ID,
    blocks: [
      {
        type: 'divider',
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `⭐️ A new event has been published *"${detailType}"*`,
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Version:*\n<${buildURLForSchema(event, newVersion)}|version ${newVersion}>`,
          },
          {
            type: 'mrkdwn',
            text: `*SchemaType:*\n${event.detail.SchemaType}`,
          },
        ],
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Event Source:*\n${source}`,
          },
          {
            type: 'mrkdwn',
            text: `*Creation Date:*\n${event.detail.CreationDate}`,
          },
        ],
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `*Schema (v${newVersion})* \`\`\`${JSON.stringify(JSON.parse(schema), null, 4)}\`\`\``,
        },
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: '_What am I seeing this? A new event has been created on your event bus._',
          },
        ],
      },
      {
        type: 'divider',
      },
    ],
  };
};