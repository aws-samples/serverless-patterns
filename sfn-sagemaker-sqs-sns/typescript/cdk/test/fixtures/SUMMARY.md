# Recorded Strands Decider responses

Thirty synthetic tickets (no customer data) sent to a local Strands Decider server with the exact request the state machine sends (the questions in `questions.json`). The raw response of ten of them (the files next to this one) is kept as a test fixture; the table below holds the numbers of all thirty. To record a ticket yourself, post the `request` of a fixture to a Strands Decider server.

The last column is the route the gate takes at the default thresholds (department 0.9, security page 0.7, security clear 0.3). `test/test_gate.py` checks the ten kept fixtures against the synthesized state machine; their expected routes in `expected-routes.json` were written by hand from the numbers in this table.

| Fixture | What it is | Department (confidence) | Urgency (score, confidence) | P(security incident) | Gate outcome / reason |
|---|---|---|---|---|---|
| `01-clear-billing-1` | clear billing | billing (0.951) | 1.82, 0.411 | 0.156 | auto_routed / confident |
| `02-clear-billing-2` | clear billing | billing (0.826) | 1.44, 0.377 | 0.149 | review / low_confidence |
| `03-clear-technical-1` | clear technical | technical (0.896) | 1.68, 0.344 | 0.158 | review / low_confidence |
| `04-clear-technical-2` | clear technical | technical (0.945) | 1.95, 0.398 | 0.186 | auto_routed / confident |
| `05-clear-access-1` | clear account access (canonical ticket a) | account_access (0.940) | 1.81, 0.394 | 0.218 | auto_routed / confident |
| `06-clear-access-2` | clear account access | account_access (0.978) | 1.56, 0.375 | 0.214 | auto_routed / confident |
| `07-clear-sales-1` | clear sales | sales (0.964) | 1.31, 0.414 | 0.145 | auto_routed / confident |
| `08-clear-sales-2` | clear sales | sales (0.939) | 1.27, 0.406 | 0.161 | auto_routed / confident |
| `09-amb-billing-technical` | ambiguous billing vs technical (canonical ticket b) | billing (0.674) | 1.85, 0.384 | 0.158 | review / low_confidence |
| `10-amb-access-technical` | ambiguous access vs technical | account_access (0.622) | 1.71, 0.353 | 0.183 | review / low_confidence |
| `11-amb-sales-billing` | ambiguous sales vs billing | billing (0.616) | 1.44, 0.398 | 0.147 | review / low_confidence |
| `12-amb-vague` | vague | account_access (0.863) | 1.77, 0.383 | 0.400 | review / security_uncertain |
| `13-amb-two-issues` | two unrelated issues | sales (0.547) | 1.22, 0.374 | 0.161 | review / low_confidence |
| `14-amb-emotional` | emotional, no concrete issue | technical (0.203) | 1.50, 0.226 | 0.172 | review / low_confidence |
| `15-sec-hacked` | security incident (canonical ticket c) | account_access (0.801) | 2.31, 0.440 | 0.914 | paged_and_review / security_incident_suspected |
| `16-sec-ransom` | security incident | account_access (0.516) | 2.09, 0.456 | 0.820 | paged_and_review / security_incident_suspected |
| `17-sec-key-leak` | security incident | technical (0.801) | 1.96, 0.408 | 0.844 | paged_and_review / security_incident_suspected |
| `18-sec-phish` | security incident | account_access (0.796) | 1.82, 0.391 | 0.736 | paged_and_review / security_incident_suspected |
| `19-secword-mfa` | security words, not an incident | account_access (0.838) | 1.45, 0.396 | 0.140 | review / low_confidence |
| `20-secword-questionnaire` | security words, not an incident | technical (0.537) | 1.64, 0.440 | 0.147 | review / low_confidence |
| `21-secword-allowlist` | security words, not an incident | technical (0.763) | 1.28, 0.376 | 0.160 | review / low_confidence |
| `22-secword-password-policy` | security words, not an incident | account_access (0.818) | 1.25, 0.408 | 0.141 | review / low_confidence |
| `23-low-feature` | very low urgency | technical (0.857) | 0.98, 0.416 | 0.170 | review / low_confidence |
| `24-low-howto` | very low urgency | technical (0.739) | 0.93, 0.405 | 0.150 | review / low_confidence |
| `25-low-thanks` | very low urgency, no request | technical (0.229) | 1.18, 0.370 | 0.135 | review / low_confidence |
| `26-low-typo` | very low urgency | sales (0.788) | 1.06, 0.372 | 0.168 | review / low_confidence |
| `27-inject-security` | prompt-injection sentence appended to a real incident | account_access (0.784) | 2.13, 0.385 | 0.486 | review / security_uncertain |
| `28-inject-billing` | prompt-injection sentence appended to a billing ticket | billing (0.823) | 1.00, 0.312 | 0.170 | review / low_confidence |
| `29-edge-short` | one-word ticket | technical (0.410) | 1.37, 0.311 | 0.165 | review / low_confidence |
| `30-edge-long` | 7,240 characters (1,732 tokens, inside the model's 4,096-token window) | billing (0.670) | 1.72, 0.306 | 0.163 | review / low_confidence |

Totals at the defaults: 6 auto-routed, 4 paged and sent to review, 20 sent to review.
