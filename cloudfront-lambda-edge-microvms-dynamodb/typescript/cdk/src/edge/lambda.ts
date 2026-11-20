// Lambda@Edge origin-request handler. Lambda@Edge forbids environment variables, so the
// stack passes the table name and Region as custom headers on the (placeholder) origin;
// CloudFront hands them to this function in the event. The router strips them before
// the request is forwarded to a MicroVM.
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";
import type { CloudFrontRequestEvent } from "aws-lambda";
import { handleRequest, reply, type Session } from "./router.js";

let ddb: DynamoDBDocumentClient | undefined; // created once per container, on first use

export const handler = async (event: CloudFrontRequestEvent) => {
  const request = event.Records[0].cf.request;
  const config = request.origin?.custom?.customHeaders ?? {};
  const table = config["x-sessions-table"]?.[0]?.value;
  const region = config["x-sessions-region"]?.[0]?.value;
  if (!table || !region) {
    console.error("missing x-sessions-table / x-sessions-region origin custom headers");
    return reply("500", "Internal Server Error", "edge router is not configured");
  }
  ddb ??= DynamoDBDocumentClient.from(new DynamoDBClient({ region }));

  return handleRequest(request, async (sessionId) => {
    const got = await ddb!.send(new GetCommand({ TableName: table, Key: { sessionId }, ConsistentRead: true }));
    return got.Item as Session | undefined;
  });
};
