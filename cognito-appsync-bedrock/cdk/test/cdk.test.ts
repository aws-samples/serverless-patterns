import {
  AdminConfirmSignUpCommand,
  AdminDeleteUserCommand,
  AuthFlowType,
  CognitoIdentityProviderClient,
  InitiateAuthCommand,
  SignUpCommand,
} from "@aws-sdk/client-cognito-identity-provider";
import { readFileSync } from "fs";
import { appSyncRequestCognito } from "../src/appsyncRequest";

let APPSYNC_URL = "";
let REGION = "";
let USER_POOL_ID = "";
let USER_POOL_CLIENT_ID = "";
let cognitoClient: CognitoIdentityProviderClient;

const testUserSuffix = Date.now();
const TEST_USER_EMAIL = `testuser_${testUserSuffix}@example.com`;
const TEST_USER_PASSWORD = "SecurePassword123!";

let idToken: string | null = null;

beforeAll(async () => {
  let cdkOutputs;
  try {
    const cdkOutputsFile = readFileSync("cdk-outputs.json");
    cdkOutputs = JSON.parse(cdkOutputsFile.toString());
  } catch (error) {
    console.error("Failed to read or parse cdk-outputs.json:", error);
    throw new Error(
      "cdk-outputs.json not found or is invalid. Deploy your CDK stack first."
    );
  }

  const stackName = "AppsyncBedrockCognitoStack"; // Ensure this matches your deployed stack name
  const stackOutputs = cdkOutputs[stackName];

  if (!stackOutputs) {
    throw new Error(
      `Stack outputs for '${stackName}' not found in cdk-outputs.json. Check stack name and deployment.`
    );
  }

  APPSYNC_URL = stackOutputs.GraphQLApiUrl;
  REGION = stackOutputs.AWSRegion;
  USER_POOL_ID = stackOutputs.CognitoUserPoolId;
  USER_POOL_CLIENT_ID = stackOutputs.CognitoUserPoolClientId;

  if (!APPSYNC_URL || !REGION || !USER_POOL_ID || !USER_POOL_CLIENT_ID) {
    console.error("Missing CDK outputs:", {
      APPSYNC_URL,
      REGION,
      USER_POOL_ID,
      USER_POOL_CLIENT_ID,
    });
    throw new Error(
      "One or more required CDK outputs are missing from cdk-outputs.json."
    );
  }

  cognitoClient = new CognitoIdentityProviderClient({ region: REGION });

  console.log(`Attempting to sign up test user: ${TEST_USER_EMAIL}`);
  try {
    await cognitoClient.send(
      new SignUpCommand({
        ClientId: USER_POOL_CLIENT_ID,
        Username: TEST_USER_EMAIL,
        Password: TEST_USER_PASSWORD,
        UserAttributes: [{ Name: "email", Value: TEST_USER_EMAIL }],
      })
    );
    console.log(`Test user ${TEST_USER_EMAIL} sign-up initiated.`);
  } catch (error: any) {
    if (error.name === "UsernameExistsException") {
      console.warn(`Test user ${TEST_USER_EMAIL} already exists.`);
    } else {
      console.error("Error during sign up:", error);
      throw error;
    }
  }

  console.log(`Attempting to admin-confirm test user: ${TEST_USER_EMAIL}`);
  try {
    await cognitoClient.send(
      new AdminConfirmSignUpCommand({
        UserPoolId: USER_POOL_ID,
        Username: TEST_USER_EMAIL,
      })
    );
    console.log(`Test user ${TEST_USER_EMAIL} confirmed by admin.`);
  } catch (error) {
    console.error("Error during admin confirm sign up:", error);
    throw error;
  }

  console.log(`Attempting to log in test user: ${TEST_USER_EMAIL}`);
  try {
    const authResponse = await cognitoClient.send(
      new InitiateAuthCommand({
        AuthFlow: AuthFlowType.USER_PASSWORD_AUTH,
        ClientId: USER_POOL_CLIENT_ID,
        AuthParameters: {
          USERNAME: TEST_USER_EMAIL,
          PASSWORD: TEST_USER_PASSWORD,
        },
      })
    );
    idToken = authResponse.AuthenticationResult?.IdToken ?? null;
    if (!idToken) throw new Error("Failed to retrieve ID token.");
    console.log(`Test user ${TEST_USER_EMAIL} logged in. ID token obtained.`);
  } catch (error) {
    console.error("Error during initiate auth (login):", error);
    throw error;
  }
}, 90000);

afterAll(async () => {
  if (TEST_USER_EMAIL && USER_POOL_ID && cognitoClient) {
    console.log(`Attempting to delete test user: ${TEST_USER_EMAIL}`);
    try {
      await cognitoClient.send(
        new AdminDeleteUserCommand({
          UserPoolId: USER_POOL_ID,
          Username: TEST_USER_EMAIL,
        })
      );
      console.log(`Test user ${TEST_USER_EMAIL} deleted successfully.`);
    } catch (error: any) {
      if (error.name === "UserNotFoundException") {
        console.warn(
          `Test user ${TEST_USER_EMAIL} was already deleted or not found.`
        );
      } else {
        console.error(`Failed to delete test user ${TEST_USER_EMAIL}:`, error);
      }
    }
  }
}, 30000);

describe("Bedrock Model invoked with Programmatic Cognito Auth (Lambda Resolver)", () => {
  test("The user performs the invoke mutation using a programmatically obtained Cognito ID token", async () => {
    if (!idToken) {
      throw new Error(
        "ID token was not obtained in beforeAll. Cannot run test."
      );
    }

    const prompt = "What is the capital of India?";
    const operationName = "InvokeBedrockMutation"; // Aligned name

    console.log(
      `Calling AppSync mutation (via Lambda resolver) with prompt: "${prompt}"`
    );

    const mutationPromise = await appSyncRequestCognito<{ invoke: string }>(
      {
        config: { url: APPSYNC_URL, region: REGION },
        operation: {
          operationName: operationName, // Use aligned name
          query: `mutation ${operationName}($prompt: String!) {
            invoke(prompt: $prompt)
          }`,
          variables: { prompt: prompt },
        },
      },
      idToken
    );

    console.log(
      "AppSync Mutation Response:",
      JSON.stringify(mutationPromise, null, 2)
    );

    if (mutationPromise?.errors) {
      console.error("GraphQL Errors:", mutationPromise.errors);
      mutationPromise.errors.forEach((err) =>
        console.error(JSON.stringify(err, null, 2))
      );
      throw new Error(
        `GraphQL request failed: ${
          mutationPromise.errors[0]?.message || "Unknown GraphQL error"
        }`
      );
    }

    expect(mutationPromise?.data).toBeDefined();
    expect(mutationPromise.data?.invoke).toBeTruthy();
    expect(typeof mutationPromise.data?.invoke).toBe("string");
    if (prompt === "What is the capital of India?") {
      expect(mutationPromise.data?.invoke.toLowerCase()).toContain("delhi");
    }
  });
});
