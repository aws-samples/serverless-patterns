import { Handler } from "aws-lambda"
import { BedrockRuntimeClient, InvokeModelWithResponseStreamCommand } from "@aws-sdk/client-bedrock-runtime"
import { randomUUID } from 'crypto'
import { appsyncRequest } from "./appsyncRequest"

const client = new BedrockRuntimeClient()

export const handler: Handler<object, object> = async (event: { chatId: string, prompt: string}) => {
  const commandInput = {
    contentType: "application/json",
    modelId: "anthropic.claude-3-haiku-20240307-v1:0",
    body: JSON.stringify({
      anthropic_version: "bedrock-2023-05-31",
      max_tokens: 1000,
      messages: [{ role: "user", content: [{ type: "text", text: event.prompt }] }]
    })
  }
  const command = new InvokeModelWithResponseStreamCommand(commandInput)
  const response = await client.send(command)

  let fullText = ""
  const messageId = randomUUID()
  for await (const item of response.body) {
    const chunk = JSON.parse(new TextDecoder().decode(item.chunk.bytes))
    const chunk_type = chunk.type

    const text = chunk.delta?.text || ''
    fullText = fullText + text

    const emitChunk = {
      chatId: event.chatId,
      messageId,
      type: chunk_type,
      text,
      fullText
    }
    
    await appsyncRequest(emitChunk)
  }

  return {}
}