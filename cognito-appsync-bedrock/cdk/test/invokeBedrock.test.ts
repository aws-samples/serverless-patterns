import { resolveBedrockRegion } from "../src/lambda/invokeBedrock/index";

describe("resolveBedrockRegion", () => {
  const originalEnv = process.env;

  beforeEach(() => {
    process.env = { ...originalEnv };
    delete process.env.BEDROCK_REGION;
    delete process.env.AWS_REGION;
    delete process.env.AWS_DEFAULT_REGION;
  });

  afterAll(() => {
    process.env = originalEnv;
  });

  test("prefers BEDROCK_REGION when provided", () => {
    process.env.BEDROCK_REGION = "eu-west-1";
    process.env.AWS_REGION = "us-west-2";

    expect(resolveBedrockRegion()).toBe("eu-west-1");
  });

  test("falls back to AWS_REGION and AWS_DEFAULT_REGION", () => {
    process.env.AWS_REGION = "ap-southeast-2";
    expect(resolveBedrockRegion()).toBe("ap-southeast-2");

    delete process.env.AWS_REGION;
    process.env.AWS_DEFAULT_REGION = "ca-central-1";
    expect(resolveBedrockRegion()).toBe("ca-central-1");
  });

  test("throws when no region environment variable is set", () => {
    expect(() => resolveBedrockRegion()).toThrow(
      "AWS region is not configured."
    );
  });
});
