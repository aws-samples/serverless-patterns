import pytest
from aws_lambda_powertools import Logger
from publish_sfn_failure_to_sns.index import handler

logger = Logger()


@pytest.mark.usefixtures("set_env_vars", "sns_mock")
class TestApp:
    def test_publish_sfn_failure_to_sns_for_step_function(self):
        """
        Test Case Description: This test will verify that the function 'publish_sfn_codebuild_failure_to_sns' sends the correct data to the SNS topic from the Step Function event
        """
        region = "us-west-2"
        account = "123456789012"
        state_machine_pipeline_test_event = {
            "version": "0",
            "id": "f70db68b-8804-5a83-4ca1-87cb2b8c39a1",
            "detail-type": "Step Functions Execution Status Change",
            "source": "aws.states",
            "account": account,
            "time": "2023-04-25T16:58:12Z",
            "region": region,
            "resources": [
                f"arn:aws:states:{region}:{account}:execution:KbSyncPipelineStateMachine-80qwGoKCO32h:db378995-0fa7-42da-bfe7-2112803a9489"
            ],
            "detail": {
                "executionArn": f"arn:aws:states:{region}:{account}:execution:KbSyncPipelineStateMachine-80qwGoKCO32h:db378995-0fa7-42da-bfe7-2112803a9489",
                "stateMachineArn": f"arn:aws:states:{region}:{account}:stateMachine:KbSyncPipelineStateMachine-80qwGoKCO32h",
                "name": "db378995-0fa7-42da-bfe7-2112803a9489",
                "status": "FAILED",
                "startDate": 1682441891824,
                "stopDate": 1682441892117,
                "input": '{"knowledgeBaseId":"adf-pipeline-finops-cost-forecast","scheduled":"true"}',
                "output": None,
                "inputDetails": {"included": True},
                "outputDetails": None,
                "error": None,
                "cause": None,
            },
        }

        response_dict = handler(state_machine_pipeline_test_event, {})

        assert response_dict["errorStatus"] == "FAILED"
        assert response_dict["severity"] == "CRITICAL"
        assert response_dict["originalError"]["source"] == "aws.states"

    def test_publish_sfn_failure_to_sns_for_unknown_event(self):
        """
        Test Case Description: This test will verify that the function 'publish_sfn_failure_to_sns' sends the correct data to the SNS topic from the Code Pipeline event
        """
        region = "us-west-2"
        account = "123456789012"
        code_pipeline_test_event = {
            "version": "0",
            "id": "8bfeaf4c-cda2-1038-d20a-1f43e9c029fd",
            "detail-type": "CodePipeline Pipeline Execution State Change",
            "source": "aws.not_exist",
            "account": account,
            "time": "2023-04-26T07:52:57Z",
            "region": region,
            "resources": [f"arn:aws:codepipeline:{region}:{account}:monitoring-logs-spoke"],
            "detail": {
                "pipeline": "monitoring-logs-spoke",
                "execution-id": "82f19aa0-3f0b-45ab-81fc-5e8c9d3484a5",
                "state": "FAILED",
                "version": 40.0,
            },
        }

        response_dict = handler(code_pipeline_test_event, {})

        assert response_dict["severity"] == "UNKNOWN"
        assert response_dict["originalError"]["source"] == "aws.not_exist"
