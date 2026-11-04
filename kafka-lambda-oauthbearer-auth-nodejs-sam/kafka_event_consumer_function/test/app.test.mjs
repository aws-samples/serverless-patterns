import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

import { parseRecords, lambdaHandler } from "../app.mjs";

const here = path.dirname(fileURLToPath(import.meta.url));
const event = JSON.parse(readFileSync(path.join(here, "..", "..", "events", "event.json"), "utf-8"));

test("parseRecords flattens and base64-decodes the batch", () => {
  const messages = parseRecords(event);
  assert.equal(messages.length, 10);
  assert.equal(messages[0].topic, "KafkaOAuthBearerLambdaTopic");
  assert.equal(messages[0].partition, 1);
  assert.equal(messages[0].offset, 208);
  assert.equal(messages[0].timestamp, 1790996330920);
  assert.equal(messages[0].timestampType, "CREATE_TIME");
  assert.equal(messages[0].decodedKey, "jthomas@example.org");
  const person = JSON.parse(messages[0].decodedValue);
  assert.equal(person.firstName, "George");
  assert.equal(person.lastName, "Yang");
  assert.equal(person.email, "jthomas@example.org");
  assert.equal(messages[1].offset, 209);
  assert.equal(messages[1].decodedKey, "robert96@example.org");
});

test("handler returns 200 OK and skips DynamoDB when no table is set", async () => {
  delete process.env.DYNAMODB_TABLE_NAME;
  assert.equal(await lambdaHandler(event), "200 OK");
});
