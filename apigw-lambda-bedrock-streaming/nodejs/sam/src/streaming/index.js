import { BedrockRuntimeClient, InvokeModelWithResponseStreamCommand } from "@aws-sdk/client-bedrock-runtime";

const bedrockClient = new BedrockRuntimeClient({ 
    region: process.env.BEDROCK_REGION || 'us-east-1' 
});

const streamifyResponse = globalThis.awslambda?.streamifyResponse;
const HttpResponseStream = globalThis.awslambda?.HttpResponseStream;

if (!streamifyResponse || !HttpResponseStream) {
    throw new Error('Lambda streaming functionality not available. Ensure you are using Node.js 20.x or later.');
}

export const handler = streamifyResponse(async (event, responseStream, context) => {
    console.log('Event:', JSON.stringify(event, null, 2));
    
    try {
        // Set up HTTP response metadata
        const httpResponseMetadata = {
            statusCode: 200,
            headers: {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            }
        };

        // Create the response stream with metadata
        responseStream = HttpResponseStream.from(responseStream, httpResponseMetadata);

        // Extract the message from the request body
        const body = JSON.parse(event.body || '{}');
        const prompt = body.message || body.prompt || 'Hello, how can I help you?';
        
        // Configure the model parameters
        const modelId = 'global.anthropic.claude-sonnet-4-5-20250929-v1:0';
        const payload = {
            anthropic_version: "bedrock-2023-05-31",
            max_tokens: 1000,
            messages: [
                {
                    role: "user",
                    content: prompt
                }
            ]
        };

        // Create the command for streaming response
        const command = new InvokeModelWithResponseStreamCommand({
            modelId: modelId,
            body: JSON.stringify(payload),
            contentType: 'application/json',
            accept: 'application/json'
        });

        // Invoke the model with streaming
        const response = await bedrockClient.send(command);
        
        // Stream the response chunks as they arrive
        if (response.body) {
            for await (const chunk of response.body) {
                if (chunk.chunk?.bytes) {
                    const chunkData = JSON.parse(new TextDecoder().decode(chunk.chunk.bytes));
                    if (chunkData.type === 'content_block_delta' && chunkData.delta?.text) {
                        responseStream.write(chunkData.delta.text);
                    }
                }
            }
        }

        // End the response stream
        responseStream.end();

    } catch (error) {
        console.error('Error:', error);
        
        // Set error response metadata
        const errorResponseMetadata = {
            statusCode: 500,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        };

        responseStream = HttpResponseStream.from(responseStream, errorResponseMetadata);
        responseStream.write(JSON.stringify({
            error: 'Internal server error',
            message: error.message
        }));
        responseStream.end();
    }
});