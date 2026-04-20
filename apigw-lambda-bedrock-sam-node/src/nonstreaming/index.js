import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

const bedrockClient = new BedrockRuntimeClient({ 
    region: process.env.BEDROCK_REGION || 'us-east-1' 
});

export const handler = async (event) => {
    console.log('Non-streaming Event:', JSON.stringify(event, null, 2));
    
    try {
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

        // Create the command for non-streaming response
        const command = new InvokeModelCommand({
            modelId: modelId,
            body: JSON.stringify(payload),
            contentType: 'application/json',
            accept: 'application/json'
        });

        // Invoke the model without streaming
        const response = await bedrockClient.send(command);
        
        // Parse the response
        const responseBody = JSON.parse(new TextDecoder().decode(response.body));
        const content = responseBody.content?.[0]?.text || 'No response generated';

        return {
            statusCode: 200,
            headers: {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            body: content
        };

    } catch (error) {
        console.error('Non-streaming Error:', error);
        
        return {
            statusCode: 500,
            headers: {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*'
            },
            body: `Error: ${error.message}`
        };
    }
};