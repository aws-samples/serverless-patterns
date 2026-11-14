import { AppSyncRequestApiKey, GraphQLResult } from "../src/appsyncRequest"
import { readFileSync } from "fs"
let APPSYNC_URL = ""
let APPSYNC_API_KEY = ""
let REGION = ""

beforeAll(() => {
    const file = readFileSync("cdk-outputs.json");
    const data = JSON.parse(file.toString())
    APPSYNC_URL = data.BackendStack.GraphQLApiURL
    APPSYNC_API_KEY = data.BackendStack.GraphQLApiKey
    REGION = data.BackendStack.Region
  });

describe("AppSync connections", () => {
    test("The user is able to perform the ask mutation with the API_KEY", async() => {
        const mutationPromise = await AppSyncRequestApiKey({
            config: {
                url: APPSYNC_URL,
                region: REGION,
                key: APPSYNC_API_KEY
            },
            operation: {
                operationName: "MyMutation",
                query: `mutation MyMutation($chatId: String!, $prompt: String!) {
                    ask(chatId: $chatId, prompt: $prompt) {
                        chatId
                        data
                    }
                }`,
                variables: {
                    chatId: 'test',
                    prompt: 'What is the capital of France?'
                }
            }
        })
    
        console.log(mutationPromise)
        expect(mutationPromise.data).toBeDefined()
    });

    test("The user is unable to perform the send mutation with the API KEY",async () => {
        const mutationPromise = await AppSyncRequestApiKey({
            config: {
                url: APPSYNC_URL,
                region: REGION,
                key: APPSYNC_API_KEY
            },
            operation: {
                operationName: "MyMutation",
                query: `mutation MyMutation($chatId: String!, $data: String!) {
                    send(chatId: $chatId, data: $data) {
                        chatId
                        data
                    }
                }`,
                variables: {
                    chatId: 'test',
                    data: 'Paris is the capital of France'
                }
            }
        }) as GraphQLResult
    
        console.log(mutationPromise)
        expect(mutationPromise?.errors?.shift()?.errorType).toBe("Unauthorized")
    })
})

