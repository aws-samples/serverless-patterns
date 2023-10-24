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

describe('Bedrock Model invoked', () => {
    test("The user is able to perform the ask mutation with the API_KEY", async() => {
        const mutationPromise = await AppSyncRequestApiKey({
            config: {
                url: APPSYNC_URL,
                region: REGION,
                key: APPSYNC_API_KEY
            },
            operation: {
                operationName: "MyMutation",
                query: `mutation MyMutation($prompt: String!) {
                    invoke(prompt: $prompt)
                }`,
                variables: {
                    prompt: 'What is the capital of France?'
                }
            }
        }) as GraphQLResult<{invoke: {completion: string}}>
    
        console.log(mutationPromise)
        if (mutationPromise?.data) {
            expect(mutationPromise.data.invoke).toBeTruthy()
        } else {
            throw new Error("No data returned")
        }
    });

})
