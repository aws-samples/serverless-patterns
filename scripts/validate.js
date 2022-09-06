const fs = require('fs');
const path = require('path');
const { Octokit } = require('@octokit/rest');

const Validator = require('jsonschema').Validator;
const v = new Validator();

const supportedLanguages = ['TypeScript', 'Node.js', 'Python', 'Java', '.Net', 'C#', 'Go', 'Rust'];
const supportedFrameworks = ['CDK', 'SAM', 'Terraform', 'Serverless Framework'];

const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');

console.log(process.env);

const octokit = new Octokit({
  auth: process.env.TOKEN,
});

const buildErrors = (validationErrors) => {
  return validationErrors.map((error) => {
    return {
      path: error.property.replace(/instance\./g, ''),
      message: error.message.replace(/instance\./g, ''),
      data: error.instance.replace(/instance\./g, ''),
      stack: error.stack.replace(/instance\./g, ''),
    };
  });
};

const patternSchema = {
  id: 'serverless-pattern-schema',
  type: 'object',
  properties: {
    title: { type: 'string' },
    description: { type: 'string' },
    language: {
      type: 'string',
      enum: supportedLanguages,
    },
    framework: {
      type: 'string',
      enum: supportedFrameworks,
    },
    introBox: {
      type: 'object',
      properties: {
        headline: { type: 'string' },
        text: {
          type: 'array',
          items: {
            type: 'string',
          },
        },
      },
      required: ['headline', 'text'],
    },
    gitHub: {
      type: 'object',
      properties: {
        template: {
          type: 'object',
          properties: {
            repoURL: { type: 'string' },
            templateURL: { type: 'string' },
            projectFolder: { type: 'string' },
            templateFile: { type: 'string' },
          },
          required: ['repoURL', 'templateURL', 'projectFolder', 'templateFile'],
        },
      },
      required: ['template'],
    },
    authors: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          bio: { type: 'string' },
        },
        required: ['name', 'bio'],
      },
    },
  },
  required: ['title', 'language', 'framework', 'introBox', 'gitHub', 'authors'],
};

//console.log('VALIDATE 3');
//console.log(process.env);

const addedFiles = process.env.ADDED_FILES ? process.env.ADDED_FILES.split(',') : [];
const modifiedFiles = process.env.MODIFIED_FILES ? process.env.MODIFIED_FILES.split(',') : [];

// const addedFiles = ['/cdk-sfn-s3/example-pattern.json'];
// const modifiedFiles = ['README.md'];

const findFile = (array, filename) => array.find((item) => item.includes(filename));

const pathToExamplePattern = findFile([...addedFiles, ...modifiedFiles], 'example-pattern.json');

const main = async () => {
  if (!pathToExamplePattern) {
    console.log('No example-pattern found, skipping any validation phase.');
    process.exit(0);
  }

  // Read the file contents

  try {
    const examplePatternData = fs.readFileSync(path.join(__dirname, '../', pathToExamplePattern), {
      encoding: 'utf-8',
    });

    const parsedJSON = JSON.parse(examplePatternData);

    const result = v.validate(parsedJSON, patternSchema);

    if (result.errors.length > 0) {
      const errors = buildErrors(result.errors);
      console.log(errors);

      const errorList = errors.map((error, index) => `${index + 1}. ${error.path}: ${error.stack}\n\n`);

      // Write comment back with errors for
      await octokit.rest.issues.createComment({
        owner,
        repo,
        issue_number: process.env.PR_NUMBER,
        body:
          'Thank you for your contribution to Serverless Land! 🚀 \n\n' +
          '⚠️ Your `example-pattern.json` is missing some key fields, please review below and address any errors you have \n\n' +
          `${errorList.toString()} \n\n` +
          `Once fixed and pushed back into the repo. We can review your pattern. \n\n`
      });

      throw new Error('Failed to validate pattern, errors found');
    }

    // Everything OK....
  } catch (error) {
    console.error(error);
    throw Error('Failed to process the example-pattern.json file.');
  }
};

main();
