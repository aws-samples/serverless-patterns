// Turns the Kafka client.properties file written by refresh_token.sh into a
// KafkaJS client config. Both the SASL/OAUTHBEARER patterns (static Cognito / AWS
// web-identity token embedded in the properties file) and the MSK IAM pattern
// (token minted on demand by the AWS MSK IAM SASL signer) are supported, so the
// producer/consumer code is identical across all three patterns.
import { readFileSync, existsSync } from "node:fs";

function loadProperties(path) {
  const props = {};
  for (const raw of readFileSync(path, "utf-8").split("\n")) {
    const line = raw.trim();
    if (!line || line.startsWith("#") || !line.includes("=")) continue;
    const idx = line.indexOf("=");
    props[line.slice(0, idx).trim()] = line.slice(idx + 1).trim();
  }
  return props;
}

export function clientConfig(propertiesFile) {
  const props = loadProperties(propertiesFile);
  const config = { brokers: props["bootstrap.servers"].split(",") };

  // TLS trust anchor: self-managed brokers present a self-signed cert whose CA PEM
  // sits on the client instance; MSK presents a publicly-trusted Amazon cert, so we
  // fall back to the default system trust store. The self-signed cert carries the
  // broker IPs as SANs, but skip hostname checking to stay robust if a broker is
  // reached by an address not listed in the SANs.
  const caCert = process.env.KAFKA_CA_CERT || "/home/ec2-user/kafka.crt";
  if (existsSync(caCert)) {
    config.ssl = { ca: [readFileSync(caCert, "utf-8")], checkServerIdentity: () => undefined };
  } else {
    config.ssl = true;
  }

  const region = process.env.AWS_REGION || "us-west-2";
  const jaas = props["sasl.jaas.config"] || "";
  const tokenMatch = jaas.match(/oauth\.access\.token="([^"]+)"/);
  if (tokenMatch) {
    const token = tokenMatch[1];
    config.sasl = { mechanism: "oauthbearer", oauthBearerProvider: async () => ({ value: token }) };
  } else {
    // MSK IAM: mint an OAUTHBEARER token via the AWS signer, honoring an awsRoleArn
    // from the JAAS config if present.
    const roleMatch = jaas.match(/awsRoleArn="([^"]+)"/);
    config.sasl = {
      mechanism: "oauthbearer",
      oauthBearerProvider: async () => {
        const signer = await import("aws-msk-iam-sasl-signer-js");
        const { token } = roleMatch
          ? await signer.generateAuthTokenFromRole({ region, awsRoleArn: roleMatch[1] })
          : await signer.generateAuthToken({ region });
        return { value: token };
      },
    };
  }
  return config;
}
