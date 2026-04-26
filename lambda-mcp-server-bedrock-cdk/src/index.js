const { BedrockRuntimeClient, InvokeModelCommand } = require('@aws-sdk/client-bedrock-runtime');

const client = new BedrockRuntimeClient();

// Stateless MCP Server on Lambda — implements MCP Streamable HTTP transport
// Supports: tools/list, tools/call, initialize
exports.handler = async (event) => {
  const method = event.requestContext?.http?.method || 'GET';
  const path = event.rawPath || '/';

  // Health check
  if (method === 'GET' && path === '/') {
    return { statusCode: 200, body: JSON.stringify({ status: 'ok', server: 'lambda-mcp-bedrock' }) };
  }

  // MCP endpoint
  if (method === 'POST') {
    const body = JSON.parse(event.body || '{}');
    const response = await handleMcpRequest(body);
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(response),
    };
  }

  return { statusCode: 405, body: 'Method not allowed' };
};

async function handleMcpRequest(request) {
  const { method, id, params } = request;

  if (method === 'initialize') {
    return {
      jsonrpc: '2.0', id,
      result: {
        protocolVersion: '2025-03-26',
        capabilities: { tools: { listChanged: false } },
        serverInfo: { name: 'lambda-bedrock-mcp', version: '1.0.0' },
      },
    };
  }

  if (method === 'tools/list') {
    return {
      jsonrpc: '2.0', id,
      result: {
        tools: [
          {
            name: 'ask_bedrock',
            description: 'Ask Amazon Bedrock (Claude) a question and get an AI-generated response',
            inputSchema: {
              type: 'object',
              properties: {
                prompt: { type: 'string', description: 'The question or prompt to send to Bedrock' },
                max_tokens: { type: 'number', description: 'Maximum tokens in response', default: 512 },
              },
              required: ['prompt'],
            },
          },
          {
            name: 'summarize',
            description: 'Summarize text using Amazon Bedrock (Claude)',
            inputSchema: {
              type: 'object',
              properties: {
                text: { type: 'string', description: 'The text to summarize' },
              },
              required: ['text'],
            },
          },
        ],
      },
    };
  }

  if (method === 'tools/call') {
    const toolName = params?.name;
    const args = params?.arguments || {};

    if (toolName === 'ask_bedrock') {
      const answer = await invokeBedrock(args.prompt, args.max_tokens || 512);
      return { jsonrpc: '2.0', id, result: { content: [{ type: 'text', text: answer }] } };
    }

    if (toolName === 'summarize') {
      const summary = await invokeBedrock(`Summarize the following text concisely:\n\n${args.text}`, 512);
      return { jsonrpc: '2.0', id, result: { content: [{ type: 'text', text: summary }] } };
    }

    return { jsonrpc: '2.0', id, error: { code: -32601, message: `Unknown tool: ${toolName}` } };
  }

  // notifications/initialized — acknowledge
  if (method === 'notifications/initialized') {
    return null;
  }

  return { jsonrpc: '2.0', id, error: { code: -32601, message: `Unknown method: ${method}` } };
}

async function invokeBedrock(prompt, maxTokens) {
  const response = await client.send(new InvokeModelCommand({
    modelId: process.env.MODEL_ID,
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify({
      anthropic_version: 'bedrock-2023-05-31',
      max_tokens: maxTokens,
      messages: [{ role: 'user', content: prompt }],
    }),
  }));
  const body = JSON.parse(new TextDecoder().decode(response.body));
  return body.content[0].text;
}
