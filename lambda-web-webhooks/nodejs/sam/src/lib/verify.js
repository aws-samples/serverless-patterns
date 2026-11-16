import crypto from 'crypto';

/**
 * Verify Stripe webhook signature.
 * Stripe uses HMAC-SHA256 with a timestamp prefix.
 * Header format: t=<timestamp>,v1=<signature>
 */
function verifyStripe(payload, headers, secret) {
  const sigHeader = headers['stripe-signature'];
  if (!sigHeader) return { valid: false, error: 'Missing stripe-signature header' };

  const parts = {};
  for (const item of sigHeader.split(',')) {
    const [key, ...rest] = item.split('=');
    parts[key] = rest.join('=');
  }

  if (!parts.t || !parts.v1) {
    return { valid: false, error: 'Malformed stripe-signature header' };
  }

  const signedPayload = `${parts.t}.${payload}`;
  const expectedSig = crypto
    .createHmac('sha256', secret)
    .update(signedPayload)
    .digest('hex');

  try {
    const valid = crypto.timingSafeEqual(
      Buffer.from(parts.v1, 'hex'),
      Buffer.from(expectedSig, 'hex')
    );
    return { valid, timestamp: parts.t };
  } catch {
    return { valid: false, error: 'Signature length mismatch' };
  }
}

/**
 * Verify GitHub webhook signature.
 * GitHub uses HMAC-SHA256.
 * Header: x-hub-signature-256 = sha256=<hex>
 */
function verifyGitHub(payload, headers, secret) {
  const sigHeader = headers['x-hub-signature-256'];
  if (!sigHeader) return { valid: false, error: 'Missing x-hub-signature-256 header' };

  const expectedSig = 'sha256=' + crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  try {
    const valid = crypto.timingSafeEqual(
      Buffer.from(sigHeader),
      Buffer.from(expectedSig)
    );
    return { valid };
  } catch {
    return { valid: false, error: 'Signature length mismatch' };
  }
}

/**
 * Verify generic webhook with configurable HMAC header.
 * Header: x-webhook-signature = <hex>
 */
function verifyGeneric(payload, headers, secret) {
  const sigHeader = headers['x-webhook-signature'];
  if (!sigHeader) return { valid: false, error: 'Missing x-webhook-signature header' };

  const expectedSig = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  try {
    const valid = crypto.timingSafeEqual(
      Buffer.from(sigHeader, 'hex'),
      Buffer.from(expectedSig, 'hex')
    );
    return { valid };
  } catch {
    return { valid: false, error: 'Signature length mismatch' };
  }
}

/**
 * Generate a valid signature for testing.
 */
function generateSignature(provider, payload, secret) {
  if (provider === 'stripe') {
    const timestamp = Math.floor(Date.now() / 1000);
    const signedPayload = `${timestamp}.${payload}`;
    const sig = crypto.createHmac('sha256', secret).update(signedPayload).digest('hex');
    return { header: 'stripe-signature', value: `t=${timestamp},v1=${sig}` };
  }
  if (provider === 'github') {
    const sig = crypto.createHmac('sha256', secret).update(payload).digest('hex');
    return { header: 'x-hub-signature-256', value: `sha256=${sig}` };
  }
  // generic
  const sig = crypto.createHmac('sha256', secret).update(payload).digest('hex');
  return { header: 'x-webhook-signature', value: sig };
}

const verifiers = { stripe: verifyStripe, github: verifyGitHub, generic: verifyGeneric };

export { verifiers, generateSignature };
