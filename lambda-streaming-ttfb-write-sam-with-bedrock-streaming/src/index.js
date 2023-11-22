exports.handler = awslambda.streamifyResponse(
    async (event, responseStream, context) => {
        const lambdaRequestBody = JSON.parse(event.body);
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
            stopSequences = ["\n\nHuman:"],
            anthropicVersion = "bedrock-2023-05-31",
            modelId = 'anthropic.claude-v2',
            contentType = 'application/json',
            accept = '*/*';

        const formattedPrompt = f`Human: ${prompt}\n\nAssistant:`

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
                prompt: formattedPrompt,
                max_tokens_to_sample: maxTokens,
                temperature,
                top_p: topP,
                stop_sequences: stopSequences,
                anthropic_version: anthropicVersion
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
                const jsonString = new TextDecoder().decode(value.body); // body is a Uint8Array. jsonString->'{"bytes":"eyJjb21wbGV0aW9uIjoiIEkiLCJzdG9wX3JlYXNvbiI6bnVsbH0="}'
                const base64encoded = JSON.parse(jsonString).bytes; // base64 encoded string. 
                const decodedString = base64ToUtf8(base64encoded);
                try {
                    const streamingCompletion = JSON.parse(decodedString).completion;
                    chunks.push(streamingCompletion)
                    responseStream.write(streamingCompletion)
                } catch (error) {
                    console.error(error);
                    responseStream.write(null);
                    responseStream.end()
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