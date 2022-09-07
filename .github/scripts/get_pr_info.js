module.exports = async ({ github, context, core }) => {
  const prNumber = process.env.PR_NUMBER;

  if (prNumber === '') {
    core.setFailed(`No PR number was passed. Aborting`);
  }

  try {
    const {
      data: { head, base, ...rest },
    } = await github.rest.pulls.get({
      owner: context.repo.owner,
      repo: context.repo.repo,
      pull_number: prNumber,
    });

    const files = github.rest.pulls.listFiles({
      owner: context.repo.owner,
      repo: context.repo.repo,
      pull_number: prNumber
    })


    console.log("data", files);
    
    core.setOutput('headRef', head.ref);
    core.setOutput('headSHA', head.sha);
    core.setOutput('baseRef', base.ref);
    core.setOutput('baseSHA', base.sha);
  } catch (error) {
    core.setFailed(`Unable to retrieve info from PR number ${prNumber}.\n\n Error details: ${error}`);
    throw error;
  }
};
