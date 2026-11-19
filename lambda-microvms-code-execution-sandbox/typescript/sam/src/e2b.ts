// SPDX-License-Identifier: MIT-0
// The same sandbox through the E2B-compatible entry point, which implements a
// subset of the E2B JavaScript SDK API (see the Rayito docs for the exact
// surface). Code that uses that subset only needs a different import.
import { Sandbox } from "rayito/e2b";

if (!process.env["RAYITO_TEMPLATE"]) {
  throw new Error("export RAYITO_TEMPLATE=<SandboxImageName output of the stack>");
}

await using sbx = await Sandbox.create({ timeoutMs: 5 * 60_000 });
console.log("runCode:", (await sbx.runCode("1 + 1")).text);
await sbx.files.write("/home/user/a.txt", "hello");
console.log("files.read:", await sbx.files.read("/home/user/a.txt"));
