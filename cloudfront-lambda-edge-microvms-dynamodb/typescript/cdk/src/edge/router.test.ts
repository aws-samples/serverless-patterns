import { describe, it, expect, vi } from "vitest";
import type { CloudFrontRequest } from "aws-lambda";
import { handleRequest, type Session } from "./router.js";

// A minimal CloudFront origin-request event `request`.
const req = (uri = "/s/alice/", querystring = ""): CloudFrontRequest => ({
  clientIp: "203.0.113.1",
  method: "GET",
  uri,
  querystring,
  headers: {},
  origin: {
    custom: {
      domainName: "example.com",
      customHeaders: { "x-sessions-table": [{ key: "x-sessions-table", value: "t" }] },
      keepaliveTimeout: 5,
      path: "",
      port: 443,
      protocol: "https",
      readTimeout: 30,
      sslProtocols: ["TLSv1.2"],
    },
  },
});

const NOW = 1000;
const SESSION: Session = { endpoint: "ep.aws", token: "JWE", tokenExpiresAt: NOW + 20 * 60_000 };
const route = (session: Session | undefined, r = req()) => handleRequest(r, async () => session, NOW) as Promise<any>;

describe("usable session -> proxy to the MicroVM", () => {
  it("rewrites origin + Host, adds the token and port, strips config headers", async () => {
    const r = await route(SESSION);
    expect(r.origin.custom.domainName).toBe("ep.aws");
    expect(r.origin.custom.customHeaders).toEqual({});
    expect(r.headers["host"][0].value).toBe("ep.aws");
    expect(r.headers["x-aws-proxy-auth"][0].value).toBe("JWE");
    expect(r.headers["x-aws-proxy-port"][0].value).toBe("8080");
  });

});

describe("validation and lookup", () => {
  it.each([`session=${"a".repeat(65)}`, ""])("400s %j without a lookup", async (qs) => {
    const lookup = vi.fn();
    const r: any = await handleRequest(req("/", qs), lookup, NOW);
    expect(lookup).not.toHaveBeenCalled();
    expect(r.status).toBe("400");
  });

});

describe("miss -> control plane", () => {
  it("307s to /_control with the session and the encoded original url", async () => {
    const r = await route(undefined, req("/s/alice/x", "foo=bar"));
    expect(r.status).toBe("307");
    expect(r.headers.location[0].value).toBe("/_control?session=alice&return=" + encodeURIComponent("/s/alice/x?foo=bar"));
    expect(r.headers["cache-control"][0].value).toBe("no-store");
  });

  it.each([
    ["no token", { endpoint: "ep" }],
    ["token within the 60s margin", { ...SESSION, tokenExpiresAt: NOW + 60_000 }],
  ])("treats %s as a miss", async (_, s) => {
    expect((await route(s as Session)).status).toBe("307");
  });

  it.each(["_attempt=1", "_attempt=0"])(
    "503s instead of redirecting again when %j is present (loop guard)",
    async (qs) => {
      expect((await route(undefined, req("/s/alice/", qs))).status).toBe("503");
    },
  );
});
