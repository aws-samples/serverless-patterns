#!/bin/bash
# Startup script for code-server + lifecycle hooks inside Lambda MicroVM.
#
# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Start lifecycle hooks handler in the background (port 9000)
python3 /opt/hooks/app.py &

# Start code-server in the foreground (port 8080)
exec code-server --auth none --bind-addr 0.0.0.0:8080 /home/project
