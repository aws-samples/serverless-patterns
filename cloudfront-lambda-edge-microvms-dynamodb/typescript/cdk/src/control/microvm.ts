// Launch-or-attach a session's MicroVM. Pure over its injected deps so it unit-tests
// without AWS:
//
//   1. The record names a live VM -> mint a fresh token (waiting first if it's still booting).
//   2. Otherwise claim the launch with a conditional put (the launch mutex), so two
//      concurrent first requests can't start two VMs. The loser gets LaunchInProgress.
//   3. The winner records the microvmId right after RunMicrovm, so a retry that lands
//      while the VM is still booting attaches to it (step 1) instead of relaunching.
import type { IdlePolicy } from "@aws-sdk/client-lambda-microvms";

export interface SessionRecord {
  sessionId: string;
  state: "PENDING" | "RUNNING";
  launchedAt: number;
  microvmId?: string;
  endpoint?: string;
  token?: string;
  tokenExpiresAt?: number;
}

export interface EnsureDeps {
  imageArn: string;
  now: () => number;
  sleep: (ms: number) => Promise<void>;
  ddb: {
    get: (sessionId: string) => Promise<SessionRecord | undefined>;
    put: (rec: SessionRecord) => Promise<void>;
    // Writes `rec` only if no launch was claimed after `staleBefore`, or the record still
    // names `deadMicrovmId` (a VM we just found gone); false if another launch holds it.
    claim: (rec: SessionRecord, staleBefore: number, deadMicrovmId?: string) => Promise<boolean>;
  };
  mvm: {
    runMicrovm: (args: { imageIdentifier: string; idlePolicy: IdlePolicy; runHookPayload: string }) => Promise<{ microvmId: string }>;
    getMicrovm: (id: string) => Promise<{ state: string; endpoint: string } | undefined>; // undefined = not found
    createAuthToken: (id: string) => Promise<string>;
  };
}

export class LaunchInProgress extends Error {
  constructor() {
    super("launch in progress");
  }
}

const IDLE: IdlePolicy = { autoResumeEnabled: true, maxIdleDurationSeconds: 900, suspendedDurationSeconds: 1800 };

const TOKEN_TTL_MS = 30 * 60_000; // matches CreateMicrovmAuthToken expirationInMinutes: 30
// A claim older than this is treated as abandoned (e.g. the winner crashed) and can be
// re-claimed. Kept above the control Lambda's 60s timeout.
const CLAIM_TTL_MS = 90_000;
// Boot-wait budget. With RunMicrovm and the DynamoDB calls around it, the control plane
// answers within CloudFront's 30s origin timeout, so a slow boot surfaces as its own
// 500 rather than an opaque CloudFront 504.
const BOOT_WAIT_MS = 20_000;
const POLL_MS = 500;

const isGone = (state: string) => state === "TERMINATING" || state === "TERMINATED";

async function waitRunning(d: EnsureDeps, microvmId: string): Promise<string> {
  const deadline = d.now() + BOOT_WAIT_MS;
  while (d.now() < deadline) {
    const vm = await d.mvm.getMicrovm(microvmId);
    if (vm?.state === "RUNNING") return vm.endpoint;
    if (!vm || isGone(vm.state)) throw new Error(`microvm ${microvmId} terminated during boot`);
    await d.sleep(POLL_MS);
  }
  throw new Error(`microvm ${microvmId} did not reach RUNNING`);
}

// Mint a token and store the now-usable record the edge reads. Only a booting (PENDING)
// VM is waited on: a SUSPENDED one auto-resumes when the edge proxies the next request.
async function attach(d: EnsureDeps, rec: SessionRecord & { microvmId: string }, vm?: { state: string; endpoint: string }) {
  const endpoint = vm && vm.state !== "PENDING" ? vm.endpoint : await waitRunning(d, rec.microvmId);
  const token = await d.mvm.createAuthToken(rec.microvmId);
  await d.ddb.put({ ...rec, state: "RUNNING", endpoint, token, tokenExpiresAt: d.now() + TOKEN_TTL_MS });
}

export async function ensureSession(d: EnsureDeps, sessionId: string): Promise<void> {
  const rec = await d.ddb.get(sessionId);
  if (rec?.microvmId) {
    // Not found -> relaunch. Other errors (e.g. throttling) propagate, so a hiccup never
    // starts a second VM.
    const vm = await d.mvm.getMicrovm(rec.microvmId);
    if (vm && !isGone(vm.state)) return attach(d, { ...rec, microvmId: rec.microvmId }, vm);
  }

  // Claim the launch. A VM we just found gone doesn't block the claim, even if it was
  // launched less than CLAIM_TTL_MS ago.
  const claim: SessionRecord = { sessionId, state: "PENDING", launchedAt: d.now() };
  if (!(await d.ddb.claim(claim, d.now() - CLAIM_TTL_MS, rec?.microvmId))) throw new LaunchInProgress();

  let microvmId: string;
  try {
    ({ microvmId } = await d.mvm.runMicrovm({
      imageIdentifier: d.imageArn,
      idlePolicy: IDLE,
      runHookPayload: JSON.stringify({ sessionId }), // the in-VM /run hook reads this
    }));
  } catch (err) {
    // Release the claim so the next attempt retries (and surfaces the real error)
    // instead of waiting out CLAIM_TTL_MS behind LaunchInProgress.
    await d.ddb.put({ ...claim, launchedAt: 0 }).catch(() => {});
    throw err;
  }
  const launched = { ...claim, microvmId };
  await d.ddb.put(launched);
  return attach(d, launched); // just launched: wait for it to boot
}
