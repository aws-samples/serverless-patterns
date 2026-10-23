# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""The confidence gate and the shape of the workflow, read from the synthesized template.

Run `npm test` (it synthesizes first) or `npx cdk synth --quiet && python3 -m unittest discover -s test`.
"""
import copy
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import asl  # noqa: E402

HERE = os.path.dirname(__file__)
FIXTURES = os.path.join(HERE, "fixtures")

# Defaults in lib/strands-decider-confidence-gated-triage-stack.ts
DEPT, PAGE, CLEAR = 0.9, 0.7, 0.3


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


QUESTIONS = _load(os.path.join(HERE, "..", "questions.json"))


def state_after_model(dept_conf=0.95, sec_p=0.02, urgency_conf=0.4):
    """The state document the gate sees: the ticket plus a model response shaped like the real ones."""
    return {
        "id": "T-1",
        "text": "My payouts have failed for 3 days.",
        "model": {"response": {"answers": {
            "department": {"type": "choice", "choice": "billing", "confidence": dept_conf},
            "urgency": {"type": "score", "score": 1.5, "confidence": urgency_conf},
            "security_incident": {"type": "noul", "noul": sec_p},
        }}},
    }


class GateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.definition = asl.state_machine_definition(asl.load_template())

    def gate(self, doc):
        return asl.gate_result(self.definition, doc)

    def test_the_five_branches(self):
        self.assertEqual(self.gate(state_after_model()), ("auto_routed", "confident"))
        self.assertEqual(self.gate(state_after_model(sec_p=0.96)), ("paged_and_review", "security_incident_suspected"))
        self.assertEqual(self.gate(state_after_model(sec_p=0.5)), ("review", "security_uncertain"))
        self.assertEqual(self.gate(state_after_model(dept_conf=0.3)), ("review", "low_confidence"))
        self.assertEqual(self.gate(state_after_model(dept_conf=7)), ("review", "decision_unavailable"))

    def test_thresholds_are_inclusive_for_action_and_exclusive_for_clear(self):
        self.assertEqual(self.gate(state_after_model(sec_p=PAGE))[1], "security_incident_suspected")
        self.assertEqual(self.gate(state_after_model(sec_p=PAGE - 0.001))[1], "security_uncertain")
        self.assertEqual(self.gate(state_after_model(sec_p=CLEAR))[1], "confident")
        self.assertEqual(self.gate(state_after_model(sec_p=CLEAR + 0.001))[1], "security_uncertain")
        self.assertEqual(self.gate(state_after_model(dept_conf=DEPT))[1], "confident")
        self.assertEqual(self.gate(state_after_model(dept_conf=DEPT - 0.001))[1], "low_confidence")

    def test_security_wins_over_department_confidence_and_urgency_does_not_gate(self):
        self.assertEqual(self.gate(state_after_model(dept_conf=1.0, sec_p=0.95))[0], "paged_and_review")
        for urgency_conf in (0.0, 0.2, 1.0):
            self.assertEqual(self.gate(state_after_model(urgency_conf=urgency_conf))[1], "confident")

    def test_answers_the_gate_cannot_trust_go_to_a_person(self):
        def mutated(path, value=None, delete=False):
            doc = copy.deepcopy(state_after_model())
            cur = doc["model"]["response"]
            for key in path[:-1]:
                cur = cur[key]
            if delete:
                del cur[path[-1]]
            else:
                cur[path[-1]] = value
            return doc

        dept = ["answers", "department", "confidence"]
        sec = ["answers", "security_incident", "noul"]
        cases = {
            "security answer missing": mutated(["answers", "security_incident"], delete=True),
            "security probability missing": mutated(sec, delete=True),
            "department answer missing": mutated(["answers", "department"], delete=True),
            "department confidence missing": mutated(dept, delete=True),
            "security probability is a string": mutated(sec, "0.9"),
            "security probability is a boolean": mutated(sec, True),
            "security probability is null": mutated(sec, None),
            "security probability above 1": mutated(sec, 1.5),
            "security probability below 0": mutated(sec, -0.1),
            "department confidence above 1": mutated(dept, 1.5),
            "department confidence is a string": mutated(dept, "0.99"),
        }
        for label, doc in cases.items():
            with self.subTest(label):
                self.assertEqual(self.gate(doc), ("review", "decision_unavailable"))
        no_answers = {"id": "T-1", "text": "x", "model": {"response": {"model": "x"}}}
        self.assertEqual(self.gate(no_answers), ("review", "decision_unavailable"))

    def test_a_broken_department_answer_does_not_suppress_a_security_page(self):
        for label, doc in (("missing", state_after_model(sec_p=0.96)), ("out of range", state_after_model(dept_conf=7, sec_p=0.96))):
            with self.subTest(label):
                if label == "missing":
                    del doc["model"]["response"]["answers"]["department"]
                self.assertEqual(self.gate(doc), ("paged_and_review", "security_incident_suspected"))

    def test_invalid_input_never_reaches_the_model(self):
        for bad in ({}, {"id": "T-1"}, {"text": "hi"}, {"id": 7, "text": "hi"}, {"id": "T-1", "text": None}):
            with self.subTest(bad):
                self.assertEqual(asl.next_state(self.definition, "ValidateInput", bad), "InvalidTicket")
        self.assertEqual(asl.next_state(self.definition, "ValidateInput", {"id": "T-1", "text": "hi"}), "AskDecider")
        self.assertEqual(self.definition["States"]["InvalidTicket"]["Error"], "InvalidTicket")

    def test_recorded_model_responses_route_as_expected(self):
        expected = _load(os.path.join(FIXTURES, "expected-routes.json"))
        for name, want in expected.items():
            with self.subTest(name):
                fixture = _load(os.path.join(FIXTURES, name + ".json"))
                self.assertEqual(fixture["http_status"], 200)
                # The recorded request is exactly what the workflow sends to the endpoint.
                self.assertEqual(fixture["request"]["questions"], QUESTIONS)
                doc = {"id": name, "text": fixture["request"]["state"], "model": {"response": fixture["response"]}}
                self.assertEqual(self.gate(doc), tuple(want), fixture["note"])


class TemplateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = asl.load_template()
        cls.resources = cls.template["Resources"]
        cls.states = asl.state_machine_definition(cls.template)["States"]

    def of_type(self, kind):
        return [r for r in self.resources.values() if r["Type"] == kind]

    def test_there_is_no_lambda_function_or_api(self):
        kinds = {r["Type"] for r in self.resources.values()}
        self.assertFalse({"AWS::Lambda::Function", "AWS::ApiGateway::RestApi"} & kinds)

    def test_state_machine_is_express_and_does_not_log_execution_data(self):
        (machine,) = self.of_type("AWS::StepFunctions::StateMachine")
        props = machine["Properties"]
        self.assertEqual(props["StateMachineType"], "EXPRESS")
        self.assertEqual(props["LoggingConfiguration"]["Level"], "ERROR")
        self.assertIs(props["LoggingConfiguration"]["IncludeExecutionData"], False)

    def test_endpoint_variant_waits_long_enough_for_the_model_download(self):
        (config,) = self.of_type("AWS::SageMaker::EndpointConfig")
        (variant,) = config["Properties"]["ProductionVariants"]
        self.assertEqual(variant["InitialInstanceCount"], 1)
        self.assertGreaterEqual(variant["ContainerStartupHealthCheckTimeoutInSeconds"], 900)

    def test_workflow_may_invoke_only_this_endpoint(self):
        statements = []
        for policy in self.of_type("AWS::IAM::Policy"):
            statements += [s for s in policy["Properties"]["PolicyDocument"]["Statement"]
                           if "sagemaker:InvokeEndpoint" in (s["Action"] if isinstance(s["Action"], list) else [s["Action"]])]
        self.assertEqual(len(statements), 1)
        (endpoint_id,) = [k for k, r in self.resources.items() if r["Type"] == "AWS::SageMaker::Endpoint"]
        self.assertEqual(statements[0]["Resource"], {"Ref": endpoint_id})

    def test_no_resource_wildcards_except_documented_service_actions(self):
        allowed_actions = {"ecr:GetAuthorizationToken", "logs:CreateLogDelivery",
                           "logs:GetLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery",
                           "logs:ListLogDeliveries", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies",
                           "logs:DescribeLogGroups"}
        offenders = []
        for policy in self.of_type("AWS::IAM::Policy"):
            for statement in policy["Properties"]["PolicyDocument"]["Statement"]:
                resources = statement.get("Resource")
                resources = resources if isinstance(resources, list) else [resources]
                actions = statement["Action"] if isinstance(statement["Action"], list) else [statement["Action"]]
                if "*" in resources and not set(actions) <= allowed_actions:
                    offenders.append((actions, resources))
        self.assertEqual(offenders, [])

    def test_queues_and_topic_require_tls(self):
        policies = self.of_type("AWS::SQS::QueuePolicy") + self.of_type("AWS::SNS::TopicPolicy")
        self.assertEqual(len(policies), 3, "two queues and one topic each deny non-TLS access")
        for policy in policies:
            self.assertIn('"aws:SecureTransport": "false"', json.dumps(policy["Properties"]["PolicyDocument"]))

    def test_the_dead_letter_queue_keeps_messages_longer_than_the_review_queue(self):
        # SQS counts a message's retention from its first enqueue, so the dead-letter queue must outlast the source.
        queues = [r for r in self.resources.values() if r["Type"] == "AWS::SQS::Queue"]
        (source,) = [r for r in queues if "RedrivePolicy" in r["Properties"]]
        (dlq,) = [r for r in queues if "RedrivePolicy" not in r["Properties"]]
        self.assertGreater(dlq["Properties"]["MessageRetentionPeriod"], source["Properties"]["MessageRetentionPeriod"])

    def test_both_model_revisions_are_pinned_to_full_commit_hashes(self):
        (model,) = self.of_type("AWS::SageMaker::Model")
        environment = model["Properties"]["PrimaryContainer"]["Environment"]
        for key in ("DECIDER_REVISION", "DECIDER_BASE_REVISION"):
            self.assertRegex(environment[key], r"^[0-9a-f]{40}$", key)

    # --- the model call ---------------------------------------------------------------------------------
    def test_the_model_call_sends_the_ticket_and_the_three_questions(self):
        body = self.states["AskDecider"]["Arguments"]["Body"]
        self.assertEqual(body["state"], "{% $states.input.text %}")
        self.assertEqual(body["questions"], QUESTIONS)
        self.assertEqual(set(QUESTIONS), {"department", "urgency", "security_incident"})

    def test_the_model_call_retries_only_throttling_and_transient_errors_and_times_out_after_60_seconds(self):
        state = self.states["AskDecider"]
        (retrier,) = state["Retry"]
        self.assertEqual(sorted(retrier["ErrorEquals"]),
                         ["SageMakerRuntime.InternalFailureException", "SageMakerRuntime.ServiceUnavailableException",
                          "SageMakerRuntime.ThrottlingException"])
        self.assertEqual(retrier["MaxAttempts"], 2)
        self.assertEqual(state["TimeoutSeconds"], 60)

    def test_a_failed_model_call_or_an_unparsable_body_goes_to_review(self):
        # JSONPath States.StringToJson on a body that is not JSON raises States.Runtime, which no Catch can
        # handle. JSONata $parse raises States.QueryEvaluationError, which a Catch on States.ALL handles.
        state = self.states["AskDecider"]
        self.assertEqual(state["QueryLanguage"], "JSONata")
        self.assertEqual([n for n, s in self.states.items() if s.get("QueryLanguage") == "JSONata"], ["AskDecider"])
        self.assertNotIn("States.StringToJson", json.dumps(state))
        self.assertIn("$parse($states.result.Body)", state["Output"])
        (catcher,) = state["Catch"]
        self.assertEqual((catcher["ErrorEquals"], catcher["Next"]), (["States.ALL"], "ReasonDecisionUnavailable"))
        self.assertIn("$states.errorOutput", catcher["Output"])
        self.assertEqual(self.states["ReasonDecisionUnavailable"]["Next"], "SendToHumanReview")

    # --- the queue and the page ---------------------------------------------------------------------------
    def test_queue_and_topic_calls_retry_except_permanent_errors_and_a_failed_page_still_reaches_review(self):
        # The first retrier matches the errors that a retry cannot fix and allows no attempts. States.TaskFailed
        # in the second matches every known error except States.Timeout, so everything else is retried.
        missing = {"SendToHumanReview": "SQS.QueueDoesNotExistException", "PageSecurityOnCall": "SNS.NotFoundException"}
        for name, error in missing.items():
            permanent, others = self.states[name]["Retry"]
            self.assertEqual(sorted(permanent["ErrorEquals"]), sorted(["States.Permissions", error]), name)
            self.assertEqual(permanent["MaxAttempts"], 0, name)
            self.assertEqual(others["ErrorEquals"], ["States.TaskFailed"], name)
            self.assertEqual(others["MaxAttempts"], 3, name)
        (catcher,) = self.states["PageSecurityOnCall"]["Catch"]
        self.assertEqual((catcher["ErrorEquals"], catcher["Next"]), (["States.ALL"], "ReasonPageFailed"))
        self.assertEqual(self.states["ReasonPageFailed"]["Next"], "SendToHumanReview")
        self.assertNotIn("Catch", self.states["SendToHumanReview"], "an unreachable queue must fail the execution")

    def test_the_review_message_is_the_whole_state_and_the_page_has_no_ticket_text(self):
        self.assertEqual(self.states["SendToHumanReview"]["Parameters"]["MessageBody.$"], "$")
        message = self.states["PageSecurityOnCall"]["Parameters"]["Message"]
        self.assertEqual(set(message), {"ticket_id.$", "security_probability.$"})
        self.assertEqual(message["ticket_id.$"], "$.id")


if __name__ == "__main__":
    unittest.main()
