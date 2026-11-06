// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

"use strict";

const https = require("https");
const { URL } = require("url");

// AWS SDK clients are created lazily so the pure helper functions can be
// imported (e.g. by unit tests) without the SDK being present on the path.
let secretsClient = null;
let sfnClient = null;

function getSecretsClient() {
  if (!secretsClient) {
    const { SecretsManagerClient } = require("@aws-sdk/client-secrets-manager");
    secretsClient = new SecretsManagerClient({});
  }
  return secretsClient;
}

function getSfnClient() {
  if (!sfnClient) {
    const { SFNClient } = require("@aws-sdk/client-sfn");
    sfnClient = new SFNClient({});
  }
  return sfnClient;
}

// Cache the API key across warm invocations to avoid re-reading the secret.
let cachedApiKey = null;

/**
 * Structured log line. Never log the API key or full secret material.
 */
function log(level, message, extra) {
  const line = { level, message };
  if (extra) {
    Object.assign(line, extra);
  }
  // Single JSON line so CloudWatch Logs Insights can parse it.
  process.stdout.write(JSON.stringify(line) + "\n");
}

/**
 * Read the TypeSafe Jev API key from Amazon Secrets Manager (cached).
 */
async function getApiKey() {
  if (cachedApiKey) {
    return cachedApiKey;
  }
  const secretArn = process.env.JEV_API_KEY_SECRET_ARN;
  if (!secretArn) {
    throw new Error("JEV_API_KEY_SECRET_ARN environment variable is not set");
  }
  try {
    const { GetSecretValueCommand } = require("@aws-sdk/client-secrets-manager");
    const res = await getSecretsClient().send(
      new GetSecretValueCommand({ SecretId: secretArn })
    );
    cachedApiKey = res.SecretString;
    if (!cachedApiKey) {
      throw new Error("Secret has no string value; set the Jev API key first");
    }
    return cachedApiKey;
  } catch (err) {
    log("error", "Failed to read Jev API key from Secrets Manager", {
      error: err.message,
    });
    throw err;
  }
}

/**
 * POST the ticket state plus typed questions to the TypeSafe Jev System One
 * model and return the parsed JSON response.
 */
function callJev(endpoint, apiKey, payload) {
  return new Promise((resolve, reject) => {
    let url;
    try {
      url = new URL(endpoint);
    } catch (err) {
      reject(new Error(`Invalid JEV_ENDPOINT: ${err.message}`));
      return;
    }

    const body = JSON.stringify(payload);
    const options = {
      hostname: url.hostname,
      path: url.pathname + url.search,
      method: "POST",
      port: url.port || 443,
      headers: {
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(body),
        Authorization: `Bearer ${apiKey}`,
      },
      timeout: 10000,
    };

    const req = https.request(options, (res) => {
      let data = "";
      res.on("data", (chunk) => {
        data += chunk;
      });
      res.on("end", () => {
        if (res.statusCode < 200 || res.statusCode >= 300) {
          reject(new Error(`Jev returned HTTP ${res.statusCode}: ${data}`));
          return;
        }
        try {
          resolve(JSON.parse(data));
        } catch (err) {
          reject(new Error(`Failed to parse Jev response: ${err.message}`));
        }
      });
    });

    req.on("timeout", () => {
      req.destroy(new Error("Jev request timed out"));
    });
    req.on("error", (err) => reject(err));
    req.write(body);
    req.end();
  });
}

/**
 * Build the Jev request: the ticket becomes the state, and three typed
 * questions are asked in a single call. Matches the TypeSafe System One
 * request contract:
 *   - every question carries `instructions`
 *   - a `choice` question lists its options in a `criteria` object
 *     (option -> description)
 *   - a `score` question lists its ordered levels in a `criteria` array
 *   - a `noul` question states a proposition; Jev returns the probability
 *     that the proposition is true
 */
function buildJevRequest(ticket) {
  return {
    model: "jev-latest",
    state: JSON.stringify(ticket),
    questions: {
      // choice: which department should own this ticket?
      department: {
        type: "choice",
        instructions: "Which team should own this ticket",
        criteria: {
          billing: "Payment, invoicing, or subscription issues",
          technical_support: "Bugs, errors, or integration problems",
          account_security: "Compromised accounts, unauthorized access, or abuse",
          general: "Anything that does not fit the other categories",
        },
      },
      // score: how urgent is this ticket, on an ordered low-to-critical rubric?
      urgency: {
        type: "score",
        instructions: "How urgent is this ticket",
        criteria: [
          "Not time-sensitive; can wait",
          "Mildly time-sensitive",
          "Time-sensitive; should be handled today",
          "Urgent; actively blocking the customer",
          "Critical; severe or escalating business impact",
        ],
      },
      // noul: a declarative statement; Jev returns P(statement is true).
      security: {
        type: "noul",
        instructions: "The ticket reports an active security incident",
      },
    },
  };
}

