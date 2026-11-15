import { AppSyncResolverEvent } from "aws-lambda";
import { BedrockRuntimeClient, ConverseStreamCommand } from "@aws-sdk/client-bedrock-runtime";
import { AppSyncRequestIAM } from "./appsyncRequest";

const GRAPHQL_URL = process.env.GRAPHQL_URL || "";
const REGION = process.env.REGION || "us-east-1";
const MODEL_ID = process.env.MODEL_ID || "";

const bedrock = new BedrockRuntimeClient({ region: REGION });

const sendChunk = (chatId: string, data: string) =>
    AppSyncRequestIAM({
        config: {
            url: GRAPHQL_URL,
            region: REGION,
        },
        operation: {
            query: `mutation MyMutation($chatId: String!, $data: String!) {
                send(chatId: $chatId, data: $data) {
                    chatId
                    data
                }
            }`,
            operationName: "MyMutation",
            variables: { chatId, data }
        }
    });

exports.handler = async (event: AppSyncResolverEvent<{ chatId: string, prompt: string }>) => {
    const response = await bedrock.send(new ConverseStreamCommand({
        modelId: MODEL_ID,
        messages: [{ role: "user", content: [{ text: event.arguments.prompt || "" }] }],
        inferenceConfig: { maxTokens: 1024 },
    }));

    // Forward each text chunk to subscribers as it arrives. Other stream
    // events (message start/stop, metadata, reasoning) are not sent.
    for await (const item of response.stream ?? []) {
        const text = item.contentBlockDelta?.delta?.text;
        if (text) {
            await sendChunk(event.arguments.chatId, text);
        }
    }
}
