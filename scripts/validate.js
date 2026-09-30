// Validates example-pattern.json files against the Serverless Land pattern schema
// (pattern-schema.mjs, copied from serverless-land — don't edit it here).
//
// Locally:
//   cd scripts && npm i
//   node scripts/validate.js path/to/example-pattern.json [more files...]
//
// In CI, the files come from the ADDED_FILES and MODIFIED_FILES env vars
// (comma-separated, relative to the repo root). When GH_AUTOMATION is true, the
// script also comments on and labels the pull request (needs TOKEN, PR_NUMBER,
// ACTOR and GITHUB_REPOSITORY).
//
// Exits non-zero if any file fails validation.
const fs = require('fs');
const path = require('path');

const PATTERN_FILE = 'example-pattern.json';
const repoRoot = path.join(__dirname, '..');

const cliFiles = process.argv.slice(2);
const isLocalRun = cliFiles.length > 0;
// GH_AUTOMATION defaults to true for CI runs (existing behaviour) and false for local runs.
const githubAutomation = process.env.GH_AUTOMATION ? process.env.GH_AUTOMATION === 'true' : !isLocalRun;

const splitList = (value) => (value ? value.split(',').map((f) => f.trim()).filter(Boolean) : []);

// Local paths are relative to the current directory; CI paths are relative to the repo root.
const patternFiles = isLocalRun
  ? cliFiles.map((f) => path.resolve(f))
  : [...new Set([...splitList(process.env.ADDED_FILES), ...splitList(process.env.MODIFIED_FILES)])]
      .filter((f) => path.basename(f) === PATTERN_FILE)
      .map((f) => path.join(repoRoot, f));

let github;
const getGitHub = () => {
  if (!github) {
    const { Octokit } = require('@octokit/rest');
    const [owner, repo] = (process.env.GITHUB_REPOSITORY || '').split('/');
    github = {
      octokit: new Octokit({ auth: process.env.TOKEN }),
      issue: { owner, repo, issue_number: process.env.PR_NUMBER },
    };
  }
  return github;
};

const addLabels = (labels) => {
  const { octokit, issue } = getGitHub();
  return octokit.rest.issues.addLabels({ ...issue, labels });
};

const comment = (body) => {
  const { octokit, issue } = getGitHub();
  return octokit.rest.issues.createComment({ ...issue, body });
};

const removeLabel = async (name) => {
  const { octokit, issue } = getGitHub();
  try {
    await octokit.rest.issues.removeLabel({ ...issue, name });
  } catch (error) {
    // The label isn't on the PR. That's fine.
  }
};

// Zod reports a missing field as "expected string, received undefined". Say it plainly.
const formatIssue = (issue) => {
  const where = issue.path.length ? issue.path.join('.') : '(file)';
  const message =
    issue.code === 'invalid_type' && /received undefined/.test(issue.message) ? 'is required' : issue.message;
  return `\`${where}\`: ${message}`;
};

// Returns { parsed, errors } for one file. errors is an array of strings.
const validateFile = (schema, file) => {
  let parsed;
  try {
    parsed = JSON.parse(fs.readFileSync(file, 'utf-8'));
  } catch (error) {
    return { errors: [`Could not read ${PATTERN_FILE} as JSON: ${error.message}`] };
  }
  const result = schema.safeParse(parsed);
  return { parsed, errors: result.success ? [] : result.error.issues.map(formatIssue) };
};

const reportMissingFile = async () => {
  console.info(`No ${PATTERN_FILE} found, skipping any validation phase.`);
  if (!githubAutomation) return;
  await addLabels(['missing-example-pattern-file']);
  await comment(
    `@${process.env.ACTOR} looks like you are missing the example-pattern.json file in your pattern. \n\n` +
      `You can [find the example-pattern template here](https://github.com/aws-samples/serverless-patterns/blob/main/_pattern-model/example-pattern.json). \n\n` +
      `The file is used on ServerlessLand and is required. Once the file is added we can review the pattern. \n\n`
  );
};

const reportErrors = async (failures) => {
  const sections = failures.map(({ file, errors }) => {
    const list = errors.map((error, index) => `${index + 1}. ${error}`).join('\n');
    return `**${path.relative(repoRoot, file)}**\n\n${list}`;
  });
  if (!githubAutomation) return;
  await comment(
    `@${process.env.ACTOR} your 'example-pattern.json' is missing some key fields, please review below and address any errors you have \n\n` +
      `${sections.join('\n\n')} \n\n` +
      `_If you need any help, take a look at the [example-pattern file](https://github.com/aws-samples/serverless-patterns/blob/main/_pattern-model/example-pattern.json)._ \n\n` +
      `Make the changes, and push your changes back to this pull request. When all automated checks are successful, the Serverless DA team will process your pull request. \n\n`
  );
  await addLabels(['invalid-example-pattern-file', 'requested-changes']);
  console.info('Errors found: Added comments back to the pull request requesting changes');
};

const reportSuccess = async (parsedPatterns) => {
  if (!githubAutomation) return;
  try {
    await addLabels(['valid-example-pattern-file']);
    const { octokit, issue } = getGitHub();
    const pullRequestInfo = await octokit.rest.pulls.get({
      owner: issue.owner,
      repo: issue.repo,
      pull_number: issue.issue_number,
    });
    const forkOwner = pullRequestInfo.data.head.repo.full_name;
    const forkRepo = pullRequestInfo.data.head.ref;
    const forkURL = `https://github.com/${forkOwner}/tree/${forkRepo}`;
    for (const parsedJSON of parsedPatterns) {
      await comment(
        `Valid pattern file found. \n\n` +
          `Reviewer you can view the [pattern file here](https://beta.serverlessland.com/patterns/sandbox?repo=${encodeURIComponent(forkURL)}&pattern=${encodeURIComponent(JSON.stringify(parsedJSON))}) \n\n`
      );
    }
  } catch (error) {
    console.info(`Failed generating preview. Error - ${error.message}`);
  }
  await removeLabel('requested-changes');
  await removeLabel('missing-example-pattern-file');
};

const main = async () => {
  if (patternFiles.length === 0) {
    await reportMissingFile();
    return;
  }

  const { createPatternSchema } = await import('./pattern-schema.mjs');
  // No servicesMap here, so patternArch service keys aren't checked.
  const schema = createPatternSchema();

  const failures = [];
  const parsedPatterns = [];
  for (const file of patternFiles) {
    const { parsed, errors } = validateFile(schema, file);
    const name = path.relative(process.cwd(), file);
    if (errors.length) {
      failures.push({ file, errors });
      console.error(`✘ ${name}`);
      errors.forEach((error, index) => console.error(`  ${index + 1}. ${error}`));
    } else {
      parsedPatterns.push(parsed);
      console.info(`✔ ${name}`);
    }
  }

  if (failures.length) {
    await reportErrors(failures);
    process.exitCode = 1;
    return;
  }

  await reportSuccess(parsedPatterns);
  console.info('Everything OK with pattern');
};

main().catch((error) => {
  console.error(error);
  console.error(`Failed to process the ${PATTERN_FILE} file.`);
  process.exitCode = 1;
});
