import {
  LambdaMicrovmsClient,
  RunMicrovmCommand,
  ListMicrovmsCommand,
  GetMicrovmCommand,
  CreateMicrovmAuthTokenCommand,
  type MicrovmState,
} from '@aws-sdk/client-lambda-microvms';
// The demo page is bundled into this function as a string via esbuild's text
// loader (configured on the NodejsFunction in the stack). We serve it from the
// same custom domain as the API so the page and its /api/provision call are
// same-origin — no CORS, no separate public endpoint.
// @ts-ignore -- resolved to a string at bundle time by the '.html' text loader.
import INDEX_HTML from '../frontend/index.html';

/**
 * Demo app + provisioning API for MicroVM custom domains, served from the ALB
 * as a Lambda target under the demo custom domain:
 *
 *   GET  /               -> the single-file demo page (HTML)
 *   POST /api/provision  -> reuse a RUNNING MicroVM from the configured image if
 *                           one exists (else RunMicrovm a fresh one), mint a
 *                           short-lived auth token, and return everything the
 *                           page needs to call the MicroVM through its custom
 *                           domain.
 *
 * This Lambda is a CONTROL-PLANE target only — it provisions and serves static
 * HTML. It is never in the request path to the MicroVM itself; the browser
 * calls the MicroVM's own custom domain directly afterwards.
 */

const IMAGE_ARN = requireEnv('MICROVM_IMAGE_ARN');
const CUSTOM_DOMAIN_BASE = requireEnv('CUSTOM_DOMAIN_BASE'); // e.g. microvms.example.com
const MICROVM_ENDPOINT_BASE = requireEnv('MICROVM_ENDPOINT_BASE'); // e.g. lambda-microvm.us-east-2.on.aws
const TOKEN_TTL_MINUTES = Number(process.env.TOKEN_TTL_MINUTES ?? '30');
const DEFAULT_PORT = Number(process.env.DEFAULT_PORT ?? '8080');

const client = new LambdaMicrovmsClient({});

// The page and the /api/provision call are same-origin (both under the demo
// custom domain), so no CORS is needed between them. We still send permissive
// CORS on the JSON response in case the page is opened from elsewhere. Tokens
// are short-lived and per-MicroVM.
const JSON_HEADERS: Record<string, string> = {
  'content-type': 'application/json',
  'access-control-allow-origin': '*',
  'access-control-allow-methods': 'GET,POST,OPTIONS',
  'access-control-allow-headers': 'content-type',
};

export async function handler(event: any): Promise<any> {
  // ALB target invocation shape: { httpMethod, path, ... }.
  const method =
    event?.httpMethod ?? event?.requestContext?.http?.method ?? 'GET';
  const rawPath =
    event?.path ?? event?.requestContext?.http?.path ?? '/';
  const routePath = rawPath.split('?')[0].replace(/\/+$/, '') || '/';

  if (method === 'OPTIONS') {
    return { statusCode: 204, headers: JSON_HEADERS, body: '' };
  }

  // Serve the demo page for the app root; anything that isn't the API path is
  // treated as the page too, so a stray refresh on a sub-path still works.
  if (routePath !== '/api/provision') {
    return {
      statusCode: 200,
      headers: { 'content-type': 'text/html; charset=utf-8' },
      body: INDEX_HTML,
    };
  }

  try {
    const microvm = await getOrRunMicrovm();
    const endpoint = await waitForEndpoint(microvm.microvmId!, microvm.endpoint);
    const port = DEFAULT_PORT;

    const tokenResp = await client.send(
      new CreateMicrovmAuthTokenCommand({
        microvmIdentifier: microvm.microvmId!,
        expirationInMinutes: TOKEN_TTL_MINUTES,
        allowedPorts: [{ port }],
      }),
    );
    const authToken = tokenResp.authToken?.['X-aws-proxy-auth'];
    if (!authToken) {
      throw new Error('CreateMicrovmAuthToken returned no X-aws-proxy-auth token');
    }

    // The service endpoint is "<uuid>.lambda-microvm.<region>.on.aws"; the
    // custom domain swaps the base for the wildcard base this stack owns.
    const uuid = endpoint.split('.')[0];
    const customDomain = `${uuid}.${CUSTOM_DOMAIN_BASE}`;

    return json(200, {
      microvmId: microvm.microvmId,
      state: microvm.state,
      reused: microvm.reused,
      serviceEndpoint: endpoint,
      customDomain,
      authToken,
      port,
      tokenTtlMinutes: TOKEN_TTL_MINUTES,
      defaultPath: '/ping',
    });
  } catch (err: any) {
    console.error('provision failed', err);
    return json(500, { error: err?.name ?? 'Error', message: String(err?.message ?? err) });
  }
}

/** Reuse the first RUNNING MicroVM from our image, else launch a new one. */
async function getOrRunMicrovm(): Promise<{
  microvmId?: string;
  state?: MicrovmState;
  endpoint?: string;
  reused: boolean;
}> {
  // ListMicrovms summaries don't include the endpoint, so we filter by state
  // here and resolve the endpoint via GetMicrovm / RunMicrovm below.
  let nextToken: string | undefined;
  do {
    const page = await client.send(
      new ListMicrovmsCommand(nextToken ? { nextToken } : {}),
    );
    const running = (page.microvms ?? []).find(
      (m) => m.state === 'RUNNING' && m.imageArn === IMAGE_ARN,
    );
    if (running?.microvmId) {
      return { microvmId: running.microvmId, state: running.state, reused: true };
    }
    nextToken = page.nextToken;
  } while (nextToken);

  const run = await client.send(
    new RunMicrovmCommand({
      imageIdentifier: IMAGE_ARN,
      idlePolicy: {
        autoResumeEnabled: true,
        maxIdleDurationSeconds: 900,
        suspendedDurationSeconds: 1800,
      },
    }),
  );
  return {
    microvmId: run.microvmId,
    state: run.state,
    endpoint: run.endpoint,
    reused: false,
  };
}

/**
 * Resolve the MicroVM endpoint, polling GetMicrovm until it appears. RunMicrovm
 * returns the endpoint directly; a reused MicroVM needs one GetMicrovm call.
 */
async function waitForEndpoint(microvmId: string, known?: string): Promise<string> {
  if (known) return known;
  for (let attempt = 0; attempt < 10; attempt++) {
    const got = await client.send(
      new GetMicrovmCommand({ microvmIdentifier: microvmId }),
    );
    if (got.endpoint) return got.endpoint;
    await sleep(1000);
  }
  throw new Error(`MicroVM ${microvmId} has no endpoint yet`);
}

function json(statusCode: number, body: unknown) {
  return { statusCode, headers: JSON_HEADERS, body: JSON.stringify(body) };
}

function requireEnv(name: string): string {
  const v = process.env[name];
  if (!v) throw new Error(`Missing required environment variable ${name}`);
  return v;
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
