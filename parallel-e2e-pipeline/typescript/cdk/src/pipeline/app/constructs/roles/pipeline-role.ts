import {
  PolicyDocument,
  PolicyStatement,
  Effect,
  Role,
  ServicePrincipal
} from "aws-cdk-lib/aws-iam";
import { Construct } from 'constructs';


interface PipelineRoleProps { 
  roles: string[]
}

export class PipelineRole extends Construct {
  readonly role: Role;
  readonly policy: PolicyDocument;

  public constructor(parent: Construct, id: string, props: PipelineRoleProps) {
    super(parent, id);
    this.policy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          actions: ["sts:*"],
          effect: Effect.ALLOW,
          resources: [...props.roles]
        }),
        new PolicyStatement({
          actions: [
            "codecommit:GetBranch",
            "codecommit:GetCommit",
            "codecommit:UploadArchive",
            "codecommit:GetUploadArchiveStatus",
            "codecommit:CancelUploadArchive",
            "codebuild:BatchGetBuilds",
            "codebuild:StartBuild",
            "codedeploy:CreateDeployment",
            "codedeploy:GetApplicationRevision",
            "codedeploy:GetDeployment",
            "codedeploy:GetDeploymentConfig",
            "codedeploy:RegisterApplicationRevision"
          ],
          effect: Effect.ALLOW,
          resources: ["*"]
        })
      ]
    });
    this.role = new Role(this, "PipelineRole", {
      assumedBy: new ServicePrincipal("codepipeline.amazonaws.com"),
      inlinePolicies: { base_policy: this.policy }
    });
  };
};
