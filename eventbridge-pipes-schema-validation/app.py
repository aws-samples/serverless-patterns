#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.kafka_glue_validate import KafkaGlueValidateStack

app = cdk.App()

KafkaGlueValidateStack (app, "kafka-glue-validate")

app.synth()
