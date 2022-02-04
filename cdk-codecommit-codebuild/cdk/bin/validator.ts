import cdk = require("@aws-cdk/core");
import { PipelineStack } from "../lib/pipeline";

const app = new cdk.App();

const staticSite = new PipelineStack(app, "codebuildOnPR", {
    repositoryName: "test-pattern",
});

// example of adding a tag - please refer to AWS best practices for ideal usage
cdk.Tags.of(staticSite).add("Project", "codecommit-codebuild-pipeline");

app.synth();
