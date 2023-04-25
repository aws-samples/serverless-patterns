#!/usr/bin/env python3

from aws_cdk import App as app, Aws


from stack import (
    EventbridgeEventsReplayStack,
)

from simple_lower_env_stack import SimpleLowerEnvironmentStack


app = app()
PROD_ACCOUNT_ID = app.node.try_get_context("prodAccountId")
CROSS_ACCOUNT_EVENTBUS_ARN = app.node.try_get_context("crossAccountEventBusArn")
EventbridgeEventsReplayStack(
    app, "EventbridgeEventsReplayStack", CROSS_ACCOUNT_EVENTBUS_ARN
)


SimpleLowerEnvironmentStack(app, "SimpleLowerEnvironmentStack", PROD_ACCOUNT_ID)
app.synth()
