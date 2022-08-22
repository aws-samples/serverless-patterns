import { App } from "aws-cdk-lib";
import { ApiStack } from "./api/index";
import { buildSync } from "esbuild";
import path from "node:path";

import config from "./api/config.json";

buildSync({
  bundle: true,
  entryPoints: [path.resolve(__dirname, "api", "lambda", "index.ts")],
  format: "cjs",
  outfile: path.join(__dirname, "api", "dist", "index.js"),
  platform: "node",
  sourcemap: true,
  target: "node16",
});

const app = new App();

new ApiStack(app, `${config.apiName}`, {
  description: `${config.apiDescription}`,
  stackName: `${config.apiName}`,
});

app.synth();
