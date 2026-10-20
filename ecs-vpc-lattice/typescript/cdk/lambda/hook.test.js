// Local test, no AWS needed: node --test lambda/hook.test.js
const test = require('node:test');
const assert = require('node:assert');
const { probe, parseHookDetails, parseHookDetailsChecked } = require('./hook.js');

const reply = (status, body) => async () => ({ status, text: async () => body });

test('succeeds when the test listener reports the expected version', async () => {
  const seen = [];
  const doFetch = async (url, init) => { seen.push(init.headers['x-environment']); return reply(200, '{"version":"v2"}')(); };
  const r = await probe({ url: 'http://example.test/', expectedVersion: 'v2', doFetch, attempts: 2, delayMs: 1 });
  assert.strictEqual(r.ok, true);
  assert.deepStrictEqual(seen, ['test']);
});

test('fails when the test listener still reports the old version', async () => {
  const r = await probe({ url: 'http://example.test/', expectedVersion: 'v2', doFetch: reply(200, '{"version":"v1"}'), attempts: 2, delayMs: 1 });
  assert.strictEqual(r.ok, false);
  assert.strictEqual(r.last.version, 'v1');
});

test('retries after a network error and then succeeds', async () => {
  let n = 0;
  const doFetch = async () => { if (n++ === 0) throw new Error('timeout'); return reply(200, '{"version":"v2"}')(); };
  const r = await probe({ url: 'http://example.test/', expectedVersion: 'v2', doFetch, attempts: 3, delayMs: 1 });
  assert.strictEqual(r.ok, true);
});

test('fails on non-200 and on a non-JSON body', async () => {
  assert.strictEqual((await probe({ url: 'u', expectedVersion: 'v2', doFetch: reply(503, '{"version":"v2"}'), attempts: 1 })).ok, false);
  assert.strictEqual((await probe({ url: 'u', expectedVersion: 'v2', doFetch: reply(200, 'oops'), attempts: 1 })).ok, false);
});

test('handler returns FAILED without hookDetails', async () => {
  const { handler } = require('./hook.js');
  const r = await handler({ lifecycleStage: 'POST_TEST_TRAFFIC_SHIFT' });
  assert.strictEqual(r.hookStatus, 'FAILED');
});

test('hookDetails is accepted as a JSON string or as an object', () => {
  const details = { url: 'http://example.test/', expectedVersion: 'v2' };
  assert.deepStrictEqual(parseHookDetails(JSON.stringify(details)), details);
  assert.deepStrictEqual(parseHookDetails(details), details);
  assert.deepStrictEqual(parseHookDetails('not json'), {});
  assert.deepStrictEqual(parseHookDetails(undefined), {});
});

test('a malformed hookDetails string is distinguished from a missing one', () => {
  assert.strictEqual(parseHookDetailsChecked('not json').malformed, true);
  assert.strictEqual(parseHookDetailsChecked(undefined).malformed, false);
  assert.strictEqual(parseHookDetailsChecked('{"url":"u"}').malformed, false);
});
