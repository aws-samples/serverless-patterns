// SPDX-License-Identifier: MIT-0
// A pool keeps suspended, already warm MicroVMs so that take() resumes one
// instead of creating a new MicroVM. Each pooled MicroVM is billed while it is
// parked (see the README, Cost), so keep the pool small and close it.
import { SandboxPool } from "rayito";

const template = process.env["RAYITO_TEMPLATE"];
if (!template) {
  throw new Error("export RAYITO_TEMPLATE=<SandboxImageName output of the stack>");
}

// `await using` closes the pool, which terminates the parked MicroVMs.
// start() returns at once and a background filler warms and parks the slot.
await using pool = await new SandboxPool({ size: 1, template }).start();

// waitMs makes take() wait for the filler instead of falling back to create().
const started = Date.now();
const sbx = await pool.take({ waitMs: 120_000 });
try {
  console.log(`take() returned a usable sandbox after ${Date.now() - started} ms`);
  console.log("runCode:", (await sbx.runCode("sum(range(10))")).text);
} finally {
  await sbx.kill();
}
const { takes, hits, misses } = pool.stats();
console.log("stats:", JSON.stringify({ takes, hits, misses }));
