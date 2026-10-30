// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// Mocked-Jev test for the confidence-gate branch logic. No AWS calls, no
// network - it feeds mocked Jev responses through the handler's normalizer and
// through a local mirror of the Step Functions Choice-state thresholds, then
// asserts each ticket lands in the correct branch.
//
// Run: node test/decision.test.js

"use strict";

const assert = require("assert");
const { normalizeDecision, buildJevRequest } = require("../src/decision");

// Mirror of the Step Functions Choice thresholds in
// lib/jev-confidence-gated-triage-stack.ts. Kept in sync deliberately so this
// test proves the exact gate the deployed workflow enforces.
function gate(decision) {
  const confidentSecurity =
    decision.security.value === true && decision.security.confidence >= 0.9;
  const confidentRouting =
    decision.department.confidence >= 0.6 && decision.urgency.confidence >= 0.7;
  if (confidentSecurity) return "page_security";
  if (confidentRouting) return "auto_route";
  return "human_review";
}

let passed = 0;
function check(name, actual, expected) {
  assert.strictEqual(actual, expected, `${name}: expected ${expected}, got ${actual}`);
  console.log(`  ok - ${name}`);
  passed += 1;
}

// --- normalizeDecision -------------------------------------------------------
// Mocks use the REAL TypeSafe System One response shape (answers keyed by
// question name, type-specific fields):
//   choice -> { type, choice, confidence, probabilities }
//   score  -> { type, score, confidence, legend, probabilities }
//   noul   -> { type, noul }   (probability only; no confidence field)
const jevHigh = {
  model: "jev-1.13.0",
  answers: {
    department: {
      type: "choice",
      choice: "technical_support",
      confidence: 0.94,
      probabilities: { technical_support: 0.94, billing: 0.04, general: 0.02, account_security: 0.0 },
    },
    urgency: {
      type: "score",
      score: 4,
      confidence: 0.88,
      probabilities: { 0: 0.0, 1: 0.02, 2: 0.05, 3: 0.05, 4: 0.88 },
    },
    // noul near 0 -> "not a security incident", high confidence.
    security: { type: "noul", noul: 0.02 },
  },
};
const normHigh = normalizeDecision(jevHigh);
check("normalize reads choice value", normHigh.department.value, "technical_support");
check("normalize reads choice confidence", normHigh.department.confidence, 0.94);
check("normalize reads score value", normHigh.urgency.value, 4);
check("normalize reads score confidence", normHigh.urgency.confidence, 0.88);
// noul 0.02 -> value false, confidence |0.02 - 0.5| * 2 = 0.96.
check("normalize derives noul value (false)", normHigh.security.value, false);
check("normalize derives noul confidence", Number(normHigh.security.confidence.toFixed(4)), 0.96);

// Missing/garbage answers default to a safe fallback that forces human review
// rather than a false auto-route.
const normEmpty = normalizeDecision({});
check("normalize missing choice -> confidence 0", normEmpty.department.confidence, 0);
check("normalize missing score -> value null", normEmpty.urgency.value, null);
// A missing noul is treated as noul 0 -> value false, confidence 1.0 in the
// "false" direction, so the security page never fires on absent evidence.
check("normalize missing noul -> value false", normEmpty.security.value, false);

// --- buildJevRequest ---------------------------------------------------------
const req = buildJevRequest({ subject: "hi", body: "x" });
check("request has 3 typed questions", Object.keys(req.questions).length, 3);
check("department is a choice question", req.questions.department.type, "choice");
check("urgency is a score question", req.questions.urgency.type, "score");
check("security is a noul question", req.questions.security.type, "noul");
check("state is serialized ticket", typeof req.state, "string");

// --- the confidence gate -----------------------------------------------------

// High confidence, not security -> auto-route.
check("high-confidence ticket auto-routes", gate(normHigh), "auto_route");

// Ambiguous ticket: low department/urgency confidence -> human review.
check(
  "low-confidence ticket goes to human review",
  gate(
    normalizeDecision({
      answers: {
        department: { type: "choice", choice: "general", confidence: 0.42 },
        urgency: { type: "score", score: 2, confidence: 0.51 },
        security: { type: "noul", noul: 0.2 },
      },
    })
  ),
  "human_review"
);

// Security incident above the 0.9 bar -> page on-call.
// noul 0.965 -> value true, confidence |0.965 - 0.5| * 2 = 0.93.
check(
  "high-confidence security incident pages on-call",
  gate(
    normalizeDecision({
      answers: {
        department: { type: "choice", choice: "account_security", confidence: 0.9 },
        urgency: { type: "score", score: 5, confidence: 0.95 },
        security: { type: "noul", noul: 0.965 },
      },
    })
  ),
  "page_security"
);

// Security suspected but BELOW the 0.9 bar -> not paged; routing confidence is
// high, so it auto-routes rather than paging on weak evidence.
// noul 0.85 -> value true, confidence |0.85 - 0.5| * 2 = 0.7 (< 0.9).
check(
  "low-confidence security does NOT page (auto-routes)",
  gate(
    normalizeDecision({
      answers: {
        department: { type: "choice", choice: "account_security", confidence: 0.8 },
        urgency: { type: "score", score: 4, confidence: 0.82 },
        security: { type: "noul", noul: 0.85 },
      },
    })
  ),
  "auto_route"
);

// Department confident but urgency uncertain -> human review (both must clear).
// noul 0.05 -> value false, confidence 0.9.
check(
  "partial routing confidence goes to human review",
  gate(
    normalizeDecision({
      answers: {
        department: { type: "choice", choice: "billing", confidence: 0.95 },
        urgency: { type: "score", score: 3, confidence: 0.55 },
        security: { type: "noul", noul: 0.05 },
      },
    })
  ),
  "human_review"
);

console.log(`\nAll ${passed} assertions passed.`);
