// Consumes JSON messages from a Kafka topic and prints each one parsed and
// pretty-printed, using SASL/OAUTHBEARER authentication (the token comes from the
// properties file written by refresh_token.sh).
//
// Usage: node consumer.mjs <properties-file> <topic> [group-id]
import { Kafka } from "kafkajs";

import { clientConfig } from "./kafkaConfig.mjs";

const [, , propertiesFile, topic, groupArg] = process.argv;
if (!propertiesFile || !topic) {
  console.error("Usage: node consumer.mjs <properties-file> <topic> [group-id]");
  process.exit(2);
}
const groupId = groupArg || "kafka-oauth-consumer-group";

const kafka = new Kafka({ clientId: "kafka-json-consumer", ...clientConfig(propertiesFile) });
const consumer = kafka.consumer({ groupId });
await consumer.connect();
await consumer.subscribe({ topic, fromBeginning: true });

console.log(`Consuming from topic '${topic}' (group '${groupId}'). Press Ctrl-C to stop.`);
await consumer.run({
  eachMessage: async ({ partition, message }) => {
    const raw = message.value.toString();
    let pretty;
    try {
      pretty = JSON.stringify(JSON.parse(raw), null, 2);
    } catch {
      pretty = raw;
    }
    const key = message.key ? message.key.toString() : null;
    console.log(`\n--- message partition=${partition} offset=${message.offset} key=${key} ---\n${pretty}`);
  },
});

for (const signal of ["SIGINT", "SIGTERM"]) {
  process.on(signal, async () => {
    await consumer.disconnect();
    console.log("Consumer closed.");
    process.exit(0);
  });
}