/**
 * Normalize Jev's typed answers into the flat shape the Step Functions Choice
 * state branches on: $.decision.<name>.{value, confidence}.
 *
 * Jev returns answers keyed by question name, with type-specific fields
 * (see the TypeSafe API reference):
 *   - choice: { type, choice, confidence, probabilities }
 *   - score:  { type, score, confidence, legend, probabilities }
 *   - noul:   { type, noul }   // probability the statement is true; no
 *                              // separate confidence field
 *
 * For a noul, the calibrated confidence is how decisively the probability
 * departs from a 0.5 coin flip: |noul - 0.5| * 2. A noul near 1.0 is a
 * high-confidence "true"; near 0.0 a high-confidence "false"; near 0.5 is
 * genuinely uncertain and should fall to human review.
 */
function normalizeDecision(jevResponse) {
  const answers = (jevResponse && jevResponse.answers) || {};

  const num = (v) => (typeof v === "number" ? v : 0);

  const choiceAnswer = (name) => {
    const a = answers[name] || {};
    return {
      value: a.choice !== undefined ? a.choice : null,
      confidence: num(a.confidence),
    };
  };

  const scoreAnswer = (name) => {
    const a = answers[name] || {};
    return {
      value: a.score !== undefined ? a.score : null,
      confidence: num(a.confidence),
    };
  };

  const noulAnswer = (name) => {
    const a = answers[name] || {};
    const p = num(a.noul);
    return {
      // The statement is judged true when the probability clears the midpoint.
      value: p >= 0.5,
      // Distance from the coin flip, rescaled to 0-1.
      confidence: Math.abs(p - 0.5) * 2,
    };
  };

  return {
    department: choiceAnswer("department"),
    urgency: scoreAnswer("urgency"),
    security: noulAnswer("security"),
  };
}

exports.handler = async (event) => {
  const endpoint = process.env.JEV_ENDPOINT;
  const stateMachineArn = process.env.STATE_MACHINE_ARN;

  if (!endpoint || !stateMachineArn) {
    log("error", "Missing required environment configuration");
    return {
      statusCode: 500,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "Function is not configured correctly" }),
    };
  }

  // Parse the inbound ticket (API Gateway proxy body).
  let ticket;
  try {
    ticket = event && event.body ? JSON.parse(event.body) : event;
  } catch (err) {
    log("warn", "Invalid ticket payload", { error: err.message });
    return {
      statusCode: 400,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "Request body must be valid JSON" }),
    };
  }

  let decision;
  try {
    const apiKey = await getApiKey();
    const jevResponse = await callJev(endpoint, apiKey, buildJevRequest(ticket));
    decision = normalizeDecision(jevResponse);
    log("info", "Jev decision received", {
      departmentConfidence: decision.department.confidence,
      urgencyConfidence: decision.urgency.confidence,
      securityConfidence: decision.security.confidence,
    });
  } catch (err) {
    log("error", "Jev decision call failed", { error: err.message });
    return {
      statusCode: 502,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "Failed to obtain a triage decision" }),
    };
  }

  // Start the confidence gate (Step Functions) synchronously.
  try {
    const { StartSyncExecutionCommand } = require("@aws-sdk/client-sfn");
    const execution = await getSfnClient().send(
      new StartSyncExecutionCommand({
        stateMachineArn,
        input: JSON.stringify({ ticket, decision }),
      })
    );

    const output = execution.output ? JSON.parse(execution.output) : {};
    log("info", "Triage complete", { status: execution.status });

    return {
      statusCode: 200,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        status: execution.status,
        decision,
        triage: output.triage || output.review || output.paging || null,
      }),
    };
  } catch (err) {
    log("error", "Failed to run the confidence gate", { error: err.message });
    return {
      statusCode: 502,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "Failed to run triage workflow" }),
    };
  }
};

// Exported for unit testing the confidence-gate branch logic.
exports.buildJevRequest = buildJevRequest;
exports.normalizeDecision = normalizeDecision;
