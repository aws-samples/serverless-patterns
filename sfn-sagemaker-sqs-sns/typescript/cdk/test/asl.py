# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Reads the synthesized state machine out of the CloudFormation template and evaluates its Choice states.

`cdk synth` writes the template. The tests evaluate the Choice rules of the deployed definition, not a
copy of their logic. Only the operators the definition uses are implemented; anything else raises
NotImplementedError, so a change to the rules cannot pass unnoticed.
"""
import json
import os

TEMPLATE = os.environ.get("GATE_TEMPLATE") or os.path.join(
    os.path.dirname(__file__), "..", "cdk.out", "StrandsDeciderConfidenceGatedTriageStack.template.json"
)


def load_template(path=TEMPLATE):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found. Run `npx cdk synth --quiet` first (npm test does).")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def state_machine_definition(template):
    machines = [r for r in template["Resources"].values() if r["Type"] == "AWS::StepFunctions::StateMachine"]
    assert len(machines) == 1, "expected exactly one state machine"
    definition = machines[0]["Properties"]["DefinitionString"]
    if isinstance(definition, dict):
        # Intrinsic references (endpoint name, queue URL, topic ARN) are not needed to evaluate the rules.
        definition = "".join(p if isinstance(p, str) else "REF" for p in definition["Fn::Join"][1])
    return json.loads(definition)


def _get(doc, path):
    cur = doc
    for key in path[2:].split("."):
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError(path)
        cur = cur[key]
    return cur


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def evaluate(rule, doc):
    """Evaluate one Choice rule (or nested And/Or/Not) against the state input."""
    if "And" in rule:
        return all(evaluate(r, doc) for r in rule["And"])  # short-circuits, as Step Functions does
    if "Or" in rule:
        return any(evaluate(r, doc) for r in rule["Or"])
    if "Not" in rule:
        return not evaluate(rule["Not"], doc)
    var = rule["Variable"]
    if "IsPresent" in rule:
        try:
            _get(doc, var)
            present = True
        except KeyError:
            present = False
        return present == rule["IsPresent"]
    value = _get(doc, var)  # a missing path is a States.Runtime error in Step Functions too
    ops = {
        "IsNumeric": lambda v, e: _is_number(v) == e,
        "IsString": lambda v, e: isinstance(v, str) == e,
        "NumericGreaterThanEquals": lambda v, e: v >= e,
        "NumericGreaterThan": lambda v, e: v > e,
        "NumericLessThanEquals": lambda v, e: v <= e,
        "NumericLessThan": lambda v, e: v < e,
    }
    (op,) = [k for k in rule if k not in ("Variable", "Next")]
    if op not in ops:
        raise NotImplementedError(op)
    return ops[op](value, rule[op])


def next_state(definition, name, doc):
    """The state that Choice state `name` sends `doc` to."""
    state = definition["States"][name]
    for rule in state["Choices"]:
        if evaluate(rule, doc):
            return rule["Next"]
    return state["Default"]


def gate_result(definition, doc):
    """(outcome, reason) that the confidence gate gives to a document that holds the parsed model response."""
    result = definition["States"][next_state(definition, "ConfidenceGate", doc)]["Result"]
    return result["outcome"], result["reason"]
