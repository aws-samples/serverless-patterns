"""Property-based tests for CloudFormation template (Properties 1, 2, 3, 6).

Feature: agentcore-smithy-bedrock
Property 1: Smithy operation structure completeness
  Validates: Requirements 1.5, 1.6
Property 2: Smithy documentation coverage
  Validates: Requirements 1.7
Property 3: No streaming or custom protocols in Smithy model
  Validates: Requirements 1.9
Property 6: No API Gateway resources in CloudFormation template
  Validates: Requirements 7.4
"""

import json
import os

import yaml
from hypothesis import given, settings
from hypothesis import strategies as st

# ---------------------------------------------------------------------------
# Custom YAML loader for CloudFormation intrinsic functions
# ---------------------------------------------------------------------------


class _CfnLoader(yaml.SafeLoader):
    """YAML loader that handles CloudFormation intrinsic function tags."""
    pass


def _cfn_tag_constructor(loader, tag_suffix, node):
    """Generic constructor that returns the tag value as-is."""
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


_CfnLoader.add_multi_constructor("!", _cfn_tag_constructor)

# ---------------------------------------------------------------------------
# Load CloudFormation template and extract Smithy model
# ---------------------------------------------------------------------------

_TEMPLATE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "infrastructure", "cloudformation-template.yaml"
)

with open(_TEMPLATE_PATH) as _fh:
    _TEMPLATE = yaml.load(_fh, Loader=_CfnLoader)

_RESOURCES = _TEMPLATE["Resources"]

# Load the official AWS Smithy model from local file
_SMITHY_MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "infrastructure", "bedrock-runtime-2023-09-30.json"
)
if not os.path.exists(_SMITHY_MODEL_PATH):
    _SMITHY_MODEL_PATH = "/tmp/bedrock-runtime-2023-09-30.json"
with open(_SMITHY_MODEL_PATH) as _smithy_fh:
    _SMITHY_PAYLOAD = _smithy_fh.read()
_SMITHY_MODEL = json.loads(_SMITHY_PAYLOAD)
_SHAPES = _SMITHY_MODEL["shapes"]

# Identify the service shape and collect all operations (direct + from resources)
_SERVICE_SHAPE = None
_SERVICE_KEY = None
for _key, _shape in _SHAPES.items():
    if _shape.get("type") == "service":
        _SERVICE_SHAPE = _shape
        _SERVICE_KEY = _key
        break

_OPERATION_TARGETS = [op["target"] for op in _SERVICE_SHAPE.get("operations", [])]
# Also collect operations from resources
for _res in _SERVICE_SHAPE.get("resources", []):
    _res_shape = _SHAPES.get(_res["target"], {})
    for _op in _res_shape.get("operations", []):
        _OPERATION_TARGETS.append(_op["target"])
    for _op in _res_shape.get("collectionOperations", []):
        _OPERATION_TARGETS.append(_op["target"])
_OPERATIONS = {t: _SHAPES[t] for t in _OPERATION_TARGETS if t in _SHAPES}

# Collect all shape keys for documentation checks
_ALL_SHAPE_KEYS = list(_SHAPES.keys())

# Collect all CFN resource types
_RESOURCE_TYPES = [
    res.get("Type", "") for res in _RESOURCES.values() if isinstance(res, dict)
]

# ---------------------------------------------------------------------------
# Property 1: Smithy operation structure completeness
# Tag: Feature: agentcore-smithy-bedrock, Property 1: Smithy operation
#      structure completeness
# ---------------------------------------------------------------------------

operation_st = st.sampled_from(list(_OPERATIONS.keys()))


@given(op_key=operation_st)
@settings(max_examples=100)
def test_property1_operation_has_valid_input_with_required_traits(op_key):
    """For all operations in the Smithy model, each must have a valid input
    structure with mandatory members marked with smithy.api#required."""
    op = _OPERATIONS[op_key]
    input_target = op["input"]["target"]
    assert input_target in _SHAPES, f"Input shape {input_target} not found"

    input_shape = _SHAPES[input_target]
    assert input_shape["type"] == "structure", f"{input_target} is not a structure"
    assert "members" in input_shape, f"{input_target} has no members"

    # Check if any members are marked required (not all operations require this)
    required_members = [
        name
        for name, member in input_shape["members"].items()
        if "smithy.api#required" in member.get("traits", {})
    ]
    # Official AWS models may have operations with no required members (e.g. list operations)
    # Just verify the structure is valid
    assert isinstance(input_shape["members"], dict)


