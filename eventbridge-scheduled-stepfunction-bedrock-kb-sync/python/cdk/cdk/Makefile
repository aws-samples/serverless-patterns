#!/usr/bin/env make

SHELL := /bin/bash
.DEFAULT_GOAL := help

# TODO add docker-compose cmd to Makefile

###########################
# VARIABLES
###########################

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

# select stage with command make -e STAGE=<stage> <target>
# dev is default, available: dev, int, prod
PLATFORM_STAGE := dev

###########################
# TARGETS
###########################

.PHONY: help
help:  ## help target to show available commands with information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: synth
synth:  ## cdk synth
	npx cdk synth -o cdk.out

#################
#
# Run the following lines for bootstrapping your venv
# afterwards you must do a source .venv/bin/activate
#
##################
.PHONY: bootstrap-venv
bootstrap-venv: ## setup venv if needed, this is not needed when using the make zsh (docker environment)
	${mkfile_dir}scripts/bootstrap.sh 

.PHONY: bootstrap
bootstrap:  ## bootstrap, this is not needed when using the make zsh (docker environment)
	python3 -m pip install -r requirements.txt
	npm install

.PHONY: test
test:  ## run tests
	pytest -v tests

.PHONY: lint
lint:  ## run linter tools
	pylint --reports=y src || pylint-exit $? -efail

.PHONY: cfnlint
cfnlint:  ## run linter tools
	cfn-lint --reports=y src || pylint-exit $? -efail



.PHONY: clear-tmp-files
clear-tmp-files:  ## clear all tmp files
	rm -rf ./cdk.out
	find ./ -type d -name __pycache__ -exec rm -rf {} +
	find ./ -type d -name .pytest_cache -exec rm -rf {} +

##################
#Coverage Commands - 
##################
.PHONY: coverage
coverage: ## Display the covde coverage results
	pytest --cov=src  tests/

.PHONY: coverage-report
coverage-report: ## Build a code coverage report using coverage.py
	pytest --cov-report xml:cov.xml --cov=src tests/
# coverage run --source=src -m pytest -v src/
# coverage report


.PHONY: git-secrets
git-secrets:  ## deploy git-secrets
	$(eval testgit := $(shell which git-secrets))
	@echo $(testgit)
	@if test "$(testgit)" = ""; then \
		echo "Please install git secrets on your local machine, see information in README.md"; \
	else \
		echo "Deploying git-secrets in repo"; \
		git secrets --install -f; \
		git secrets --register-aws; \
	fi \

.PHONY: git-secrets-scan
git-secrets-scan:  ## run git secrets scan
	git secrets --scan

.PHONY: pre-commit-autoupdate
pre-commit-autoupdate:
	-pre-commit autoupdate
