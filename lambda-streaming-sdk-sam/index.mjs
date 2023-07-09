import {
    LambdaClient,
    InvokeWithResponseStreamCommand,
    paginateListFunctions
} from "@aws-sdk/client-lambda";

// Preview region is in EU-WEST-1
const REGION = "eu-west-1";

const lambda = new LambdaClient({ region: REGION });

// Get the example streaming function ARN
const getExampleFunctionArn = async (functionName) => {
    const paginatorConfig = {
        client: lambda,
        pageSize: 50
    };

    const listFunctionParams = {};

    try {
        const paginator = paginateListFunctions(paginatorConfig, listFunctionParams);

        const EXAMPLE_FUNCTION_NAME_PREFIX = `lambda-streaming-sdk-sam-${functionName}`;
        for await (const page of paginator) {
            if (!page.Functions) return;

            let result;

            page.Functions.forEach(fn => {
                if (fn.FunctionName.startsWith(EXAMPLE_FUNCTION_NAME_PREFIX)) {
                    result = fn.FunctionArn;
                    return;
                }
            });

            return result;
        } 
    } catch (err) {
        console.log("Error", err);
    }
}

function Decodeuint8arr(uint8array) {
    return new TextDecoder("utf-8").decode(uint8array);
}

const main = async (functionName) => {
    const targetFunctionArn = await getExampleFunctionArn(functionName);

    if (!targetFunctionArn) {
        console.log("Could not find the reference streaming function. Have you deployed it yet?");
        return;
    }

    const params = {
        FunctionName: targetFunctionArn,
        LogType: "Tail"
    };

    try {
        // Call the InvokeWithResponseStream API
        const response = await lambda.send(new InvokeWithResponseStreamCommand(params));

        // The response should contain an EventStream Async Iterator
        const events = response.EventStream;

        // Each `event` is a chunk of the streamed response.
        for await (const event of events) {
            // There are two types of events you can get on a stream.
            console.log(event);

            // `PayloadChunk`: These contain the actual raw bytes of the chunk
            // It has a single property: `Payload`
            if (event.PayloadChunk) {
                // Decode the raw bytes into a string a human can read
                console.log(Decodeuint8arr(event.PayloadChunk.Payload));
            }

            // `InvokeComplete`: This event is sent when the function is done streaming.
            // It has the following properties:
            // `LogResult`: Contains the last 4KiB of execution logs as a base64 encoded
            //     string when Tail Logs are enabled.
            // `ErrorCode`: The error code if the function ran into an error mid-stream.
            // `ErrorDetails`: Additional details about the error if the function ran into
            //     an error mid-stream.
            if (event.InvokeComplete) {
                if (event.InvokeComplete.ErrorCode) {
                    console.log("Error Code:", event.InvokeComplete.ErrorCode);
                    console.log("Details:", event.InvokeComplete.ErrorDetails);
                }

                if (event.InvokeComplete.LogResult) {
                    const buff = Buffer.from(event.InvokeComplete.LogResult, 'base64');
                    console.log("Logs:", buff.toString("utf-8"));
                }
            }
        }
    } catch (err) {
        console.log("Error", err);
    }
}

// Happy path streaming example
console.log("Happy path streaming example");
await main("HappyPath");

// Midstream error example
console.log("Midstream error example");
await main("MidstreamError");

// Timeout example
console.log("Timeout example");
await main("Timeout");