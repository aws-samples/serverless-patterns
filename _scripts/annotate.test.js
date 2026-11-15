// node --test _scripts/annotate.test.js
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { escapeData, escapeProperty, errorCommand, summaryMarkdown } = require('./annotate');

test('escapeData escapes %, CR and LF', () => {
  assert.equal(escapeData('100% done\r\nnext'), '100%25 done%0D%0Anext');
});

test('escapeProperty also escapes : and ,', () => {
  assert.equal(escapeProperty('a:b,c%'), 'a%3Ab%2Cc%25');
});

test('errorCommand builds file, line and title, and strips backticks from the message', () => {
  const line = errorCommand({
    pattern: 'sqs-lambda/python/sam',
    check: 'Broad IAM',
    file: 'sqs-lambda/python/sam/template.yaml',
    line: 12,
    message: 'grants every action on every resource: `Action: "*"`',
  });
  assert.equal(
    line,
    '::error file=sqs-lambda/python/sam/template.yaml,line=12,title=Broad IAM%3A sqs-lambda/python/sam::grants every action on every resource: Action: "*"'
  );
});

test('errorCommand leaves out line when it is not known', () => {
  const line = errorCommand({ pattern: 'p', check: 'Pattern file', file: 'p/example-pattern.json', message: 'x' });
  assert.equal(line, '::error file=p/example-pattern.json,title=Pattern file%3A p::x');
});

test('summaryMarkdown reports a pass', () => {
  assert.match(summaryMarkdown([]), /All checks passed/);
});

test('summaryMarkdown lists problems in a table and escapes pipes', () => {
  const md = summaryMarkdown([{ pattern: 'p', check: 'Pattern file', file: 'p/example-pattern.json', message: 'a | b\nc' }]);
  assert.match(md, /1 problem found/);
  assert.match(md, /\| `p` \| Pattern file \| a \\\| b c \|/);
  assert.match(md, /PUBLISHING\.md#pattern-checklist/);
});
