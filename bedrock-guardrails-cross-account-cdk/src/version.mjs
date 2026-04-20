import pkg from '@aws-sdk/client-bedrock';
const { BedrockClient, CreateGuardrailVersionCommand } = pkg;

const client = new BedrockClient();

export async function onEvent(event) {
  const guardrailIdentifier = event.ResourceProperties.GuardrailIdentifier;

  if (event.RequestType === 'Create' || event.RequestType === 'Update') {
    const response = await client.send(new CreateGuardrailVersionCommand({
      guardrailIdentifier,
    }));

    return {
      PhysicalResourceId: response.version,
      Data: { Version: response.version },
    };
  }

  return { PhysicalResourceId: event.PhysicalResourceId };
}
