#!/usr/bin/env python3

import aws_cdk as cdk

# from aurora_serverless_ingestion.aurora_serverless_ingestion_stack import AuroraServerlessIngestionStack

# from aws_cdk import core
from aurora_serverless_ingestion.aurora_serverless_ingestion_stack import AuroraServerlessIngestionStack

app = cdk.App()
AuroraServerlessIngestionStack(app, "aurora-serverless-ingestion")

app.synth()
