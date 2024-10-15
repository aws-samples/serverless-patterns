#!/usr/bin/env python3
import os

import aws_cdk as cdk

from alb_path_based_session_stickiness.alb_path_based_session_stickiness_stack import (
    AlbPathBasedSessionStickinessStack,
)


app = cdk.App()
AlbPathBasedSessionStickinessStack(app, "AlbPathBasedSessionStickinessStack")
app.synth()
