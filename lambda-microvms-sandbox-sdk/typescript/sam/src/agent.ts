// SPDX-License-Identifier: MIT-0
// Optional (EnableAgent=true, after build-agent-image.ts): run a coding agent
// (OpenCode) inside the sandbox. The model credential, a short-term Amazon
// Bedrock API key, is stored in AWS Secrets Manager and only reaches Bedrock
// through the secrets gateway that runs in the sandbox agent: code in the
// sandbox can use the key but cannot read it, and the sandbox has no other
// Internet access.
import {
  CreateSecretCommand,
  PutSecretValueCommand,
  ResourceExistsException,
  SecretsManagerClient,
} from "@aws-sdk/client-secrets-manager";
import { getTokenProvider } from "@aws/bedrock-token-generator";
import { AgentLimits, AgentModel, AgentSpec, Sandbox, bedrockGateway } from "rayito";

const stack = process.env["STACK_NAME"];
const region = process.env["AWS_REGION"];
const modelId = process.env["MODEL_ID"] ?? "us.anthropic.claude-haiku-4-5-20251001-v1:0";
if (!stack || !region) {
  throw new Error("export STACK_NAME=<stack name> AWS_REGION=<region>");
}

// 1. Mint a short-term Bedrock API key (valid up to 12 hours) and store it.
// Rayito resolves secret names under the rayito/ prefix.
const secretName = `${stack}-bedrock-key`;
const secretValue = `Bearer ${await getTokenProvider({ region })()}`;
const secrets = new SecretsManagerClient({ region });
try {
  await secrets.send(new CreateSecretCommand({ Name: `rayito/${secretName}`, SecretString: secretValue }));
} catch (error) {
  if (!(error instanceof ResourceExistsException)) throw error;
  await secrets.send(new PutSecretValueCommand({ SecretId: `rayito/${secretName}`, SecretString: secretValue }));
}

// 2. A sandbox without Internet access whose only way out is the gateway,
// restricted to the Converse API of this one model and 30 calls per minute.
await using sbx = await Sandbox.create({
  template: `${stack}-agent`,
  timeoutMs: 15 * 60_000,
  allowInternetAccess: false,
  gateways: {
    bedrock: bedrockGateway(secretName, { region, models: [modelId], ratePerMinute: 30 }),
  },
});
await sbx.files.write("/home/user/project/app.py", "def add(a, b):\n    return a - b\n");

// 3. The agent edits files and runs commands inside the MicroVM.
const spec = new AgentSpec({
  model: new AgentModel({ provider: "bedrock", id: modelId, gateway: "bedrock", region }),
  instructions: "Work only inside /home/user/project. Be brief.",
});
const result = await sbx.agent.run("Fix the bug in app.py and check it with python3 -c.", {
  spec,
  workdir: "/home/user/project",
  limits: new AgentLimits({ maxSteps: 15, timeoutMs: 5 * 60_000 }),
});
console.log("agent:", result.text);
console.log("steps:", result.steps, "tokens:", result.usage.total);
console.log("app.py now:\n" + (await sbx.files.read("/home/user/project/app.py")));
