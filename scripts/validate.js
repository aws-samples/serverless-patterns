const fs = require('fs');
const path = require('path');
const { Octokit } = require('@octokit/rest');

const Validator = require('jsonschema').Validator;
const v = new Validator();
const schema = require('./pattern-schema.json');

const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');
const includeGitHubChanges = process.env.GH_AUTOMATION ? process.env.GH_AUTOMATION === 'true' : true;

const octokit = new Octokit({
  auth: process.env.TOKEN,
});

const buildErrors = (validationErrors) => {
  return validationErrors.map((error) => {
    return {
      path: error.property.replace(/instance\./g, ''),
      message: error.message.replace(/instance\./g, ''),
      data: error.instance,
      stack: error.stack.replace(/instance\./g, ''),
    };
  });
};

const addedFiles = process.env.ADDED_FILES ? process.env.ADDED_FILES.split(',') : [];
const modifiedFiles = process.env.MODIFIED_FILES ? process.env.MODIFIED_FILES.split(',') : [];

const findFile = (array, filename) => array.find((item) => item.includes(filename));

const pathToExamplePattern = findFile([...addedFiles, ...modifiedFiles], 'example-pattern.json');

const main = async () => {
  if (!pathToExamplePattern) {
    console.info('No example-pattern.json found, skipping any validation phase.');
    process.exit(0);
  }

  try {
    const examplePatternData = fs.readFileSync(path.join(__dirname, '../', pathToExamplePattern), {
      encoding: 'utf-8',
    });

    const parsedJSON = JSON.parse(examplePatternData);

    const result = v.validate(parsedJSON, schema);

    if (result.errors.length > 0) {
      const errors = buildErrors(result.errors);

      const errorList = errors.map((error, index) => `${index + 1}. \`${error.path}\`: ${error.stack}\n\n`);

      if (includeGitHubChanges) {
        // Write comment back with errors for
        await octokit.rest.issues.createComment({
          owner,
          repo,
          issue_number: process.env.PR_NUMBER,
          body:
            `@${process.env.GITHUB_ACTOR} your 'example-pattern.json' is missing some key fields, please review below and address any errors you have \n\n` +
            `${errorList.toString().replace(/,/g, '')} \n\n` +
            `_If you need any help, take a look at the [example-pattern file](https://github.com/aws-samples/serverless-patterns/blob/main/_pattern-model/example-pattern.json)._ \n\n` +
            `Make the changes, and push your changes back to this pull request. When all automated checks are successful, the Serverless DA team will process your pull request. \n\n`,
        });
      }

      console.info('includeGitHubChanges', includeGitHubChanges)

      if (!includeGitHubChanges) {
        throw new Error('Failed to validate pattern, errors found');
      }
      console.info('Added comments back to the pull request requesting changes');
    }

    console.info('Everything OK with pattern');
  } catch (error) {
    console.info(error);
    throw Error('Failed to process the example-pattern.json file.');
  }
};

main();
