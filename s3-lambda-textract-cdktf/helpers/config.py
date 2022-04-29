"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import json
from os import path
import jsonschema.exceptions
from jsonschema import validate


def getDeploymentConfig(file: str) -> dict:
    """
    Load and validate the deployment configuration json file

    :param file: configuration json file
    :return: configuration as dict
    """
    if not path.exists(file):
        raise FileNotFoundError("Missing config.json file")
    try:
        with open(file, "r") as f:
            config = json.load(f)
    except json.JSONDecodeError as err:
        raise IOError(err)

    schema = _get_schema()

    try:
        validate(instance=config, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        raise SyntaxError(err)

    return config


def _get_schema():
    """
    The validation Schema provider

    :return: the schema validation as a dict
    """
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Config",
        "description": "Stack deployment configuration",
        "type": "object",
        "properties": {
            "region": {"type": "string"},
            "tags": {
                "type": "object",
                "maxItems": 10
            },
            "layers": {
                "type": "object",
                "properties": {
                    "pillow": {
                        "type": "object",
                        "properties": {
                            "always_refresh": {"type": "boolean"},
                            "url": {"type": "string"},
                            "hash": {"type": "string"}
                        }
                    }
                }
            }
        },
        "required": [
            "region"
        ],
        "additionalProperties": False
    }
