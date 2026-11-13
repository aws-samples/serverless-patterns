// Which release ("shard") holds a pattern's zip. GitHub allows 1,000 assets
// per release, so pattern zips are spread over ZIP_SHARD_COUNT releases tagged
// zips-1 .. zips-N.
//
// shard = 1 + jumpConsistentHash(fnv1a64(zipName), ZIP_SHARD_COUNT), where
// zipName is the pattern folder path with "/" -> "-" and no ".zip"
// (sqs-lambda/python/sam -> sqs-lambda-python-sam). Jump hash means raising
// the count later moves only about 1/N of the zips.
//
// This file is kept byte-for-byte identical in aws-samples/serverless-patterns
// (_scripts/zip-shard.mjs) and serverless-land (schemas/zip-shard.mjs). Both
// repos test it against the same zip-shard-vectors.json. No imports and BigInt
// only, so it runs in Node and the browser.

export const ZIP_SHARD_COUNT = 16;
export const ZIP_SHARD_TAG_PREFIX = "zips-";

const MASK_64 = (1n << 64n) - 1n;
const FNV_OFFSET = 0xcbf29ce484222325n;
const FNV_PRIME = 0x100000001b3n;
const JUMP_MULTIPLIER = 2862933555777941757n;

/** 64-bit FNV-1a of the string's UTF-8 bytes, as a BigInt. */
export function fnv1a64(text) {
  let hash = FNV_OFFSET;
  for (const byte of new TextEncoder().encode(text)) {
    hash ^= BigInt(byte);
    hash = (hash * FNV_PRIME) & MASK_64;
  }
  return hash;
}

/** Jump consistent hash (Lamping and Veach, 2014): a bucket in 0 .. buckets-1. */
export function jumpConsistentHash(key, buckets) {
  let k = BigInt.asUintN(64, key);
  let b = -1;
  let j = 0;
  while (j < buckets) {
    b = j;
    k = (k * JUMP_MULTIPLIER + 1n) & MASK_64;
    j = Math.floor((b + 1) * (2 ** 31 / Number((k >> 33n) + 1n)));
  }
  return b;
}

/** Shard number, 1 .. count, for a zip name with or without ".zip". */
export function zipShard(zipName, count = ZIP_SHARD_COUNT) {
  const name = String(zipName).replace(/\.zip$/, "");
  return 1 + jumpConsistentHash(fnv1a64(name), count);
}

/** Release tag of a zip's shard, e.g. "zips-7". */
export function zipShardTag(zipName, count = ZIP_SHARD_COUNT) {
  return `${ZIP_SHARD_TAG_PREFIX}${zipShard(zipName, count)}`;
}
