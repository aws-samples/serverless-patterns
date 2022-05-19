const { execSync } = require('child_process');

const path = '/usr/src/app';

module.exports = (pathToTemplate) => {
  try {
    console.log(`Verifying ${pathToTemplate}`);
    execSync(`cfn_nag ${path}/${pathToTemplate} --output-format json`);
    return [];
  } catch (error) {
    const errorFromCFNNAG = error.output[1].toString();
    const response = JSON.parse(errorFromCFNNAG);
    return response;
  }
};
