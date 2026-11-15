#!/bin/bash

# Define the prefix
PREFIX="api-key-"

# Add a dry run flag
DRY_RUN=false

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --dry-run) DRY_RUN=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# List secrets with the prefix and store them in an array
secrets=($(aws secretsmanager list-secrets --query 'SecretList[?starts_with(Name, `'"$PREFIX"'`)].Name' --output text))

# Loop through each secret
for secret in "${secrets[@]}"; do
    if $DRY_RUN; then
        echo "Would delete secret: $secret"
    else
        aws secretsmanager delete-secret --secret-id "$secret" --recovery-window-in-days 7 --no-cli-pager
        echo "Deleted secret: $secret"
    fi
done

if $DRY_RUN; then
    echo "Dry run completed. No secrets were actually deleted."
fi
