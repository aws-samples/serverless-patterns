import { Role } from "aws-cdk-lib/aws-iam";
import { Construct } from 'constructs';
import { Artifact } from "aws-cdk-lib/aws-codepipeline";
import { 
  ComputeType, 
  PipelineProject, 
  BuildSpec, 
  LinuxBuildImage 
} from "aws-cdk-lib/aws-codebuild";
import { CodeBuildAction } from "aws-cdk-lib/aws-codepipeline-actions";


export const getEndToEndTestsActions = (
  scope: Construct,
  stageInput: Artifact,
  codeBuildRole: Role,
  installCommands: string[],
): CodeBuildAction[] => {

  // Names of the group of e2e tests to run. These values will be used in cdk/cloudformation ids.
  const groupOne = "E2E_Tests_Group_One";
  const groupTwo = "E2E_Tests_Group_Two";

  const buildCommands = ["cd parallel-e2e-pipeline-cdk/src/mock-e2e-tests"];

  const actions: CodeBuildAction[] = [
    new CodeBuildAction({
      actionName: groupOne,
      project: getEndToEndTestProject(
        scope,
        groupOne,
        codeBuildRole,
        ComputeType.SMALL,
        installCommands,
        // The below cli command specifies what to run on this CodeBuild server.
        [
          ...buildCommands, 
          `echo "Run additional commands for ${groupOne}"`,
          "tsc mock-e2e-1.ts",
          "node mock-e2e-1.ts"
        ]
      ),
      input: stageInput,
      outputs: [new Artifact(`${groupOne}_Ouput`)]
    }),
    new CodeBuildAction({
      actionName: groupTwo,
      project: getEndToEndTestProject(
        scope,
        groupTwo,
        codeBuildRole,
        ComputeType.SMALL,
        installCommands,
        // The below cli command specifies what to run on this CodeBuild server.
        [
          ...buildCommands, 
          `echo "Run additional commands for ${groupTwo}"`,
          "tsc mock-e2e-1.ts",
          "node mock-e2e-2.ts"
        ]
      ),
      input: stageInput,
      outputs: [new Artifact(`${groupTwo}_Ouput`)]
    }),
  ];
  return actions;
}

const getEndToEndTestProject = (
  scope: Construct,
  testGroupName: string,
  codeBuildRole: Role,
  computeType: ComputeType,
  installCommands: string[],
  buildCommands: string[],
  preBuildCommands?: string[],
  postBuildCommands?: string[],
): PipelineProject => {
  return new PipelineProject(scope, testGroupName, {
    role: codeBuildRole,
    buildSpec: BuildSpec.fromObject({
      version: '0.2',
      phases: {
        install: {
          commands: installCommands
        },
        pre_build: {
          commands: preBuildCommands ?? []
        },
        build: {
          commands: buildCommands
        },
        post_build: {
          commands: postBuildCommands ?? []
        }
      }
    }),
    environment: {
      buildImage: LinuxBuildImage.STANDARD_5_0,
      computeType: computeType
    }
  });
}
