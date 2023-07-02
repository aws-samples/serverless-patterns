
import { DynamoDBStreamEvent, DynamoDBRecord } from "aws-lambda"
import { unmarshall } from "@aws-sdk/util-dynamodb"
import * as crypto from '@aws-crypto/sha256-js'
import { defaultProvider } from '@aws-sdk/credential-provider-node'
import { SignatureV4 } from '@aws-sdk/signature-v4'
import { HttpRequest } from '@aws-sdk/protocol-http'

interface Message {
  PK: string
  SK: string
  data: string
}

export const handler = async (event: DynamoDBStreamEvent): Promise<void> => {
  let messages = []
  await Promise.all(event.Records.map(async (record: DynamoDBRecord) => {
    let payload = unmarshall(record.dynamodb.NewImage)
    messages.push(payload)
  }))

  await Promise.all(messages.map(message => appsync(message)))
}

const { Sha256 } = crypto
const { APP_SYNC_API, AWS_REGION } = process.env

const query = /* GraphQL */ `
  mutation ON_CREATE_ITEM($PK: String!, $SK: String!, $data: String!) {
    onCreateItem(PK: $PK, SK: $SK, data: $data) {
      PK
      SK
      data
    }
  }
`
const appsync = async (variables: Message): Promise<void> => {
  const endpoint = new URL(APP_SYNC_API)

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