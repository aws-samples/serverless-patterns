// node --test _scripts/zip-shard.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import { fnv1a64, zipShard, zipShardTag, ZIP_SHARD_COUNT } from "./zip-shard.mjs";

const vectors = JSON.parse(readFileSync(new URL("./zip-shard-vectors.json", import.meta.url), "utf8"));

test("fnv1a64 matches the published FNV-1a 64 values", () => {
  for (const [text, hex] of Object.entries(vectors.fnv1a64)) {
    assert.equal(fnv1a64(text).toString(16), hex, JSON.stringify(text));
  }
});

test("zipShard matches the shared vectors", () => {
  for (const [name, shard] of Object.entries(vectors.shards)) {
    assert.equal(zipShard(name, vectors.shardCount), shard, name);
    assert.equal(zipShard(`${name}.zip`, vectors.shardCount), shard, `${name}.zip`);
  }
});

test("zipShardTag uses the configured count and the zips- prefix", () => {
  assert.equal(ZIP_SHARD_COUNT, 16);
  assert.equal(zipShardTag("sqs-lambda-nodejs-sam"), "zips-1");
});

test("legacy-zips.json points at pattern folders", () => {
  const { zips } = JSON.parse(readFileSync(new URL("./legacy-zips.json", import.meta.url), "utf8"));
  for (const [name, folder] of Object.entries(zips)) {
    assert.ok(existsSync(new URL(`../${folder}/example-pattern.json`, import.meta.url)), `${name} -> ${folder}`);
  }
});

test("raising the shard count moves only a fraction of zips", () => {
  const names = Array.from({ length: 2000 }, (_, i) => `pattern-${i}`);
  const moved = names.filter((n) => zipShard(n, 16) !== zipShard(n, 17)).length;
  // Jump hash moves about 1/17 (118 of 2,000); a modulo hash would move ~94%.
  assert.ok(moved < 200, `moved ${moved}`);
  assert.ok(names.every((n) => zipShard(n, 17) === zipShard(n, 16) || zipShard(n, 17) === 17));
});
