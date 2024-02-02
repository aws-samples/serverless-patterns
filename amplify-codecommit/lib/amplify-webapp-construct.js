const {Construct} = require('constructs');
const codecommit = require('aws-cdk-lib/aws-codecommit');
const amplify = require('aws-cdk-lib/aws-amplify');
const iam = require('aws-cdk-lib/aws-iam');
const cr = require('aws-cdk-lib/custom-resources');
const fs = require('fs');
const cdk = require('aws-cdk-lib');
const { CfnOutput } = require('aws-cdk-lib');

class AmplifyWebAppConstruct extends Construct {
    constructor(scope, id, props) {
        super(scope, id);

        // Create a new CodeCommit Repository from a local repository or folder 
        const repo = new codecommit.Repository(this, 'Repository', {
            repositoryName: 'webapp-repository',
            code: codecommit.Code.fromDirectory('local-webapp-code'), // required property
        });

        // Create an IAM Role that gives Amplify permission to pull from CodeCommit
        const amplifyRole = new iam.Role(this, 'AmplifyRole', {
            assumedBy: new iam.ServicePrincipal('amplify.amazonaws.com'),
            inlinePolicies: {
                'CodeCommit': new iam.PolicyDocument({
                    statements: [
                        new iam.PolicyStatement({
                            actions: ['codecommit:GitPull'],
                            effect: iam.Effect.ALLOW,
                            resources: ['*'],
                        })
                    ]
                })
            }
        });

        //Optional: set backend endpoint URL. This is static for the example, but can also by dynamically retrieved
        const api_url = 'SAMPLE_BACKEND_API_URL'

        // Create the Amplify web app. Set repository as the code commit repo. Optional: Pass backend endpoint URL to the front end code via Amplify environment variables
        const cfnApp = new amplify.CfnApp(this, 'AmplifyApp', {
            name: 'codecommit-amplify-webApp',
            repository: repo.repositoryCloneUrlHttp,
            platform: 'WEB',
            iamServiceRole: amplifyRole.roleArn,
            buildSpec: readYamlAsString('./buildspec.yml'),
            environmentVariables: [{
                name: 'API_URL',
                value: api_url,
              }],
        });

        // Create a new Amplify Branch
        const cfnBranch = new amplify.CfnBranch(this, 'AmplifyBranch', {
            appId: cfnApp.attrAppId,
            branchName: 'main',
            stage: 'PRODUCTION',
            enableAutoBuild: true
        });

        // Create an IAM role for a custom resource, Amplify Job
        const customResourceRole = new iam.Role(this, 'CustomResourceRole', {
            assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
        });
          
        // Give the custom resource IAM role permissions to Amplify
        customResourceRole.addToPolicy(new iam.PolicyStatement({
            actions: ['amplify:*'],
            resources: ['*'], // Adjust the ARN accordingly
        }));

        // Create a Customer Resource that creates an Amplify job. This job will pull from the Amplify branch created above, and build the web application.
        new cr.AwsCustomResource(this, 'amplifyJob', {
            onCreate: {
                service: 'Amplify',
                action: 'startJob',
                parameters: { 
                    appId: cfnApp.attrAppId,
                    branchName: 'main',
                    jobType: 'RELEASE'
                },
                physicalResourceId: 'amplify-deployment-cust-res', // Replace with a unique ID
            },
            role: customResourceRole
        });

        //Optional: Output web app url for latter use
        new CfnOutput(this, 'WebApp', {
            value: `https://main.${cfnApp.attrDefaultDomain}`,
            exportName: 'WebApp',
            });
        
        new CfnOutput(this, 'AppID', {
            value: cfnApp.attrAppId,
            exportName: 'AppID',
            });

    }
}

// Optional helper function. Reads yaml buildspec file from local repo, returns buildspec contents as a string for use in cfnApp
function readYamlAsString(filePath) {
    try {
      const yamlContent = fs.readFileSync(filePath, 'utf-8');
      return yamlContent;
    } catch (error) {
      console.error('Error reading YAML file:', error);
      return null;
    }
  }

module.exports = {AmplifyWebAppConstruct};