import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { CodePipeline, ShellStep, CodePipelineSource } from "aws-cdk-lib/pipelines";

import { config } from '../config';

export class DemoPipeline extends Stack {

    public readonly pipeline: CodePipeline;

    constructor(scope: Construct, id: string, props: StackProps) {
        super(scope, id, props);
        const repoName = Repository.fromRepositoryName(this, 'testRepo', config.repositoryName);
        const demoPipeline = new CodePipeline(this, 'DemoPipeline-NonProd', {
            pipelineName: 'DemoPipeline-NonProd',
            crossAccountKeys: false,
            publishAssetsInParallel: false,
            cliVersion: config.CDK_CLI_VERSION,
            synth: new ShellStep('synth', {
                input: CodePipelineSource.codeCommit(repoName, config.branchName),
                installCommands: [
                    `npm i -g aws-cdk@${config.CDK_CLI_VERSION}`
                ],
                commands: [
                    'npm ci',
                    'npm run build',
                    'npx cdk synth'
                ]
            }),
        });
        demoPipeline.buildPipeline();
        this.pipeline = demoPipeline;
    }

}