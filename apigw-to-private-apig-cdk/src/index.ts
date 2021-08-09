import * as cdk from "@aws-cdk/core";
import { ApiStack } from "./api/index";
import { VpcStack } from "./vpc/index";
import { buildSync } from "esbuild";
import path from "path";
import config from "./api/config.json"

buildSync({
  bundle: true,
  entryPoints: [path.resolve(__dirname, "api", "lambda", "index.ts")],
  external: ["aws-sdk"],
  format: "cjs",
  outfile: path.join(__dirname, "api", "dist", "index.js"),
  platform: "node",
  sourcemap: true,
  target: "node14.2",
});

const app = new cdk.App();
const idStack = config.prefix;
const vpcStack = new VpcStack(app, `${idStack}Vpc`);
new ApiStack(app, `${idStack}Api`, vpcStack.vpc);
