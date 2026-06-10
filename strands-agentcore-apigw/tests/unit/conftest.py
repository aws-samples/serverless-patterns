"""Shared fixtures for CloudFormation template unit tests."""

import os
import pytest
import yaml


TEMPLATE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "infrastructure", "template.yaml"
)


class CfnLoader(yaml.SafeLoader):
    """YAML loader that handles CloudFormation intrinsic function tags."""
    pass


def _multi_constructor(loader, tag_suffix, node):
    """Handle multi-value CloudFormation tags like !Sub, !If, etc."""
    if isinstance(node, yaml.ScalarNode):
        return {tag_suffix: loader.construct_scalar(node)}
    elif isinstance(node, yaml.SequenceNode):
        return {tag_suffix: loader.construct_sequence(node, deep=True)}
    elif isinstance(node, yaml.MappingNode):
        return {tag_suffix: loader.construct_mapping(node, deep=True)}


# Register all CloudFormation intrinsic functions
_CFN_TAGS = [
    "Ref", "Sub", "If", "Not", "Equals", "GetAtt", "Join",
    "Select", "Split", "FindInMap", "ImportValue", "Condition",
    "And", "Or", "Base64", "Cidr", "GetAZs", "Transform",
]

for tag in _CFN_TAGS:
    CfnLoader.add_constructor(
        f"!{tag}",
        lambda loader, node, t=tag: _multi_constructor(loader, t, node),
    )


@pytest.fixture(scope="session")
def template():
    """Load and parse the CloudFormation template once for all tests."""
    with open(TEMPLATE_PATH, "r") as f:
        return yaml.load(f, Loader=CfnLoader)


@pytest.fixture(scope="session")
def resources(template):
    """Return the Resources section of the template."""
    return template["Resources"]


@pytest.fixture(scope="session")
def parameters(template):
    """Return the Parameters section of the template."""
    return template["Parameters"]


@pytest.fixture(scope="session")
def outputs(template):
    """Return the Outputs section of the template."""
    return template["Outputs"]
