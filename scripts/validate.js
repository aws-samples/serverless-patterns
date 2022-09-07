const fs = require('fs');
const path = require('path');
const { Octokit } = require('@octokit/rest');

const Validator = require('jsonschema').Validator;
const v = new Validator();
const schema = require('./pattern-schema.json');

const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');
const githubAutomation = process.env.GH_AUTOMATION ? process.env.GH_AUTOMATION === 'true' : true;

const octokit = new Octokit({
  auth: process.env.TOKEN,
});

console.info(process.env);

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

    if (githubAutomation) {
      await octokit.rest.issues.addLabels({
        owner,
        repo,
        issue_number: process.env.PR_NUMBER,
        labels: ['missing-example-pattern-file'],
      });

      await octokit.rest.issues.createComment({
        owner,
        repo,
        issue_number: process.env.PR_NUMBER,
        body:
          `@${process.env.ACTOR} looks like you are missing the example-pattern.json file in your pattern. \n\n` +
          `You can [find the example-pattern template here](https://github.com/aws-samples/serverless-patterns/blob/main/_pattern-model/example-pattern.json). \n\n` +
          `The file is used on ServerlessLand and is required. Once the file is added we can review the pattern. \n\n`,
      });
    }

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

      const errorList = errors.map((error, index) => `${index + 1}. \`${error.path}\`: ${error.stack}\n`);

      if (githubAutomation) {
        // Write comment back with errors for
        await octokit.rest.issues.createComment({
          owner,
          repo,
          issue_number: process.env.PR_NUMBER,
          body:
            `@${process.env.ACTOR} your 'example-pattern.json' is missing some key fields, please review below and address any errors you have \n\n` +
            `${errorList.reduce((acc, error) => `${acc}${error}`, '')} \n\n` +
            `_If you need any help, take a look at the [example-pattern file](https://github.com/aws-samples/serverless-patterns/blob/main/_pattern-model/example-pattern.json)._ \n\n` +
            `Make the changes, and push your changes back to this pull request. When all automated checks are successful, the Serverless DA team will process your pull request. \n\n`,
        });

        await octokit.rest.issues.addLabels({
          owner,
          repo,
          issue_number: process.env.PR_NUMBER,
          labels: ['invalid-example-pattern-file', 'requested-changes'],
        });

        throw new Error('Failed to validate pattern, errors found');
      }

      if (!githubAutomation) {
        throw new Error('Failed to validate pattern, errors found');
      }

      console.info('Errors found: Added comments back to the pull request requesting changes');
    } else {
      if (githubAutomation) {
        await octokit.rest.issues.addLabels({
          owner,
          repo,
          issue_number: process.env.PR_NUMBER,
          labels: ['valid-example-pattern-file'],
        });

        try {
          // try and remove labels if they are there, will error if not, but that's OK.
          await octokit.rest.issues.removeLabel({
            owner,
            repo,
            issue_number: process.env.PR_NUMBER,
            name: 'requested-changes',
          });

          await octokit.rest.issues.removeLabel({
            owner,
            repo,
            issue_number: process.env.PR_NUMBER,
            name: 'missing-example-pattern-file',
          });
        } catch (error) {
          // silent fail here
        }
      }

      console.info('Everything OK with pattern');
    }
  } catch (error) {
    console.info(error);
    throw Error('Failed to process the example-pattern.json file.');
  }
};

main();
