#!/usr/bin/env python3
import os

import aws_cdk as cdk

from file_processing_workflow_cdk.file_processing_workflow_cdk_stack import FileProcessingWorkflowCdkStack


app = cdk.App()
FileProcessingWorkflowCdkStack(app, "FileProcessingWorkflowCdkStack")

app.synth()

