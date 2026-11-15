import {
  withDurableExecution,
  DurableContext,
} from '@aws/durable-execution-sdk-js';
import { BedrockAgentCoreClient, InvokeAgentRuntimeCommand } from "@aws-sdk/client-bedrock-agentcore";

const AGENT_RUNTIME_ARN = process.env.AGENT_RUNTIME_ARN!;

const client = new BedrockAgentCoreClient();

interface AgentEvent {
  city: string;
}

interface TripRequest {
  label: string;
  prompt: string;
}

async function invokeAgentEndpoint(payload: Record<string, unknown>): Promise<string> {
  const command = new InvokeAgentRuntimeCommand({
    agentRuntimeArn: AGENT_RUNTIME_ARN,
    payload: Buffer.from(JSON.stringify(payload)),
  });

  const response = await client.send(command);
  if (!response.response) {
    throw new Error('No response received from agent runtime');
  }
  return response.response.transformToString();
}

/**
 * Durable function that plans two trips in parallel using context.map.
 *
 * Flow:
 * 1. Builds two trip-planning prompts (weekend + weeklong) for the given city
 * 2. Maps over them in parallel, each using waitForCallback to invoke the agent
 * 3. Combines the two results into a single response
 */
export const handler = withDurableExecution(
  async (event: AgentEvent, context: DurableContext) => {
    const { city } = event;
    context.logger.info('Starting parallel trip planning', { city });

    const tripRequests: TripRequest[] = [
      {
        label: 'weekend',
        prompt: `Create a detailed agenda for a weekend trip to ${city}. Include activities, restaurants, and timing for each day.`,
      },
      {
        label: 'weeklong',
        prompt: `Create a detailed agenda for a weeklong trip to ${city}. Include activities, restaurants, and timing for each day.`,
      },
    ];

    // Process both trip requests in parallel, each with its own callback
    const mapResult = await context.map(
      'plan-trips',
      tripRequests,
      async (mapCtx, request) => {
        const agentResponse = await mapCtx.waitForCallback(
          `invoke-agent-${request.label}`,
          async (callbackId, ctx) => {
            ctx.logger.info('Sending prompt to AgentCore', {
              callbackId,
              label: request.label,
            });

            const confirmation = await invokeAgentEndpoint({
              prompt: request.prompt,
              callbackId,
            });

            ctx.logger.info('Agent confirmed receipt', { confirmation, label: request.label });
          },
          { timeout: { minutes: 5 } },
        );

        const parsed = typeof agentResponse === 'string'
          ? JSON.parse(agentResponse)
          : agentResponse;

        return { label: request.label, answer: parsed.answer };
      },
      { maxConcurrency: 2, itemNamer: (request) => `${city}-${request.label}` },
    );

    // Combine the two results
    const result = await context.step('combine-results', async () => {
      mapResult.throwIfError();
      const results = mapResult.getResults();

      const weekend = results.find((r) => r.label === 'weekend');
      const weeklong = results.find((r) => r.label === 'weeklong');

      return {
        city,
        weekendTrip: weekend?.answer,
        weeklongTrip: weeklong?.answer,
        timestamp: new Date().toISOString(),
      };
    });

    return result;
  },
);