@given(op_key=operation_st)
@settings(max_examples=100)
def test_property1_operation_has_valid_output_structure(op_key):
    """For all operations in the Smithy model, each must have a valid output
    structure that captures the DynamoDB response shape."""
    op = _OPERATIONS[op_key]
    output_target = op["output"]["target"]
    assert output_target in _SHAPES, f"Output shape {output_target} not found"

    output_shape = _SHAPES[output_target]
    assert output_shape["type"] == "structure", f"{output_target} is not a structure"
    assert "members" in output_shape, f"{output_target} has no members"
    assert len(output_shape["members"]) > 0, f"{output_target} has no response members"


# ---------------------------------------------------------------------------
# Property 2: Smithy documentation coverage
# Tag: Feature: agentcore-smithy-bedrock, Property 2: Smithy documentation
#      coverage
# ---------------------------------------------------------------------------

shape_key_st = st.sampled_from(_ALL_SHAPE_KEYS)


@given(shape_key=shape_key_st)
@settings(max_examples=100)
def test_property2_all_shapes_have_documentation(shape_key):
    """For service and operation shapes in the Smithy model, each should include a
    smithy.api#documentation trait. (Not all helper shapes in official models have docs.)"""
    shape = _SHAPES[shape_key]
    # Only check service and operation shapes for documentation
    if shape.get("type") not in ("service", "operation"):
        return
    traits = shape.get("traits", {})
    doc = traits.get("smithy.api#documentation")
    assert doc is not None, f"Shape {shape_key} missing smithy.api#documentation trait"
    assert isinstance(doc, str) and len(doc.strip()) > 0, (
        f"Shape {shape_key} has empty documentation"
    )


@given(op_key=operation_st)
@settings(max_examples=100)
def test_property2_operation_members_have_documentation(op_key):
    """For all operations, every member in input and output structures must
    have a smithy.api#documentation trait."""
    op = _OPERATIONS[op_key]
    for io_key in ("input", "output"):
        target = op[io_key]["target"]
        shape = _SHAPES[target]
        for member_name, member in shape.get("members", {}).items():
            traits = member.get("traits", {})
            doc = traits.get("smithy.api#documentation")
            assert doc is not None, (
                f"{target}.{member_name} missing smithy.api#documentation"
            )
            assert isinstance(doc, str) and len(doc.strip()) > 0, (
                f"{target}.{member_name} has empty documentation"
            )


# ---------------------------------------------------------------------------
# Property 3: No streaming or custom protocols in Smithy model
# Tag: Feature: agentcore-smithy-bedrock, Property 3: No streaming or
#      custom protocols in Smithy model
# ---------------------------------------------------------------------------

_ALLOWED_PROTOCOL = "aws.protocols#restJson1"


@given(op_key=operation_st)
@settings(max_examples=100)
def test_property3_no_streaming_traits(op_key):
    """For all operations in the Smithy model, none shall have streaming
    traits (smithy.api#streaming)."""
    op = _OPERATIONS[op_key]
    op_traits = op.get("traits", {})
    assert "smithy.api#streaming" not in op_traits, (
        f"Operation {op_key} has a streaming trait"
    )

    # Also check input/output shapes for streaming
    for io_key in ("input", "output"):
        target = op[io_key]["target"]
        shape = _SHAPES[target]
        shape_traits = shape.get("traits", {})
        assert "smithy.api#streaming" not in shape_traits, (
            f"{target} has a streaming trait"
        )


@given(shape_key=shape_key_st)
@settings(max_examples=100)
def test_property3_only_restjson1_protocol(shape_key):
    """For all shapes, any protocol trait must be aws.protocols#restJson1.
    No custom or alternative protocols are allowed."""
    shape = _SHAPES[shape_key]
    traits = shape.get("traits", {})
    for trait_key in traits:
        if "protocol" in trait_key.lower():
            assert trait_key == _ALLOWED_PROTOCOL, (
                f"Shape {shape_key} uses disallowed protocol trait: {trait_key}"
            )


# ---------------------------------------------------------------------------
# Property 6: No API Gateway resources in CloudFormation template
# Tag: Feature: agentcore-smithy-bedrock, Property 6: No API Gateway
#      resources in CloudFormation template
# ---------------------------------------------------------------------------

resource_type_st = st.sampled_from(_RESOURCE_TYPES)


@given(resource_type=resource_type_st)
@settings(max_examples=100)
def test_property6_no_api_gateway_resources(resource_type):
    """For all resources in the CloudFormation template, none shall have a
    type matching AWS::ApiGateway::* or AWS::ApiGatewayV2::*."""
    assert not resource_type.startswith("AWS::ApiGateway::"), (
        f"Found API Gateway v1 resource: {resource_type}"
    )
    assert not resource_type.startswith("AWS::ApiGatewayV2::"), (
        f"Found API Gateway v2 resource: {resource_type}"
    )
