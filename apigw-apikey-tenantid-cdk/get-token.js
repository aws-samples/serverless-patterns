#!/usr/bin/env node

// Usage:
//   node get-token.js --user-pool-id <id> --client-id <id> --username <email> --password <pass> --api-url <url>
//
// Authenticates with Cognito, retrieves an ID token, and calls the API Gateway endpoint.

const {
  CognitoIdentityProviderClient,
  InitiateAuthCommand,
} = require("@aws-sdk/client-cognito-identity-provider");
const https = require("https");
const http = require("http");

function parseArgs() {
  const args = process.argv.slice(2);
  const parsed = {};
  for (let i = 0; i < args.length; i += 2) {
    parsed[args[i].replace(/^--/, "")] = args[i + 1];
  }
  const required = ["user-pool-id", "client-id", "username", "password", "api-url"];
  for (const key of required) {
    if (!parsed[key]) {
      console.error(`Missing required argument: --${key}`);
      process.exit(1);
    }
  }
  return parsed;
}

async function getToken(clientId, username, password) {
  const client = new CognitoIdentityProviderClient();
  const resp = await client.send(
    new InitiateAuthCommand({
      AuthFlow: "USER_PASSWORD_AUTH",
      ClientId: clientId,
      AuthParameters: { USERNAME: username, PASSWORD: password },
    })
  );
  return resp.AuthenticationResult.IdToken;
}

function callApi(url, token) {
  return new Promise((resolve, reject) => {
    const mod = url.startsWith("https") ? https : http;
    const req = mod.get(url, { headers: { Authorization: `Bearer ${token}` } }, (res) => {
      let body = "";
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () => {
        console.log(`Status: ${res.statusCode}`);
        try { console.log(JSON.stringify(JSON.parse(body), null, 2)); }
        catch { console.log(body); }
        resolve();
      });
    });
    req.on("error", reject);
  });
}

(async () => {
  const args = parseArgs();
  try {
    console.log("Authenticating with Cognito...");
    const token = await getToken(args["client-id"], args.username, args.password);
    console.log("Token obtained. Calling API...\n");
    await callApi(args["api-url"], token);
  } catch (err) {
    console.error("Error:", err.message);
    process.exit(1);
  }
})();
