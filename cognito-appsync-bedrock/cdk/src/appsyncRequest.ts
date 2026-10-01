import { SignatureV4 } from "@aws-sdk/signature-v4";
import { Sha256 } from "@aws-crypto/sha256-js";
import { defaultProvider } from "@aws-sdk/credential-provider-node";
import { HttpRequest } from "@aws-sdk/protocol-http";
import * as https from "https";

export interface Operation {
  query: string;
  operationName: string;
  variables: object;
}

export interface Config {
  url: string;
  key?: string;
  region: string;
}

export interface RequestParams {
  config: Config;
  operation: Operation;
}

export interface GraphQLResult<T = object> {
  data?: T;
  errors?: any[];
  extensions?: { [key: string]: any };
}

const executeAppSyncRequest = <T = object>(
  request: HttpRequest,
  endpoint: URL
) =>
  new Promise<GraphQLResult<T>>((resolve, reject) => {
    const httpRequest = https.request(
      { ...request, host: endpoint.hostname },
      (result) => {
        const responseChunks: Buffer[] = [];

        // AppSync responses can be streamed in multiple chunks, so wait until
        // the response has fully ended before attempting to parse the payload.
        result.on("data", (chunk) => {
          responseChunks.push(
            Buffer.isBuffer(chunk) ? chunk : Buffer.from(String(chunk))
          );
        });

        result.on("end", () => {
          const responseBody = Buffer.concat(responseChunks).toString("utf8");

          if (!responseBody) {
            resolve({});
            return;
          }

          try {
            resolve(JSON.parse(responseBody) as GraphQLResult<T>);
          } catch (error) {
            reject(
              new Error(
                `Failed to parse AppSync response as JSON: ${responseBody}`
              )
            );
          }
        });

        result.on("error", reject);
      }
    );

    httpRequest.on("error", reject);
    httpRequest.write(request.body);
    httpRequest.end();
  });

export const AppSyncRequestIAM = async <T = object>(params: RequestParams) => {
  const endpoint = new URL(params.config.url);
  const signer = new SignatureV4({
    credentials: defaultProvider(),
    region: params.config.region,
    service: "appsync",
    sha256: Sha256,
  });

  const requestToBeSigned = new HttpRequest({
    hostname: endpoint.host,
    port: 443,
    path: endpoint.pathname,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      host: endpoint.host,
    },
    body: JSON.stringify(params.operation),
  });

  const signedRequest = await signer.sign(requestToBeSigned);

  return executeAppSyncRequest<T>(signedRequest as HttpRequest, endpoint);
};

export const AppSyncRequestApiKey = async <T = object>(
  params: RequestParams
) => {
  const endpoint = new URL(params.config.url);

  const request = new HttpRequest({
    hostname: endpoint.host,
    port: 443,
    path: endpoint.pathname,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": params.config.key || "",
      host: endpoint.host,
    },
    body: JSON.stringify(params.operation),
  });

  return executeAppSyncRequest<T>(request, endpoint);
};

export const appSyncRequestCognito = async <T = object>(
  params: RequestParams,
  idToken: string
) => {
  const endpoint = new URL(params.config.url);

  const request = new HttpRequest({
    hostname: endpoint.host,
    port: 443,
    path: endpoint.pathname,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: idToken,
      host: endpoint.host,
    },
    body: JSON.stringify(params.operation),
  });

  return executeAppSyncRequest<T>(request, endpoint);
};
