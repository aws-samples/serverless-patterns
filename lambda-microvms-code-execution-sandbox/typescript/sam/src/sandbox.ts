// SPDX-License-Identifier: MIT-0
// Create a sandbox on AWS Lambda MicroVMs, run code and commands, use its
// filesystem, pause and resume it, then terminate it. RAYITO_TEMPLATE (the
// stack output SandboxImageName) selects the image, AWS_REGION the Region;
// credentials come from the default AWS credential chain.
import { Sandbox } from "rayito";

const template = process.env["RAYITO_TEMPLATE"];
if (!template) {
  throw new Error("export RAYITO_TEMPLATE=<SandboxImageName output of the stack>");
}

const started = Date.now();
// One MicroVM per sandbox. `await using` terminates it when the block ends,
// also on errors; timeoutMs is a server-side deadline as a second safety net.
await using sbx = await Sandbox.create({
  template,
  timeoutMs: 10 * 60_000,
  metadata: { pattern: "lambda-microvms-code-execution-sandbox" },
});
console.log(`sandbox created in ${Date.now() - started} ms`);

// Stateful Python: variables survive between runCode calls (Jupyter kernel).
await sbx.runCode("x = 40");
console.log("runCode:", (await sbx.runCode("x + 2")).text);

// Shell commands, with exit code and output.
const uname = await sbx.commands.run("uname -sm");
console.log("commands.run:", uname.exitCode, uname.stdout.trim());

// Filesystem: write a script, run it, read its output back.
await sbx.files.write("/home/user/hello.py", 'open("/home/user/out.txt", "w").write("hello from the MicroVM")\n');
await sbx.commands.run("python3 /home/user/hello.py");
console.log("files.read:", await sbx.files.read("/home/user/out.txt"));
console.log(
  "files.list:",
  (await sbx.files.list("/home/user"))
    .map((entry) => entry.name)
    .filter((name) => !name.startsWith("."))
    .sort()
    .join(", "),
);

// Pause freezes the whole MicroVM (memory included); resume wakes it up with
// the kernel variables and files as they were.
await sbx.pause();
await sbx.resume();
console.log("after pause/resume:", (await sbx.runCode("x + 2")).text);

console.log(`done in ${Date.now() - started} ms; terminating the sandbox`);
