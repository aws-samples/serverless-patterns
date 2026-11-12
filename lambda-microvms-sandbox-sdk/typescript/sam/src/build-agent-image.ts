// SPDX-License-Identifier: MIT-0
// Optional (EnableAgent=true): compose the agent image <stack>-agent on top
// of <stack>-base-caps. It adds OpenCode (and deepagents) with pinned
// checksums. Takes about 5 minutes; the image is NOT managed by the stack,
// delete it during cleanup (see README).
import { AgentTemplate } from "rayito";

const stack = process.env["STACK_NAME"];
const bucket = process.env["ARTIFACT_BUCKET"];
if (!stack || !bucket) {
  throw new Error("export STACK_NAME=<stack name> ARTIFACT_BUCKET=<artifact bucket>");
}

console.log(`building ${stack}-agent on ${stack}-base-caps (about 5 minutes)...`);
const info = await new AgentTemplate({
  name: `${stack}-agent`,
  base: `${stack}-base-caps`,
  runtimes: ["opencode"],
}).build({ bucket });
console.log(`agent image ready: ${info.alias} (build ${info.buildId})`);
