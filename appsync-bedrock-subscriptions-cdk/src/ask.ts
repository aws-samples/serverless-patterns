import { AppSyncResolverEvent } from "aws-lambda";
import { ChatBedrock } from "@langchain/community/chat_models/bedrock";
import { AppSyncRequestIAM } from "./appsyncRequest";
import { StringOutputParser } from "@langchain/core/output_parsers";
const GRAPHQL_URL = process.env.GRAPHQL_URL || "";
const REGION = process.env.REGION || 'us-east-1';

exports.handler = async (event: AppSyncResolverEvent<{ chatId: string, prompt: string }>) => {
    const chat = new ChatBedrock({
        model: "anthropic.claude-v2",
        region: REGION,
    })

    const parser = new StringOutputParser();

    const stream = await chat
        .pipe(parser)
        .stream([
            "\n\nHuman:",
            event.arguments.prompt || "",
            "\n\nAssistant:"
        ])

    for await (const line of stream) {
        await AppSyncRequestIAM({
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
                variables: { chatId: event.arguments.chatId, data: line }
            }
        })
    }
  }
