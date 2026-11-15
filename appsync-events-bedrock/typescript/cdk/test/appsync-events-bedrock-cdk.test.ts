import { AppSyncEventsRequestApiKey } from "../utils/appsyncRequest"
import { readFileSync } from "fs"
import { makeRequest } from "../utils/apigwRequest";

describe("AppSync Event API with API_KEY auth mode", () => {

    const file = readFileSync("cdk-outputs.json");
    const data = JSON.parse(file.toString())
    const stackName = "AppsyncEventsBedrockCdkStack"

    process.env.API_KEY = data[stackName].ApiKey
    process.env.EVENTS_API_HTTP = data[stackName].EventsApiHttp
    process.env.EVENTS_API_REALTIME = data[stackName].EventsApiRealtime
    process.env.REGION = data[stackName].Region
    process.env.CHANNEL_NAME = data[stackName].ChannelName
    process.env.CHAT_API_URL = data[stackName].ChatApiUrl

    test("The user is able to publish a message", async () => {

        if (!process.env.EVENTS_API_HTTP) throw new Error("EVENTS_API_HTTP is not defined")
        if (!process.env.API_KEY) throw new Error("API_KEY is not defined")
        if (!process.env.CHANNEL_NAME) throw new Error("CHANNEL_NAME is not defined")
        if (!process.env.REGION) throw new Error("REGION is not defined")

        const res = await AppSyncEventsRequestApiKey({
            config: {
                url: process.env.EVENTS_API_HTTP,
                region: process.env.REGION,
                key: process.env.API_KEY
            },
            channelName: process.env.CHANNEL_NAME,
            events: [
                {
                    data: "sample data"
                }
            ]
        })

        console.log(res)
        expect(res.failed.length).toBe(0)
    });

    test("The user is able to invoke the lambda function through the api gateway", async () => {

        if (!process.env.CHAT_API_URL) throw new Error("CHAT_API_URL is not defined")
        if (!process.env.API_KEY) throw new Error("API_KEY is not defined")
        if (!process.env.EVENTS_API_HTTP) throw new Error("EVENTS_API_HTTP is not defined")
        if (!process.env.EVENTS_API_REALTIME) throw new Error("EVENTS_API_REALTIME is not defined")

        const requestBody = {
            userId: "test-user",
            prompt: "What is the capital of France?"
        }

        const res = await makeRequest({
            url: process.env.CHAT_API_URL,
            method: "POST",
            apiKey: process.env.API_KEY
        }, requestBody
        )

        console.log(res)
        expect(res.statusCode).toBe(200)

    });
})

