
import {
    BedrockRuntimeClient,
    ConverseStreamCommand,
} from "@aws-sdk/client-bedrock-runtime";
import { AppSyncEventsRequestApiKey } from "../utils/appsyncRequest";
import { APIGatewayProxyEventV2, APIGatewayProxyHandler, APIGatewayProxyResult, APIGatewayProxyResultV2 } from "aws-lambda";

const REGION = process.env.REGION || 'eu-central-1'
const EVENTS_API_URL = process.env.EVENTS_API_URL || ""
const API_KEY = process.env.API_KEY || ""
const CHANNEL_NAME = process.env.CHANNEL_NAME || ""

const client = new BedrockRuntimeClient({ region: REGION })
const modelId = "anthropic.claude-3-haiku-20240307-v1:0"

export interface ChatRequest {
    userId: string
    prompt: string
}

export const handler = async (event: APIGatewayProxyEventV2) => {

    const body = JSON.parse(event.body ?? "") as ChatRequest

    // filter requests by checking if prompt is present
    if (!body.prompt) {
        throw Error("Missing prompt")
    }

    if (!body.userId) {
        throw Error("Missing userId")
    }

    const channelName = `/${CHANNEL_NAME}/${body.userId}`

    console.log("Final channel name: " + channelName)

    const command = new ConverseStreamCommand({
        modelId: modelId,
        messages: [{
            role: "user",
            content: [{ text: body.prompt }]
        }]
    })

    try {
        const response = await client.send(command)

        if (!response.stream) {
            throw Error("No Stream initiated")
        }

        let completion = ""

        for await (const line of response.stream) {
            if (line.contentBlockDelta) {

                // command towards appsync events api
                const res = await AppSyncEventsRequestApiKey({
                    config: {
                        url: EVENTS_API_URL,
                        region: REGION,
                        key: API_KEY
                    },
                    channelName: channelName,
                    events: [
                        {
                            data: line.contentBlockDelta.delta?.text
                        }
                    ]
                })

                // log result from events api call
                console.log(`For "${line.contentBlockDelta.delta?.text}":`, JSON.stringify(res))

                // add final completion
                completion += line.contentBlockDelta.delta?.text
            }
        }

        return {
            channelName: channelName,
            completion: completion
        }
    }

    catch (error) {
        throw Error("Error in lambda function:" + JSON.stringify(error))
    }

}