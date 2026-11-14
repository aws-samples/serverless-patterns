// node --test _scripts/check-folder.test.js
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { checkPatternFolder } = require('./check-folder');

// A small repo: one group folder with a pattern inside it, one flat pattern.
const root = fs.mkdtempSync(path.join(os.tmpdir(), 'check-folder-'));
const addPattern = (folder) => {
  fs.mkdirSync(path.join(root, folder), { recursive: true });
  fs.writeFileSync(path.join(root, folder, 'example-pattern.json'), '{}');
};
addPattern('eventbridge-api-destinations');
addPattern('eventbridge-api-destinations/2-slack');
addPattern('sqs-lambda-python-sam');

test('nested paths pass', () => {
  assert.deepEqual(checkPatternFolder('sqs-lambda/python/sam', root), []);
  assert.deepEqual(checkPatternFolder('apigw-sqs/sam', root), []);
  assert.deepEqual(checkPatternFolder('alb-lambda/nodejs/serverlessframework', root), []);
  assert.deepEqual(checkPatternFolder('eventbridge-api-destinations/2-slack', root), []);
});

test('a yaml segment fails, new or not', () => {
  assert.equal(checkPatternFolder('sfn-s3/yaml/sam', root).length, 1);
  assert.equal(checkPatternFolder('sfn-s3/YAML/sam', root, { isNew: false }).length, 1);
  assert.equal(checkPatternFolder('yaml', root, { isNew: false }).length, 1);
});

test('a new flat folder fails, an existing one passes', () => {
  assert.equal(checkPatternFolder('sqs-lambda-python-sam', root).length, 1);
  assert.deepEqual(checkPatternFolder('sqs-lambda-python-sam', root, { isNew: false }), []);
});

test('a group folder with its own example-pattern.json may stay flat', () => {
  assert.deepEqual(checkPatternFolder('eventbridge-api-destinations', root), []);
});

test('segments named like yaml but longer pass', () => {
  assert.deepEqual(checkPatternFolder('yaml-parser/python/sam', root), []);
});
