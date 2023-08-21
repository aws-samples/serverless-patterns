from typing import List
from aws_lambda_powertools.utilities.parser import BaseModel


class Message(BaseModel):
    eventSource: str
    bootstrapServers: str
    eventSourceKey: str
    topic: str
    partition: int
    offset: int
    timestamp: int
    timestampType: str
    key: str
    value: str
    headers: List[dict]


class MessageList(BaseModel):
    __root__: List[Message]
