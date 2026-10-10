// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

const { BedrockRuntimeClient, InvokeModelCommand } = require('@aws-sdk/client-bedrock-runtime');

const client = new BedrockRuntimeClient({ region: process.env.REGION });

exports.handler = async (event) => {
  console.log('Tool invocation received:', JSON.stringify(event));

  try {
    const body = typeof event.body === 'string' ? JSON.parse(event.body) : event;
    const prompt = body.prompt || body.arguments?.prompt || 'Hello, how can I help you today?';

    const response = await client.send(
      new InvokeModelCommand({
        modelId: process.env.MODEL_ID,
        contentType: 'application/json',
        accept: 'application/json',
        body: JSON.stringify({
          anthropic_version: 'bedrock-2023-05-31',
          max_tokens: 1024,
          messages: [
            {
              role: 'user',
              content: prompt,
            },
          ],
        }),
      })
    );

    const result = JSON.parse(new TextDecoder().decode(response.body));
    const text = result.content?.[0]?.text || '';

    return {
      statusCode: 200,
      body: JSON.stringify({
        result: text,
        model: process.env.MODEL_ID,
        usage: result.usage,
      }),
    };
  } catch (error) {
    console.error('Bedrock invocation failed:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: 'InferenceError',
        message: error.message || 'Failed to invoke Amazon Bedrock model',
      }),
    };
  }
};
