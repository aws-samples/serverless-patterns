#!/bin/sh
# Entry point for the scanner MicroVM image.
# Starts the lifecycle hook listener (port 9000) and the scanner app (port 8080).
set -e

python3 /app/hooks.py &
exec python3 /app/app.py
