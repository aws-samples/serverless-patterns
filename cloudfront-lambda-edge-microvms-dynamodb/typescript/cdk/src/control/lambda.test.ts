import { describe, it, expect, vi } from "vitest";
import { handle, type Controls } from "./lambda.js";

const controls = (over: Partial<Controls> = {}): Controls => ({
  ensure: vi.fn(async () => {}),
  terminate: vi.fn(async () => {}),
  ...over,
});

const get = (qs: string, c = controls()) => handle(c, { rawPath: "/_control", rawQueryString: qs, method: "GET" });
const ensure = (ret: string) => get(`session=alice&return=${encodeURIComponent(ret)}`);

describe("control ensure", () => {
  it("307s back to a relative return path with _attempt=1", async () => {
    const r: any = await ensure("/s/alice/x?foo=bar");
    expect(r.statusCode).toBe(307);
    expect(r.headers.location).toBe("/s/alice/x?foo=bar&_attempt=1");
  });

  it.each(["https://evil.com", "//evil.com", "/\\evil.com", "/\t/evil.com"])(
    "ignores an off-site return (%j) and answers 200 JSON",
    async (ret) => {
      const r: any = await ensure(ret);
      expect(r.statusCode).toBe(200);
      expect(r.headers.location).toBeUndefined();
      expect(JSON.parse(r.body)).toEqual({ sessionId: "alice", state: "RUNNING" });
    },
  );

});
