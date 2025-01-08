import * as crypto from '@aws-crypto/sha256-js'
import { defaultProvider } from '@aws-sdk/credential-provider-node'
import { SignatureV4 } from '@aws-sdk/signature-v4'
import { HttpRequest } from '@aws-sdk/protocol-http'

interface Chunk {
  chatId: string
  messageId: string
  type: string
  text: string
  fullText: string
}

const { Sha256 } = crypto
const { APP_SYNC_API, AWS_REGION } = process.env
const endpoint = new URL(APP_SYNC_API)
const query = /* GraphQL */ `
  mutation onMessage($chatId: String!, $messageId: String!, $type: String!, $text: String!, $fullText: String!) {
    onMessage(chatId: $chatId, messageId: $messageId, type: $type, text: $text, fullText: $fullText) {
      chatId
      messageId
      type
      text
      fullText
    }
  }
`

export const appsyncRequest = async (variables: Chunk) => {
  const signer = new SignatureV4({
    credentials: defaultProvider(),
    region: AWS_REGION,
    service: 'appsync',
    sha256: Sha256
  })

  const requestToBeSigned = new HttpRequest({
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      host: endpoint.host
    },
    hostname: endpoint.host,
    body: JSON.stringify({ query, variables }),
    path: endpoint.pathname
  })

  const signed = await signer.sign(requestToBeSigned)
  const request = new Request(APP_SYNC_API, signed)

  await fetch(request)
}