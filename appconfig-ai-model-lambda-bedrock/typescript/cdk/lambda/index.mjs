// Reads the deployed AI model invocation configuration from the AWS AppConfig Agent Lambda extension
// and maps it onto an Amazon Bedrock Converse request.
import { BedrockRuntimeClient, ConverseCommand } from '@aws-sdk/client-bedrock-runtime';

const CONFIG_PATH = process.env.CONFIG_PATH;
if (!CONFIG_PATH) throw new Error('CONFIG_PATH is not set');
const AGENT_URL = `http://localhost:${process.env.AWS_APPCONFIG_EXTENSION_HTTP_PORT ?? '2772'}${CONFIG_PATH}`;
const MAX_PROMPT_CHARS = 2000;

const bedrock = new BedrockRuntimeClient({ maxAttempts: 2 });

async function loadConfig() {
  try {
    const res = await fetch(AGENT_URL, { signal: AbortSignal.timeout(3000) });
    if (!res.ok) throw new Error(`AppConfig Agent returned HTTP ${res.status}: ${await res.text()}`);
    return await res.json();
  } catch (err) {
    console.error(JSON.stringify({ message: 'Could not read the model configuration', error: err.name, detail: err.message }));
    throw err;
  }
}

export const handler = async (event) => {
  // Bad input is the caller's problem, not the configuration's: return it without throwing, so it does not
  // count as a function error and cannot trigger a configuration rollback.
  const prompt = typeof event?.prompt === 'string' ? event.prompt.trim() : '';
  if (!prompt || prompt.length > MAX_PROMPT_CHARS) {
    return { error: `prompt must be a non-empty string of at most ${MAX_PROMPT_CHARS} characters` };
  }

  const cfg = await loadConfig();
  const configured = cfg.messages ?? [];
  const system = configured.filter((m) => m.role === 'system').map((m) => ({ text: m.content }));
  const turns = configured.filter((m) => m.role !== 'system').map((m) => ({ role: m.role, content: [{ text: m.content }] }));

  try {
    const out = await bedrock.send(new ConverseCommand({
      modelId: cfg.model,
      ...(system.length ? { system } : {}),
      messages: [...turns, { role: 'user', content: [{ text: prompt }] }],
      ...(cfg.inferenceParameters ? { inferenceConfig: cfg.inferenceParameters } : {}),
      ...(cfg.customParameters ? { additionalModelRequestFields: cfg.customParameters } : {}),
    }));
    const answer = (out.output?.message?.content ?? []).map((c) => c.text ?? '').join('');
    return { model: cfg.model, inferenceParameters: cfg.inferenceParameters ?? {}, answer, usage: out.usage };
  } catch (err) {
    // Rethrow: the function error is the signal the CloudWatch alarm and the AppConfig rollback rely on.
    console.error(JSON.stringify({ message: 'Converse failed', model: cfg.model, error: err.name, detail: err.message }));
    throw err;
  }
};
