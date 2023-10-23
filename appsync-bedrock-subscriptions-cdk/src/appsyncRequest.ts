import { SignatureV4 } from '@aws-sdk/signature-v4'
import { Sha256 } from '@aws-crypto/sha256-js';
import { defaultProvider } from '@aws-sdk/credential-provider-node'
import { HttpRequest } from '@aws-sdk/protocol-http'
import * as https from 'https'


export interface Operation {
  query: string,
  operationName: string,
  variables: object
}

export interface Config {
  url: string,
  key?: string,
  region: string,
}

export interface RequestParams {
  config: Config,
  operation: Operation
}

export interface GraphQLResult<T = object> {
  data?: T
  errors?: any[]
  extensions?: { [key: string]: any }
}


export const AppSyncRequestIAM = async (params: RequestParams) => {
  const endpoint = new URL(params.config.url)
  const signer = new SignatureV4({
    credentials: defaultProvider(),
    region: params.config.region,
    service: 'appsync',
    sha256: Sha256,
  })

  const requestToBeSigned = new HttpRequest({
    hostname: endpoint.host,
    port: 443,
    path: endpoint.pathname,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      host: endpoint.host,
    },
    body: JSON.stringify(params.operation),
  })

  const signedRequest = await signer.sign(requestToBeSigned)

  return new Promise((resolve, reject) => {
    const httpRequest = https.request({ ...signedRequest, host: endpoint.hostname }, (result) => {
      result.on('data', (data) => {
        resolve(JSON.parse(data.toString()))
      })
    })
    httpRequest.write(signedRequest.body)
    httpRequest.end()
  })
}

export const AppSyncRequestApiKey = async <T = object>(params: RequestParams) => {
  const endpoint = new URL(params.config.url)

  const request = new HttpRequest({
    hostname: endpoint.host,
    port: 443,
    path: endpoint.pathname,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': params.config.key || "",
      host: endpoint.host,
    },
    body: JSON.stringify(params.operation),
  })

  return new Promise<GraphQLResult<T>>((resolve, reject) => {
    const httpRequest = https.request({ ...request, host: endpoint.hostname }, (result) => {
      result.on('data', (data) => {
        resolve(JSON.parse(data.toString()))
      })
    })
    httpRequest.write(request.body)
    httpRequest.end()
  })
}