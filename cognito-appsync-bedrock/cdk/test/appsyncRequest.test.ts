import * as https from "https";
import { EventEmitter } from "events";
import {
  AppSyncRequestApiKey,
  appSyncRequestCognito,
} from "../src/appsyncRequest";

jest.mock("https", () => ({
  request: jest.fn(),
}));

const mockedRequest = jest.mocked(https.request);

class MockClientRequest extends EventEmitter {
  public body = "";

  write(chunk: string) {
    this.body += chunk;
  }

  end() {
    this.emit("finish");
  }
}

class MockIncomingMessage extends EventEmitter {
  constructor(private readonly responseChunks: string[]) {
    super();
  }

  flush() {
    for (const chunk of this.responseChunks) {
      this.emit("data", chunk);
    }
    this.emit("end");
  }
}

describe("appsyncRequest transport helpers", () => {
  beforeEach(() => {
    mockedRequest.mockReset();
  });

  test("appSyncRequestCognito waits for the full response body before parsing JSON", async () => {
    let capturedOptions: unknown;

    mockedRequest.mockImplementation((options, callback) => {
      capturedOptions = options;
      const request = new MockClientRequest();
      const response = new MockIncomingMessage([
        '{"data":{"invoke":"New ',
        'Delhi"}}',
      ]);

      process.nextTick(() => {
        (callback as (response: MockIncomingMessage) => void)(response);
        response.flush();
      });

      return request as unknown as ReturnType<typeof https.request>;
    });

    const result = await appSyncRequestCognito(
      {
        config: {
          url: "https://example.appsync-api.us-east-1.amazonaws.com/graphql",
          region: "us-east-1",
        },
        operation: {
          operationName: "InvokeBedrockMutation",
          query: "mutation InvokeBedrockMutation { invoke(prompt: \"hi\") }",
          variables: {},
        },
      },
      "test-id-token"
    );

    expect(result).toEqual({ data: { invoke: "New Delhi" } });
    expect(capturedOptions).toMatchObject({
      host: "example.appsync-api.us-east-1.amazonaws.com",
      headers: expect.objectContaining({
        Authorization: "test-id-token",
      }),
    });
  });

  test("AppSyncRequestApiKey rejects when the response is not valid JSON", async () => {
    mockedRequest.mockImplementation((options, callback) => {
      const request = new MockClientRequest();
      const response = new MockIncomingMessage(["not-json"]);

      process.nextTick(() => {
        (callback as (response: MockIncomingMessage) => void)(response);
        response.flush();
      });

      return request as unknown as ReturnType<typeof https.request>;
    });

    await expect(
      AppSyncRequestApiKey({
        config: {
          url: "https://example.appsync-api.us-east-1.amazonaws.com/graphql",
          region: "us-east-1",
          key: "api-key",
        },
        operation: {
          operationName: "TestOperation",
          query: "query TestOperation { status }",
          variables: {},
        },
      })
    ).rejects.toThrow("Failed to parse AppSync response as JSON");
  });
});
