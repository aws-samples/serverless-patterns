// Lambda delivers a batch of Kafka messages. The event has an eventSource and a
// "records" field: a map keyed by "<topic>-<partition>" whose values are lists of
// individual messages. One batch can span multiple partitions.
//
// This handler flattens that structure into a list of message objects, logs each
// one, and (when DYNAMODB_TABLE_NAME is set) writes the Kafka metadata plus the
// parsed JSON payload fields to DynamoDB.
//
// The AWS SDK v3 is included in the Lambda Node.js managed runtime and is imported
// lazily, so this module (and its unit tests) load without the SDK present.

let _sdk;
let _client;

// `sam local invoke` sets AWS_SAM_LOCAL=true. Local runs write to DynamoDB Local
// (started by scripts/local_dynamodb.sh) so they never touch the real table.
const LOCAL_DYNAMODB_ENDPOINT = "http://dynamodb-local:8000";

async function putItem(params) {
  if (!_sdk) _sdk = await import("@aws-sdk/client-dynamodb");
  if (!_client) {
    const local = process.env.AWS_SAM_LOCAL === "true";
    _client = new _sdk.DynamoDBClient(local ? { endpoint: LOCAL_DYNAMODB_ENDPOINT } : {});
  }
  await _client.send(new _sdk.PutItemCommand(params));
}

function decode(value) {
  // Kafka record keys and values arrive base64-encoded.
  if (value === null || value === undefined) return "null";
  return Buffer.from(value, "base64").toString("utf-8");
}

export function parseRecords(event) {
  const messages = [];
  for (const records of Object.values(event.records || {})) {
    for (const r of records) {
      const headers = [];
      for (const header of r.headers || []) {
        for (const [k, v] of Object.entries(header)) {
          const value = Array.isArray(v) ? Buffer.from(v).toString("utf-8") : String(v);
          headers.push({ key: k, value });
        }
      }
      messages.push({
        topic: r.topic,
        partition: r.partition,
        offset: r.offset,
        timestamp: r.timestamp,
        timestampType: r.timestampType,
        key: r.key ?? null,
        value: r.value ?? null,
        decodedKey: decode(r.key),
        decodedValue: decode(r.value),
        headers,
      });
    }
  }
  return messages;
}

async function writeToDynamoDb(message) {
  const tableName = process.env.DYNAMODB_TABLE_NAME;
  if (!tableName) return;
  const item = {
    topicPartition: { S: `${message.topic}-${message.partition}` },
    offset: { N: String(message.offset) },
    topic: { S: message.topic },
    partition: { N: String(message.partition) },
    timestamp: { N: String(message.timestamp) },
  };
  if (message.timestampType) item.timestampType = { S: message.timestampType };
  if (message.decodedKey !== null && message.decodedKey !== undefined) item.key = { S: message.decodedKey };
  if (message.decodedValue !== null && message.decodedValue !== undefined) item.value = { S: message.decodedValue };
  // Store each top-level primitive field of the JSON payload as its own attribute.
  try {
    const parsed = JSON.parse(message.decodedValue);
    if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
      for (const [k, v] of Object.entries(parsed)) {
        if (["string", "number", "boolean"].includes(typeof v)) item[k] = { S: String(v) };
      }
    }
  } catch {
    // Not a JSON payload - the raw value is already stored under "value".
  }
  await putItem({ TableName: tableName, Item: item });
  console.log(`Wrote message to DynamoDB table ${tableName} `
    + `(topicPartition=${item.topicPartition.S}, offset=${item.offset.N})`);
}

export const lambdaHandler = async (event) => {
  const messages = parseRecords(event);
  for (const message of messages) {
    console.log(`Received this message from Kafka - ${JSON.stringify(message)}`);
    await writeToDynamoDb(message);
  }
  console.log(`All messages in this batch = ${JSON.stringify(messages)}`);
  return "200 OK";
};
