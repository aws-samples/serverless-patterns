const fs = require('fs');
const path = require('path');
const Validator = require('jsonschema').Validator;
const v = new Validator();

const supportedLanguages = ['TypeScript', 'Node.js', 'Python', 'Java', '.Net', 'C#', 'Go', 'Rust'];
const supportedFrameworks = ['CDK', 'SAM', 'Terraform', 'Serverless Framework'];

console.log(process.env)

const buildErrors = (validationErrors) => {
  return validationErrors.map((error) => {
    return {
      path: error.property,
      message: error.message,
      data: error.instance,
      stack: error.stack,
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
    // Errors write them back to the comment on GitHub....

    const errors = buildErrors(result.errors);
    console.log('We have errors', errors);
  } else {
    console.log('All valid!');

    // Verify that the GitHub URL is correct and can be loaded.
  }

  // run against some schema validation stuff.

  //   console.log(parsedJSON);
} catch (error) {
  console.error(error);
  throw Error('Failed to process the example-pattern.json file.');
}

// Validate the path to the URL is correct too...
