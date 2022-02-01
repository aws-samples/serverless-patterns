import * as targets from "@aws-cdk/aws-events-targets";
import * as iam from "@aws-cdk/aws-iam";
import * as codebuild from '@aws-cdk/aws-codebuild';
import * as codecommit from '@aws-cdk/aws-codecommit';
import * as cdk from "@aws-cdk/core";
import * as events from "@aws-cdk/aws-events";
import * as nodeJSlambda from "@aws-cdk/aws-lambda-nodejs";
import * as lambda from "@aws-cdk/aws-lambda";
import * as path from "path";

export interface PipelineProps extends cdk.StackProps {
    repositoryName: string
}

/**
 * Static site infrastructure, which deploys site content to an S3 bucket.
 *
 * The site redirects from HTTP to HTTPS, using a CloudFront distribution,
 * Route53 alias record, and ACM certificate.
 */
export class PipelineStack extends cdk.Stack {
    constructor(scope: cdk.Construct, name: string, props: PipelineProps) {
        super(scope, name, props);
        const {repositoryName} = props

        // Get the CodeCommit Repository reference from name.
        const repository = codecommit.Repository.fromRepositoryName(this, repositoryName, repositoryName)

        // Create CodeBuild project, you can configure your project as needed
        const codeBuildProject = new codebuild.Project(this, 'ExampleCodeBuild', {
            source: codebuild.Source.codeCommit({repository}),
            buildSpec: codebuild.BuildSpec.fromSourceFilename('buildspec.yml'),
        })

        repository.onPullRequestStateChange('onPRChanged', {
            // We don't want to have the CodeBuild running on closed Branches
            eventPattern: {
                detail: {
                    'pullRequestStatus': ['Open']
                }
            },
            target: new targets.CodeBuildProject(codeBuildProject, {
                event: events.RuleTargetInput.fromObject({
                    // This is to link the commit on the PR to the codebuild Project
                    sourceVersion: events.EventField.fromPath('$.detail.sourceReference'),
                    // Mapping to be able to post a comment to a PR.
                    // That way we don't use a temporary database for that.
                    environmentVariablesOverride: [
                        {
                            "name": "pullRequestID",
                            "type": "PLAINTEXT",
                            "value": events.EventField.fromPath('$.detail.pullRequestId')
                        },
                        {
                            "name": "repositoryName",
                            "type": "PLAINTEXT",
                            "value": repositoryName
                        },
                        {
                            "name": "sourceCommit",
                            "type": "PLAINTEXT",
                            "value": events.EventField.fromPath('$.detail.sourceCommit')
                        },
                        {
                            "name": "destinationCommit",
                            "type": "PLAINTEXT",
                            "value": events.EventField.fromPath('$.detail.destinationCommit')
                        }
                    ],
                }),
            })
        })

        // Lambda That will post the comment.
        const commentLambda = new nodeJSlambda.NodejsFunction(this, 'commentOnPRWithBuildStatus', {
            runtime: lambda.Runtime.NODEJS_14_X,
            handler: 'handler',
            bundling: {
                externalModules: ['aws-sdk', '@aws-sdk/client-codecommit']
            },
            entry: path.join(__dirname, `/../src/commentLambda.ts`),
            initialPolicy: [    new iam.PolicyStatement({
                actions: ['codecommit:PostCommentForPullRequest'],
                resources: [repository.repositoryArn],
            })],
        })

        const codeBuildHookOptions = {
            target: new targets.LambdaFunction(commentLambda, {
                event: events.RuleTargetInput.fromEventPath('$.detail')
            })
        }

        // Trigger Lambda on both Success and Failed
        codeBuildProject.onBuildSucceeded('onBuildSucceeded', codeBuildHookOptions)
        codeBuildProject.onBuildFailed('onBuildFailed', codeBuildHookOptions)

    }
}
