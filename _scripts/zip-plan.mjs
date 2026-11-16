#!/usr/bin/env node
// Prints where each pattern's zip goes, for .github/workflows/create_update_release.yaml.
//
//   <folders> | node _scripts/zip-plan.mjs              one pattern folder per line on stdin
//   node _scripts/zip-plan.mjs --mapping batch.csv       rows "current_path,new_zip_name"
//   node _scripts/zip-plan.mjs --config dualWriteV1      prints one value from zip-releases.json
//
// Output, one tab-separated line per pattern:
//   folder  zip_name  shard_tag  legacy_names
// legacy_names is a comma-separated list of the Toolkit zip names (legacy-zips.json) that are
// copies of this folder, or "-". Run from the repo root.

import { existsSync, readFileSync } from "node:fs";
import { zipShardTag } from "./zip-shard.mjs";

const readJson = (name) => JSON.parse(readFileSync(new URL(name, import.meta.url), "utf8"));
const config = readJson("./zip-releases.json");
const legacy = readJson("./legacy-zips.json").zips;
const SAFE_NAME = /^[A-Za-z0-9._-]+$/;

const fail = (message) => {
  console.error(`zip-plan: ${message}`);
  process.exit(1);
};

function rowsFromMapping(file) {
  const rows = [];
  for (const [i, raw] of readFileSync(file, "utf8").split(/\r?\n/).entries()) {
    const line = raw.trim();
    if (!line || line.startsWith("#") || (i === 0 && line.startsWith("current_path"))) continue;
    const [folder, zip, extra] = line.split(",").map((s) => s.trim());
    if (!folder || !zip || extra !== undefined) fail(`${file}:${i + 1}: expected "current_path,new_zip_name"`);
    rows.push([folder.replace(/\/+$/, ""), zip.replace(/\.zip$/, "")]);
  }
  return rows;
}

const args = process.argv.slice(2);
if (args[0] === "--config") {
  if (!(args[1] in config)) fail(`no "${args[1]}" in zip-releases.json`);
  console.log(String(config[args[1]]));
  process.exit(0);
}

let rows;
if (args[0] === "--mapping") {
  if (!args[1]) fail("--mapping needs a CSV file");
  rows = rowsFromMapping(args[1]);
} else {
  const folders = readFileSync(0, "utf8").split("\n").map((s) => s.trim().replace(/^\.\//, "")).filter(Boolean);
  rows = folders.map((folder) => [folder, folder.replace(/\//g, "-")]);
}

const legacyByFolder = {};
for (const [name, folder] of Object.entries(legacy)) (legacyByFolder[folder] ??= []).push(name);

const seen = new Set();
for (const [folder, zip] of rows) {
  if (seen.has(zip)) fail(`zip name ${zip} appears twice`);
  seen.add(zip);
  if (!SAFE_NAME.test(zip)) {
    // GitHub rewrites such asset names, so the site's link would 404.
    console.error(`::warning::Skipping ${JSON.stringify(folder)}: zip name has characters other than A-Z a-z 0-9 . _ -`);
    continue;
  }
  if (!existsSync(`${folder}/example-pattern.json`)) fail(`not a pattern folder: ${folder}`);
  console.log([folder, zip, zipShardTag(zip), (legacyByFolder[folder] ?? []).join(",") || "-"].join("\t"));
}
