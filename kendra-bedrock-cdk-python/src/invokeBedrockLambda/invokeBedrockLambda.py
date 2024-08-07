import os
import boto3
import json
# retrieves kendra index id
kendra_index_id = os.environ['INDEX_ID']
region = os.environ['AWS_REGION']
model_id = os.environ['MODEL_ID']
def kendra_retrieve_document(question):
    """
    This function takes in the question from the user, and retrieves relevant passages based on default PageSize of 10.
    :param question: The question the user is asking.
    :return: Returns the context to be sent to the LLM and document URIs to be returned as relevant data sources.
    """
    kendra_client = boto3.client('kendra')
    documents = kendra_client.retrieve(IndexId=kendra_index_id, QueryText=question)
    text = ""
    uris = set()
    if len(documents['ResultItems']) > 0:
        for i in range(len(documents['ResultItems'])):
            text += documents['ResultItems'][i]['Content'] + "\n"
            uris.add(documents['ResultItems'][i]['DocumentURI'])
    return (text, uris)
def invokeLLM(question, context):
    """
    This function takes in the question from the user, along with the Kendra responses as context to generate an answer
    for the user on the frontend.
    :param question: The question the user is asking .
    :param context: The context to be sent to the LLM to generate a better
    answer.
    :return: Returns the final answer that will be provided to the end-user of the application who asked the original
    question.
    """
    # Setup Bedrock client
    bedrock = boto3.client('bedrock-runtime')
    # body of data with parameters that is passed into the bedrock invoke model request
    body = json.dumps({"max_tokens": 350,
            "system": "You are a truthful AI assistant. Your goal is to provide informative and substantive responses to queries based on the documents provided. If you do not know the answer to a question, you truthfully say you do not know.",
            "messages": [{"role": "user", "content": "Answer this user query:" + question + "with the following context:" + context}],
              "anthropic_version": "bedrock-2023-05-31",
                "temperature":0,
              "top_k":250,
              "top_p":0.999})
    # Invoking the bedrock model
    response = bedrock.invoke_model(body=body,
                                    modelId=model_id)
    response_body = json.loads(response.get('body').read())
    answer = response_body.get('content')
    # returning the answer as a final result, which ultimately gets returned to the end user
    return answer

def lambda_handler(event, context):
    question = event['question'] 
    context = kendra_retrieve_document(question)
    llm_response = invokeLLM(question, context[0])
    answer = llm_response[0]['text'] +"\n" + "*Relevant links:* " + "\n" + "\n".join(context[1])
    return answer