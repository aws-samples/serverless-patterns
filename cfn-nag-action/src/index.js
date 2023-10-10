const cfnNag = require('./cfg-nag');
const filesToCheck = ['template.yml', 'template.yaml'];

const args = process.argv.slice(2);

const newFiles = args[0] ? args[0].split(',') : [];
const modifiedFiles = args[1] ? args[1].split(',') : [];

const getValidFilesForCfnNag = (files) => files.filter((file) => filesToCheck.some((validFile) => file.includes(validFile)));

const filesToVerify = [...getValidFilesForCfnNag(newFiles), ...getValidFilesForCfnNag(modifiedFiles)];

if (!filesToVerify.length) {
  console.log('No new or modified files found to verify');
  process.exit(0);
}

const resultsFromAllPatterns = filesToVerify.reduce((acc, pathToTemplate) => {
  console.log(`Processing ${pathToTemplate}...`);
  const result = cfnNag(pathToTemplate);

  // Just get the errors from the response (ignore warnings)
  const errors = result.reduce((errors, response) => {
    const {
      filename,
      file_results: { failure_count, violations },
    } = response;

    // only failures, ignore warnings.
    if (failure_count === 0) return errors;

    const violationsWithErrors = violations.filter((violation) => violation.type === 'FAIL');

    return errors.concat({ filename, violationsWithErrors });
  }, []);

  return acc.concat(errors);
}, []);

// We have errors with the templates
if(resultsFromAllPatterns.length > 0){
    console.log('Errors found with new or modified templates, please review')
    console.log(JSON.stringify(resultsFromAllPatterns, null, 4));
    process.exit(1);
}

