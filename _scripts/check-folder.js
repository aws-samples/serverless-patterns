// Checks a pattern folder's path against PUBLISHING.md "Folder structure".
//
//   node _scripts/check-folder.js {pattern-folder} [more folders...]
//
// Paths are relative to the repo root. The CLI treats every folder as new.
// validate.js runs the same check on the pattern folders a pull request adds or changes.
//
// Rules:
// - No path segment is named `yaml`. A pattern with no function code is Integration
//   and has no language folder: `{family}/{framework}`.
// - A new pattern folder is nested: `{family}/{language}/{framework}` or `{family}/{framework}`.
//   Existing flat folders such as `sqs-lambda-python-sam` are only checked for `yaml`.
//   A group folder with its own example-pattern.json and patterns inside it, such as
//   `eventbridge-api-destinations`, is the collection's overview and may stay flat.
const fs = require('fs');
const path = require('path');

const PATTERN_FILE = 'example-pattern.json';
const SKIP_DIRS = new Set(['node_modules', '.git', 'cdk.out', '.aws-sam', '.terraform']);

// True if any folder below dir holds an example-pattern.json.
const hasNestedPattern = (dir) => {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory() || SKIP_DIRS.has(entry.name)) continue;
    const child = path.join(dir, entry.name);
    if (fs.existsSync(path.join(child, PATTERN_FILE)) || hasNestedPattern(child)) return true;
  }
  return false;
};

const isGroupFolder = (dir) =>
  fs.existsSync(path.join(dir, PATTERN_FILE)) && hasNestedPattern(dir);

// Returns an array of problems for one pattern folder. folder is relative to repoRoot.
const checkPatternFolder = (folder, repoRoot, { isNew = true } = {}) => {
  const parts = folder.split(/[\\/]/).filter((part) => part && part !== '.');
  const problems = [];
  if (parts.some((part) => part.toLowerCase() === 'yaml')) {
    problems.push(
      `\`${parts.join('/')}\` has a \`yaml\` folder. A pattern with no function code uses language Integration and has no language folder: \`{family}/{framework}\`, e.g. \`sfn-s3/sam\`.`
    );
  }
  if (isNew && parts.length === 1 && !isGroupFolder(path.join(repoRoot, parts[0]))) {
    problems.push(
      `\`${parts[0]}\` is a flat folder. New patterns use \`{family}/{language}/{framework}\`, e.g. \`sqs-lambda/python/sam\`. See PUBLISHING.md "Folder structure".`
    );
  }
  return problems;
};

module.exports = { checkPatternFolder };

if (require.main === module) {
  const repoRoot = path.join(__dirname, '..');
  const folders = process.argv.slice(2);
  if (folders.length === 0) {
    console.error('Usage: node _scripts/check-folder.js {pattern-folder} [more folders...]');
    process.exit(2);
  }
  for (const folder of folders) {
    const problems = checkPatternFolder(folder, repoRoot);
    if (problems.length) {
      process.exitCode = 1;
      console.error(`✘ ${folder}`);
      problems.forEach((problem, index) => console.error(`  ${index + 1}. ${problem.replace(/`/g, '')}`));
    } else {
      console.info(`✔ ${folder}`);
    }
  }
}
