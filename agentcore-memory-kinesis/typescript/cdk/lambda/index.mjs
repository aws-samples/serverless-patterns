import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand, DeleteCommand } from '@aws-sdk/lib-dynamodb';

const TABLE_NAME = process.env.TABLE_NAME;
if (!TABLE_NAME) throw new Error('TABLE_NAME is not set');
// METADATA_ONLY events have no memoryRecordText, so drop undefined attributes instead of failing.
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}), { marshallOptions: { removeUndefinedValues: true } });

// Default built-in namespace: /strategies/{memoryStrategyId}/actors/{actorId}
const actorOf = (namespace) => /\/actors\/([^/]+)/.exec(namespace ?? '')?.[1] ?? 'unknown';

export const handler = async (event) => {
  for (const record of event.Records) {
    try {
      const e = JSON.parse(Buffer.from(record.kinesis.data, 'base64').toString('utf8')).memoryStreamEvent;
      if (e.eventType === 'MemoryRecordDeleted') {
        // Deleted events carry only memoryId and memoryRecordId, so the table key is memoryRecordId.
        await ddb.send(new DeleteCommand({ TableName: TABLE_NAME, Key: { memoryRecordId: e.memoryRecordId } }));
      } else {
        const namespace = e.namespaces?.[0];
        await ddb.send(new PutCommand({
          TableName: TABLE_NAME,
          Item: {
            memoryRecordId: e.memoryRecordId,
            actorId: actorOf(namespace),
            memoryId: e.memoryId,
            strategyType: e.memoryStrategyType,
            namespace,
            memoryRecordText: e.memoryRecordText,
            eventType: e.eventType,
            eventTime: e.eventTime,
          },
        }));
      }
      console.info(JSON.stringify({ message: 'processed', eventType: e.eventType, memoryRecordId: e.memoryRecordId }));
    } catch (err) {
      console.error(JSON.stringify({ message: 'failed', sequenceNumber: record.kinesis.sequenceNumber, error: String(err) }));
      // Report the first failure so Lambda retries from there and shard order is kept.
      return { batchItemFailures: [{ itemIdentifier: record.kinesis.sequenceNumber }] };
    }
  }
  return { batchItemFailures: [] };
};
