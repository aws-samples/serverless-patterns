import json
from http import HTTPStatus

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import ALBResolver, Response, content_types
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths

log = Logger()
app = ALBResolver()


@app.get("/hello")
def sample_get() -> Response:
    client_correlation_id = app.current_event.get_header_value(name="Client-Correlation-Id")
    log.info(f"client_correlation_id: {client_correlation_id}")
    response = {
        "message": "Hi from API behind ALB"
    }
    return Response(status_code=int(HTTPStatus.OK), body=json.dumps(response),
                    content_type=content_types.APPLICATION_JSON)


@log.inject_lambda_context(correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER, log_event=True,
                           clear_state=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    log.debug(event)
    return app.resolve(event, context)