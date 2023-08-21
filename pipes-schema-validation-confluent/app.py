#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.kafka_confluent_validate import (
    KafkaConfluentValidateStack,
)

app = cdk.App()

KafkaConfluentValidateStack(app, "kafka-confluent-validate")

app.synth()
