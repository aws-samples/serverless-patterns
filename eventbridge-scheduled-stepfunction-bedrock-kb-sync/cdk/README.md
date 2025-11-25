
# Prerequisites

### Required Tools
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [AWS CLI v2](https://aws.amazon.com/cli/)
- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js 14+](https://nodejs.org/)

### AWS Configuration
1. [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

```
aws configure
```

## Setup local developer environment and dependencies:

```
make bootstrap-venv
source .venv/bin/activate
```

## Description

This project contains the Bedrock KB Sync pattern

## Developer Guide (Build/Test/Deploy)

The python code from both the platform_common test scaffolding package are needed in the path
for the following tools to work effectively:

- **pylance** - for the autocompletion, syntax highlighting, type hinting (language server).
- **pytest** - for the local unit testing.
- **pylint** - for coding standards/conventions.

Development Environment
cdk synth
cdk deploy --all


To achieve this any project which depends on the common unit testing layer should have a `pyproject.toml` file in it's root directory
with the following pytest directive:

```
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ".venv/lib/python3.14/site-packages"]
`

## Architecture

Detailed documentation is available in the docs/ directory:

    API Documentation
    Infrastructure Design
    Security Considerations
    Deployment Guide

## Deployment Process

1. Development:
   - Developers can create a feature branch 
   - Create PR from `feat/` to `dev`
   - PR requires review and approval
   - All unit tests must pass
   - After merge, automatic deployment to production
   - All tests and validations must pass

2. Production:
   - Create PR from `dev` to `main`
   - PR requires review and approval
   - All tests must pass
   - After merge, automatic deployment to production

## License
#todo
