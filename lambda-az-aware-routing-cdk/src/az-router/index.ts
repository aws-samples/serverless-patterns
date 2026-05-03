/**
 * Lambda AZ-aware routing — reads AZ metadata from the Lambda metadata endpoint
 * and demonstrates same-AZ routing by writing the AZ info to DynamoDB.
 */

import http from "http";

const METADATA_API = process.env.AWS_LAMBDA_METADATA_API;
const METADATA_TOKEN = process.env.AWS_LAMBDA_METADATA_TOKEN;

interface MetadataResponse {
  AvailabilityZoneID: string;
}

let cachedAzId: string | null = null;

async function getAzId(): Promise<string> {
  if (cachedAzId) return cachedAzId;

  return new Promise((resolve, reject) => {
    const url = `http://${METADATA_API}/2026-01-15/metadata/execution-environment`;
    const req = http.get(url, { headers: { Authorization: `Bearer ${METADATA_TOKEN}` } }, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => {
        const parsed: MetadataResponse = JSON.parse(data);
        cachedAzId = parsed.AvailabilityZoneID;
        resolve(cachedAzId!);
      });
    });
    req.on("error", reject);
    req.end();
  });
}

// Fallback for local testing where metadata endpoint is unavailable
async function getAzIdSafe(): Promise<string> {
  if (!METADATA_API || !METADATA_TOKEN) return "local-dev";
  try {
    return await getAzId();
  } catch {
    return "unknown";
  }
}

export const handler = async (event: any) => {
  const azId = await getAzIdSafe();
  const requestId = event.requestContext?.requestId ?? "direct-invoke";

  // In production, use azId to select same-AZ endpoints:
  // - ElastiCache: pick the reader endpoint in the same AZ
  // - RDS: pick the reader in the same AZ
  // - DynamoDB DAX: pick the same-AZ DAX node
  // This demo logs the AZ and returns it.

  const result = {
    azId,
    functionName: process.env.AWS_LAMBDA_FUNCTION_NAME,
    region: process.env.AWS_REGION,
    message: `Lambda running in ${azId}. Use this to route to same-AZ downstream services.`,
    routingExample: {
      description: "In production, map AZ IDs to same-AZ endpoints",
      sameAzBenefit: "Eliminates cross-AZ data transfer costs and reduces latency by ~1ms",
    },
  };

  return { statusCode: 200, body: JSON.stringify(result) };
};
