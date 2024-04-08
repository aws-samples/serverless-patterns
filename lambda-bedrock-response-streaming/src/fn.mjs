/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { BedrockRuntimeClient, InvokeModelWithResponseStreamCommand } from "@aws-sdk/client-bedrock-runtime";

const bedrock = new BedrockRuntimeClient({ region: "us-east-1" });

// helpers
function getBody(event) {
    let body = event.isBase64Encoded ? parseBase64(event.body) : event.body;
    console.log(JSON.stringify(body));
    return body;
}

function parseBase64(message) {
    return JSON.parse(Buffer.from(message, "base64").toString("utf-8"));
}

// bedrock: prep claude params
function getInvokeParamsForClaudeV2(body) {
    const modelParams = body.modelParams;
    const prompt = `\n\nHuman:${modelParams.prompt}Assistant:`;
    modelParams.prompt = prompt;

    const bedrockParams = body.bedrockParams;
    bedrockParams.body = JSON.stringify(modelParams);
    bedrockParams.responseStream = true;
    return bedrockParams;
}

// bedrock: helpers
async function doStreamingWithAwsSdk(params, responseStream) {
    const command = new InvokeModelWithResponseStreamCommand(params);
    const response = await bedrock.send(command);
    const chunks = [];
    for await (const chunk of response.body) {
        const parsed = parseBase64(chunk.chunk.bytes);
        chunks.push(parsed.completion);
        responseStream.write(parsed.completion);
    }
    console.log(chunks.join(''));
    responseStream.end();
}

// bedrock: invoke model
async function doBedrock(body, responseStream) {
    const params = getInvokeParamsForClaudeV2(body);
    console.log(JSON.stringify(params));
    await doStreamingWithAwsSdk(params, responseStream);
}

export const handler = awslambda.streamifyResponse(async (event, responseStream, _context) => {
    console.log(JSON.stringify(event));
    const body = getBody(event);
    await doBedrock(body, responseStream);
    console.log(JSON.stringify({"status": "complete"}));
});