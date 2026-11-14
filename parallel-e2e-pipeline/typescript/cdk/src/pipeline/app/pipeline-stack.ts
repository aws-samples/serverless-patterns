import { Stack, StackProps, App } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as codecommit from "aws-cdk-lib/aws-codecommit";
import * as codepipeline from "aws-cdk-lib/aws-codepipeline";
import * as codepipeline_actions from "aws-cdk-lib/aws-codepipeline-actions"

import { PipelineRole, E2ECodeBuildRole } from "./constructs/roles";
import { getEndToEndTestsActions } from "./constructs/end-to-end-tests";


export interface PipelineStackProps extends StackProps {
  readonly prefix: string;
};

export class PipelineStack extends Stack {
  constructor(app: App, id: string, props: PipelineStackProps) {
    super(app, id, props);

    const repository = codecommit.Repository.fromRepositoryName(
      this, 
      "ImportedRepo", 
      "serverless-patterns"  // TODO: Replace this with the name of your AWS CodeCommit repository
    );

    const sourceOutput = new codepipeline.Artifact();

    const e2eBuildRole = new E2ECodeBuildRole(this, "E2EBuildRole").role;
    const installCommands = [
      `echo "Run install commands"`,
      "npm install -g typescript"
    ];
    const stages = [
      {
        stageName: "Source",
        actions: [
          new codepipeline_actions.CodeCommitSourceAction({
            actionName: "CodeCommit_Source",
            repository: repository,
            branch: "mainline", // TODO: Replace this with the name of your working branch
            output: sourceOutput
          })
        ]
      },
      /**
       * TODO (Optional for deploying pattern): Add a deployment stage for your application. The following
       * "End_to_End_Tests" stage would run against this application.
       */
      {
        stageName: "End_to_End_Tests",
        actions: [
          ...getEndToEndTestsActions(
            this,
            sourceOutput,
            e2eBuildRole,
            installCommands
          )
        ]
      }
    ];

    const deployedPipelineRole = new PipelineRole(
      this, 
      "PipelineRole", 
      { roles: [e2eBuildRole.roleArn] }
    ).role;
    const deployedPipeline = new codepipeline.Pipeline(
      this,
      `${props.prefix}Pipeline`,
      {
        pipelineName: id,
        stages: stages,
        role: deployedPipelineRole
      }
    );
  }
};
