const {
    BedrockRuntimeClient,
    InvokeModelWithResponseStreamCommand,
  } = require("@aws-sdk/client-bedrock-runtime");

exports.handler = awslambda.streamifyResponse(
    async (event, responseStream, context) => {
        const lambdaRequestBody = JSON.parse(event.body);
        try {
            // Handle base64 encoded body from AWS SigV4 requests
            const body = event.isBase64Encoded ? 
                Buffer.from(event.body, 'base64').toString('utf-8') : 
                event.body;
            lambdaRequestBody = JSON.parse(body);
        } catch (error) {
            console.error('Error parsing request body:', error);
            responseStream.write("Invalid JSON in request body.");
            responseStream.end();
            return;
        }

        const prompt = lambdaRequestBody.prompt || '';
        if (prompt == '') {
            responseStream.write("No prompt provided.");
            responseStream.end();
        }

        const httpResponseMetadata = {
            statusCode: 200,
            headers: {
                "Content-Type": "text/html",
                "X-Custom-Header": "Example-Custom-Header"
            }
        };

         const
            maxTokens = 2500,
            temperature = .7,
            topP = 1,
            anthropicVersion = "bedrock-2023-05-31"
            modelId = 'anthropic.claude-3-haiku-20240307-v1:0',
            contentType = 'application/json',
            accept = '*/*';

        try {
            responseStream = awslambda.HttpResponseStream.from(responseStream, httpResponseMetadata);

            const bedrockruntime = new BedrockRuntimeClient({
                region: 'us-west-2',
                apiVersion: '2023-09-30',
                credentials: {
                    accessKeyId: process.env.BEDROCK_AWS_ACCESS_KEY_ID, // setting this in template file
                    secretAccessKey: process.env.BEDROCK_AWS_SECRET_ACCESS_KEY
                }
            });

            const llmRequestBody = {
                max_tokens: maxTokens,
                messages: [
                    {
                        role: "user",
                        content: prompt
                    }
                ],
                temperature,
                top_p: topP
                anthropic_version: anthropicVersion,
            };

            const params = {
                body: Buffer.from(JSON.stringify(llmRequestBody)),
                modelId,
                contentType,
                accept
            };

            const command = new InvokeModelWithResponseStreamCommand(params);
            // streaming response
            const data = await bedrockruntime.send(command);
            const actualStream = data.body.options.messageStream;
            // parse actual stream to send response
            responseStream = awslambda.HttpResponseStream.from(responseStream, httpResponseMetadata);
            const chunks = []
            for await (const value of actualStream) {
                const jsonString = new TextDecoder().decode(value.body);
                const base64encoded = JSON.parse(jsonString).bytes;
                const decodedString = Buffer.from(base64encoded, "base64").toString("utf-8");
                
                try {
                    const chunk = JSON.parse(decodedString);
                    if (chunk.type === 'content_block_delta' && chunk.delta?.text) {
                        const text = chunk.delta.text;
                        chunks.push(text);
                        responseStream.write(text);
                    }
                } catch (error) {
                    console.error(error);
                    responseStream.write(null);
                    responseStream.end();
                }
            }
            console.log("stream ended: ", chunks.join(''))
            responseStream.end();
        } catch (error) {
            console.error(error);
            throw error;
        }
    }
);