// Writes one ledger row per AWS IAM Identity Center Identity Store change event.
// The events carry IDs only, so user and group attributes are read with the Describe APIs.
import { IdentitystoreClient, DescribeUserCommand, DescribeGroupCommand } from '@aws-sdk/client-identitystore';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';

const { TABLE_NAME } = process.env;
if (!TABLE_NAME) throw new Error('TABLE_NAME is not set');

const clientConfig = { maxAttempts: 3, requestHandler: { requestTimeout: 3000, connectionTimeout: 1000 } };
const identityStore = new IdentitystoreClient(clientConfig);
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient(clientConfig), {
  marshallOptions: { removeUndefinedValues: true },
});

// Only user names and display names are stored. E-mail addresses and other personal data stay in AWS IAM Identity Center.
// A user or group deleted after the event was sent is not an error: its attributes are stored as null.
const orNull = async (call) => {
  try {
    return await call();
  } catch (err) {
    if (err.name === 'ResourceNotFoundException') return null;
    throw err;
  }
};
const describeUser = (IdentityStoreId, UserId) =>
  orNull(async () => {
    const r = await identityStore.send(new DescribeUserCommand({ IdentityStoreId, UserId }));
    return { userName: r.UserName, displayName: r.DisplayName };
  });
const describeGroup = (IdentityStoreId, GroupId) =>
  orNull(async () => {
    const r = await identityStore.send(new DescribeGroupCommand({ IdentityStoreId, GroupId }));
    return { displayName: r.DisplayName };
  });

export const handler = async (event) => {
  try {
    const d = event.detail;
    const storeId = d['identity-store'].id;
    const [kind, action] = event['detail-type'].split(' '); // User | Group | GroupMembership, Created | Updated | Deleted
    const resourceId = { User: d.user?.id, Group: d.group?.id, GroupMembership: d.membership?.id }[kind];

    let attributes; // stays undefined for *Deleted events: the resource is gone, so there is nothing to describe
    if (action !== 'Deleted') {
      if (kind === 'User') attributes = await describeUser(storeId, d.user.id);
      else if (kind === 'Group') attributes = await describeGroup(storeId, d.group.id);
      else attributes = { user: await describeUser(storeId, d.member.user.id), group: await describeGroup(storeId, d.group.id) };
    }

    const item = {
      eventId: event.id, // the idempotency key: EventBridge keeps the same id on a duplicate delivery
      eventTime: event.time,
      detailType: event['detail-type'],
      resourceType: kind,
      resourceId,
      requestId: d['request-id'],
      identityStoreId: storeId,
      ...(d.member && { userId: d.member.user.id, groupId: d.group.id }),
      attributes,
      processedAt: new Date().toISOString(),
    };
    try {
      await ddb.send(new PutCommand({ TableName: TABLE_NAME, Item: item, ConditionExpression: 'attribute_not_exists(eventId)' }));
    } catch (err) {
      if (err.name !== 'ConditionalCheckFailedException') throw err;
      console.log(JSON.stringify({ msg: 'duplicate delivery ignored', eventId: event.id }));
      return { status: 'duplicate', eventId: event.id };
    }
    console.log(JSON.stringify({ msg: 'stored', eventId: event.id, detailType: item.detailType, resourceId }));
    return { status: 'stored', eventId: event.id };
  } catch (err) {
    console.error(JSON.stringify({ msg: 'processing failed', eventId: event?.id, error: err.name, message: err.message }));
    throw err;
  }
};
