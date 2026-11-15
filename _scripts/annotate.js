// Reports validate.js problems in GitHub Actions without commenting on the pull request:
// each problem becomes an ::error workflow command (shown on the PR's Files changed tab
// and the run's summary), and a Markdown table goes to the job summary.
//
// A problem is { pattern, check, file, line, message }. pattern and file are relative to
// the repo root; line is optional.
const PUBLISHING_URL = 'https://github.com/aws-samples/serverless-patterns/blob/main/PUBLISHING.md#pattern-checklist';

// Escaping rules for workflow commands:
// https://github.com/actions/toolkit/blob/main/packages/core/src/command.ts
const escapeData = (value) => String(value).replace(/%/g, '%25').replace(/\r/g, '%0D').replace(/\n/g, '%0A');
const escapeProperty = (value) => escapeData(value).replace(/:/g, '%3A').replace(/,/g, '%2C');

const plain = (text) => String(text).replace(/`/g, '');

const errorCommand = ({ file, line, check, pattern, message }) => {
  const props = [`file=${escapeProperty(file)}`];
  if (line) props.push(`line=${escapeProperty(line)}`);
  props.push(`title=${escapeProperty(`${check}: ${pattern}`)}`);
  return `::error ${props.join(',')}::${escapeData(plain(message))}`;
};

const cell = (text) => String(text).replace(/\|/g, '\\|').replace(/\r?\n/g, ' ');

const summaryMarkdown = (problems) => {
  if (problems.length === 0) return '### Schema Validation\n\n✅ All checks passed.\n';
  const rows = problems.map(({ pattern, check, message }) => `| \`${cell(pattern)}\` | ${cell(check)} | ${cell(message)} |`);
  return [
    '### Schema Validation',
    '',
    `❌ ${problems.length} problem${problems.length === 1 ? '' : 's'} found.`,
    '',
    '| Pattern | Check | Problem |',
    '| --- | --- | --- |',
    ...rows,
    '',
    `Fix these and push again. The [pattern checklist in PUBLISHING.md](${PUBLISHING_URL}) covers the pattern file, folder structure and IAM rules.`,
    '',
  ].join('\n');
};

module.exports = { escapeData, escapeProperty, errorCommand, summaryMarkdown };
