import { Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import { WorkflowCatalog } from "./workflow-catalog";

export class WorkflowCatalogStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new WorkflowCatalog(this, "WorkflowCatalog");
  }
}
