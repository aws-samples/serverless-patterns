import { describe, it, expect, vi } from "vitest";
import { ensureSession, LaunchInProgress, type EnsureDeps, type SessionRecord } from "./microvm.js";

const NOW = 1_000_000;

// In-memory table with the same claim semantics as the real conditional put.
function makeDeps(seed?: SessionRecord, mvm: Partial<EnsureDeps["mvm"]> = {}) {
  const store = new Map<string, SessionRecord>();
  if (seed) store.set(seed.sessionId, seed);
  let clock = NOW; // advances only when the code sleeps
  const d = {
    imageArn: "arn:image",
    now: () => clock,
    sleep: async (ms: number) => void (clock += ms),
    ddb: {
      get: vi.fn(async (id: string) => store.get(id)),
      put: vi.fn(async (rec: SessionRecord) => void store.set(rec.sessionId, rec)),
      claim: vi.fn(async (rec: SessionRecord, staleBefore: number, deadMicrovmId?: string) => {
        const cur = store.get(rec.sessionId);
        if (cur && cur.launchedAt >= staleBefore && !(deadMicrovmId && cur.microvmId === deadMicrovmId)) return false;
        store.set(rec.sessionId, rec);
        return true;
      }),
    },
    mvm: {
      runMicrovm: vi.fn(async () => ({ microvmId: "m-new" })),
      getMicrovm: vi.fn(async (): Promise<{ state: string; endpoint: string } | undefined> => ({ state: "RUNNING", endpoint: "ep" })),
      createAuthToken: vi.fn(async () => "tok"),
      ...mvm,
    },
  } satisfies EnsureDeps;
  return { d, store };
}

describe("ensureSession", () => {
  it("launches a new VM, passes the session id to /run, and stores a usable record", async () => {
    const { d, store } = makeDeps();
    await ensureSession(d, "s");
    expect(d.mvm.runMicrovm).toHaveBeenCalledTimes(1);
    expect(JSON.parse(vi.mocked(d.mvm.runMicrovm).mock.calls[0][0].runHookPayload)).toEqual({ sessionId: "s" });
    expect(store.get("s")).toMatchObject({ state: "RUNNING", microvmId: "m-new", endpoint: "ep", token: "tok" });
  });

  it("attaches to a live VM and re-mints a token without relaunching", async () => {
    const { d, store } = makeDeps({ sessionId: "s", state: "RUNNING", launchedAt: 1, microvmId: "m1", endpoint: "ep" });
    await ensureSession(d, "s");
    expect(d.mvm.runMicrovm).not.toHaveBeenCalled();
    expect(store.get("s")).toMatchObject({ microvmId: "m1", token: "tok" });
  });

  it("re-mints for a SUSPENDED VM without waiting or relaunching (auto-resume on next request)", async () => {
    const getMicrovm = vi.fn(async () => ({ state: "SUSPENDED", endpoint: "ep" }));
    const { d, store } = makeDeps({ sessionId: "s", state: "RUNNING", launchedAt: 1, microvmId: "m1", endpoint: "ep" }, { getMicrovm });
    await ensureSession(d, "s");
    expect(getMicrovm).toHaveBeenCalledTimes(1);
    expect(d.mvm.runMicrovm).not.toHaveBeenCalled();
    expect(store.get("s")).toMatchObject({ microvmId: "m1", token: "tok" });
  });

  it("relaunches when the recorded VM is gone", async () => {
    const getMicrovm = vi.fn().mockResolvedValueOnce(undefined).mockResolvedValue({ state: "RUNNING", endpoint: "ep" });
    const { d, store } = makeDeps({ sessionId: "s", state: "RUNNING", launchedAt: 1, microvmId: "m-dead" }, { getMicrovm });
    await ensureSession(d, "s");
    expect(d.mvm.runMicrovm).toHaveBeenCalledTimes(1);
    expect(store.get("s")?.microvmId).toBe("m-new");
  });

  it("throws LaunchInProgress, without launching, while another caller holds a fresh claim", async () => {
    const { d } = makeDeps({ sessionId: "s", state: "PENDING", launchedAt: NOW - 1000 });
    await expect(ensureSession(d, "s")).rejects.toBeInstanceOf(LaunchInProgress);
    expect(d.mvm.runMicrovm).not.toHaveBeenCalled();
  });

  it("releases the claim and rethrows when RunMicrovm fails", async () => {
    const { d, store } = makeDeps(undefined, { runMicrovm: vi.fn().mockRejectedValue(new Error("boom")) });
    await expect(ensureSession(d, "s")).rejects.toThrow("boom");
    expect(store.get("s")?.launchedAt).toBe(0);
  });
});
