import { HttpRequest } from '@aws-sdk/protocol-http'
import * as https from 'https'

export interface RequestParamsEvent {
  config: Config
  channelName: String
  events: Array<Record<string, any>>
}

export interface Config {
  url: string,
  key?: string,
  region: string,
}

export const AppSyncEventsRequestApiKey = async (params: RequestParamsEvent) => {
  let endpoint: URL

  const regex = new RegExp(/^http:\/\/|https:\/\//)
  if (!regex.test(params.config.url)) {
    endpoint = new URL(`http://${params.config.url}`)
  } else {
    endpoint = new URL(params.config.url)
  }

  const request = new HttpRequest({
    hostname: endpoint.host,
    port: 443,
    path: "/event",
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': params.config.key || "",
    },
    body: JSON.stringify({
      "channel": params.channelName,
      "events": params.events.map(e => JSON.stringify(e))
    })
  })

  return new Promise<any>((resolve, reject) => {
    const httpRequest = https.request({ ...request, host: endpoint.hostname }, (result) => {
      let responseBody = '';
      result.on('data', (chunk) => {
        responseBody += chunk;
      });
      result.on('end', () => {
        if (result.statusCode && result.statusCode >= 200 && result.statusCode < 300) {
          resolve(JSON.parse(responseBody));
        } else {
          reject(new Error(`HTTP Error: ${result.statusCode} - ${responseBody}`));
        }
      });
    });
    httpRequest.on('error', (error) => {
      console.log(error)
      reject(error);
    });
    httpRequest.write(request.body)
    httpRequest.end()
  })

}