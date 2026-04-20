import { defaultProvider } from '@aws-sdk/credential-provider-node';
import { SignatureV4 } from '@smithy/signature-v4';
import { Sha256 } from '@aws-crypto/sha256-js';
import { HttpRequest } from '@smithy/protocol-http';
import https from 'https';

const region = process.env.AWS_REGION || 'us-east-1';

async function makeSignedRequest(method, path, body) {
  const credentials = await defaultProvider()();
  const signer = new SignatureV4({
    service: 'bedrock',
    region,
    credentials,
    sha256: Sha256,
  });

  const request = new HttpRequest({
    method,
    protocol: 'https:',
    hostname: `bedrock.${region}.amazonaws.com`,
    path,
    headers: {
      'Content-Type': 'application/json',
      host: `bedrock.${region}.amazonaws.com`,
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  const signed = await signer.sign(request);

  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: signed.hostname,
      path: signed.path,
      method: signed.method,
      headers: signed.headers,
    }, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          resolve(data ? JSON.parse(data) : {});
        } else {
          reject(new Error(`HTTP ${res.statusCode}: ${data}`));
        }
      });
    });
    req.on('error', reject);
    if (signed.body) req.write(signed.body);
    req.end();
  });
}

export async function onEvent(event) {
  const { GuardrailIdentifier, GuardrailVersion } = event.ResourceProperties;

  if (event.RequestType === 'Create' || event.RequestType === 'Update') {
    await makeSignedRequest('PUT', '/enforced-guardrail-configuration', {
      guardrailIdentifier: GuardrailIdentifier,
      guardrailVersion: GuardrailVersion,
    });

    return {
      PhysicalResourceId: `${GuardrailIdentifier}-enforced`,
      Data: { GuardrailIdentifier, GuardrailVersion },
    };
  }

  if (event.RequestType === 'Delete') {
    try {
      await makeSignedRequest('DELETE', '/enforced-guardrail-configuration', {});
    } catch (e) {
      // Ignore if already deleted
    }
  }

  return { PhysicalResourceId: event.PhysicalResourceId };
}
