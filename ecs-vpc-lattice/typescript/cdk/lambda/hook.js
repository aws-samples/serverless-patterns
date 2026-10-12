// Amazon ECS lifecycle hook (POST_TEST_TRAFFIC_SHIFT): call the green revision through the
// Amazon VPC Lattice TEST listener rule and compare the version it reports with the expected one.
// ECS passes hookDetails ({ url, expectedVersion }) from the service configuration in the event.
// The function must return { hookStatus: 'SUCCEEDED' | 'FAILED' | 'IN_PROGRESS' }; FAILED rolls back.

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// One GET; returns { status, version }. Headers select the Lattice listener rule.
async function get(doFetch, url, headers) {
  const res = await doFetch(url, { headers, signal: AbortSignal.timeout(5000) });
  let version = null;
  try { version = JSON.parse(await res.text()).version ?? null; } catch (e) { /* not JSON */ }
  return { status: res.status, version };
}

async function probe({ url, expectedVersion, doFetch = fetch, attempts = 5, delayMs = 5000 }) {
  let last = {};
  for (let i = 1; i <= attempts; i++) {
    try {
      last = await get(doFetch, url, { 'x-environment': 'test' });
      console.log(JSON.stringify({ msg: 'test-listener-probe', attempt: i, expectedVersion, observedVersion: last.version, status: last.status }));
      if (last.status === 200 && last.version === expectedVersion) return { ok: true, last };
    } catch (e) {
      last = { error: String(e.message || e) };
      console.log(JSON.stringify({ msg: 'test-listener-probe-error', attempt: i, error: last.error }));
    }
    if (i < attempts) await sleep(delayMs);
  }
  return { ok: false, last };
}

// hookDetails is configured as a JSON string in the service; accept an already parsed object as well.
function parseHookDetails(hookDetails) {
  if (typeof hookDetails === 'string') {
    try { return JSON.parse(hookDetails) || {}; } catch (e) { return {}; }
  }
  return hookDetails || {};
}

exports.handler = async (event) => {
  const { url, expectedVersion } = parseHookDetails(event.hookDetails);
  console.log(JSON.stringify({ msg: 'hook-invoked', stage: event.lifecycleStage, url, expectedVersion, eventKeys: Object.keys(event), hookDetailsType: typeof event.hookDetails }));
  if (!url || !expectedVersion) return { hookStatus: 'FAILED', reason: 'hookDetails.url and hookDetails.expectedVersion are required' };

  const result = await probe({ url, expectedVersion });
  // Manual invocations (see the README) also read the production listener to show which version production serves.
  // The invocation by ECS never does: a 5xx from production during a deployment would trip the rollback alarms.
  if (String(event.lifecycleStage || '').startsWith('MANUAL')) {
    try {
      const prod = await get(fetch, url, {});
      console.log(JSON.stringify({ msg: 'production-listener-observation', observedVersion: prod.version, status: prod.status }));
    } catch (e) { /* ignore */ }
  }

  if (result.ok) {
    console.log(JSON.stringify({ msg: 'hook-result', hookStatus: 'SUCCEEDED', observedVersion: result.last.version }));
    return { hookStatus: 'SUCCEEDED' };
  }
  const reason = `test listener returned ${JSON.stringify(result.last)}, expected version ${expectedVersion}`;
  console.log(JSON.stringify({ msg: 'hook-result', hookStatus: 'FAILED', reason }));
  return { hookStatus: 'FAILED', reason };
};

exports.probe = probe;
exports.parseHookDetails = parseHookDetails;
