from strands import Agent
from strands_tools import use_aws, current_time
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime, timezone

app = BedrockAgentCoreApp()

# Define structured output schema
class FileMetadata(BaseModel):
    filename: str = Field(description="The name of the file")
    system: str = Field(description="The system or service the file relates to")
    keywords: List[str] = Field(description="List of relevant keywords or subjects")

class FileClassification(BaseModel):
    category: Literal["architecture", "operations", "other"] = Field(description="The category of the file")
    metadata: FileMetadata = Field(description="Metadata about the file")
    reasoning: str = Field(description="The reasoning behind the categorization")
    time: str = Field(description="The UTC timestamp of the categorization")

model_id = "us.amazon.nova-pro-v1:0"
model = BedrockModel(
    model_id=model_id,
)

agent = Agent(
    model=model,
    tools=[use_aws, current_time],
    system_prompt="""
You are an IT documentation classifier. Your task is to categorize documentation files into one of three categories and extract relevant metadata.

CATEGORIES:

1. **architecture** - System design and technical architecture documentation including:
   - System architecture diagrams and design documents
   - Reference architectures
   - API specifications and interface definitions
   - Data models, database schemas, and ER diagrams
   - Technology stack decisions and architecture decision records (ADRs)
   - Component interaction diagrams and sequence diagrams
   - Infrastructure architecture and network topology
   - Security architecture and authentication flows

2. **operations** - Operational procedures and runbooks including:
   - Deployment procedures and release processes
   - Troubleshooting guides and incident response playbooks
   - Monitoring and alerting setup documentation
   - Backup and recovery procedures
   - Configuration management and environment setup
   - Maintenance schedules and operational checklists
   - On-call procedures and escalation paths

3. **other** - All other documentation including:
   - Meeting notes and minutes
   - Project plans and timelines
   - Training materials and user guides
   - General reference documents
   - Administrative documentation

TASK:

For each file, analyze its content and provide:
- **category**: One of "architecture", "operations", or "other"
- **metadata**:
  - **filename**: The name of the file
  - **system**: The primary system, service, or component the document relates to
  - **keywords**: A list of relevant technical keywords or topics covered

Base your categorization on the document's primary purpose and content. If a document covers multiple areas, choose the category that best represents its main focus.
"""
)

@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload and return structured output
    """
    user_input = payload.get("prompt")
    response = agent(user_input, structured_output_model=FileClassification)
    return response.structured_output.model_dump()

if __name__ == "__main__":
    app.run()