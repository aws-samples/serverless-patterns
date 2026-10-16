// Publishes a given number of JSON "person" messages to a Kafka topic, using
// SASL/OAUTHBEARER authentication (the token comes from the properties file written
// by refresh_token.sh).
//
// Usage: node producer.mjs <properties-file> <topic> <count>
import { Kafka } from "kafkajs";

import { clientConfig } from "./kafkaConfig.mjs";
import { randomPerson } from "./person.mjs";

const [, , propertiesFile, topic, countArg] = process.argv;
if (!propertiesFile || !topic || !countArg) {
  console.error("Usage: node producer.mjs <properties-file> <topic> <count>");
  process.exit(2);
}
const count = parseInt(countArg, 10);

const kafka = new Kafka({ clientId: "kafka-json-producer", ...clientConfig(propertiesFile) });
const producer = kafka.producer();
await producer.connect();

console.log(`Producing ${count} JSON message(s) to topic '${topic}'...`);
for (let i = 0; i < count; i++) {
  const person = randomPerson();
  const payload = JSON.stringify(person);
  const [metadata] = await producer.send({
    topic,
    acks: -1,
    messages: [{ key: person.email, value: payload }],
  });
  console.log(`Sent [${i + 1}/${count}] partition=${metadata.partition} baseOffset=${metadata.baseOffset} : ${payload}`);
}
await producer.disconnect();
console.log(`Done. Sent ${count} message(s) to '${topic}'.`);
