// Materialize Bedrock model discovery into openclaw.json at cold start.
//
// Why: the gateway's image-attachment guard and `models list` read only the
// explicit `models.providers.<id>.models` config array — they never consult the
// plugin's live discovery catalog (OpenClaw integration gap, verified 2026-07).
// So we run the plugin's own discoverBedrockModels() once per cold start
// (measured ~1.3s warm / ~3.3s cold) and write the result into the config the
// guard does read. Fallback: on any failure the config keeps whatever models
// array it already has (the static seed list baked into the image).
//
// Runs as: node materialize-models.mjs <config-path>   (before gateway starts)
import { readFileSync, writeFileSync, readdirSync } from "node:fs";

const CONFIG_PATH = process.argv[2] || "/home/node/.openclaw/openclaw.json";

// The plugin project dir carries a content-hash suffix that changes across
// plugin versions — locate it instead of hardcoding.
function findPluginDir() {
  const projects = "/home/node/.openclaw/npm/projects";
  const entry = readdirSync(projects).find((d) =>
    d.startsWith("openclaw-amazon-bedrock-provider-"),
  );
  if (!entry) throw new Error("bedrock provider plugin dir not found");
  return `${projects}/${entry}/node_modules/@openclaw/amazon-bedrock-provider`;
}

try {
  const cfg = JSON.parse(readFileSync(CONFIG_PATH, "utf8"));
  const provider = cfg?.models?.providers?.["amazon-bedrock"];
  if (!provider) throw new Error("no amazon-bedrock provider in config");

  const discovery =
    cfg?.plugins?.entries?.["amazon-bedrock"]?.config?.discovery ?? {};

  // Honor the actual deploy region. AWS_REGION is injected into the MicroVM at
  // runtime (same reserved var efs-monitor.sh uses for the mount-target DNS). The
  // static config ships a us-east-1 baseUrl / discovery region; without this rewrite
  // a VM launched in any other supported region (us-east-2, us-west-2, eu-west-1,
  // ap-northeast-1) would send inference to us-east-1 instead of its own in-region
  // Bedrock VPC endpoint. Persist the region fixes FIRST so they hold even if model
  // discovery below fails and we fall back to the static seed list.
  const region = process.env.AWS_REGION || discovery.region || "us-east-1";
  provider.baseUrl = `https://bedrock-runtime.${region}.amazonaws.com`;
  if (discovery.region) discovery.region = region;
  writeFileSync(CONFIG_PATH, JSON.stringify(cfg, null, 1));

  if (discovery.enabled === false) {
    console.log("[materialize-models] discovery disabled; keeping static list");
    process.exit(0);
  }

  const { discoverBedrockModels } = await import(
    `${findPluginDir()}/dist/discovery.js`
  );
  const models = await discoverBedrockModels({
    region,
    config: { ...discovery, refreshInterval: 0 },
  });
  if (!Array.isArray(models) || models.length === 0)
    throw new Error("discovery returned no models");

  provider.models = models;
  writeFileSync(CONFIG_PATH, JSON.stringify(cfg, null, 1));
  const withImage = models.filter((m) => m.input?.includes("image")).length;
  console.log(
    `[materialize-models] wrote ${models.length} models (${withImage} vision) to ${CONFIG_PATH}`,
  );
} catch (e) {
  console.log(
    `[materialize-models] FAILED (${String(e.message).slice(0, 120)}); keeping static list`,
  );
}
