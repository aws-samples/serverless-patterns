import os
import json

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import BedrockChat
from langchain.embeddings import BedrockEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import LanceDB

import lancedb as ldb

embeddings = BedrockEmbeddings(
    region_name="us-west-2"
)

# Retrieve data from S3 and load it into local LanceDB
s3_bucket = os.environ.get('s3BucketName')
db = ldb.connect(f"s3://{s3_bucket}/")
tbl = db.open_table('doc_table')

# Initialize LanceDB instance within langchain
vectorstore = LanceDB(connection=tbl, embedding=embeddings)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

# Create langchain prompt and initialize the Bedrock model
prompt = ChatPromptTemplate.from_template(template)
model = BedrockChat(model_id="anthropic.claude-v2", model_kwargs={"temperature": 0.1})

# Chain together the RAG search to Lance, our prompt, the LLM model, and stringifying the output
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

def lambda_handler(event, context):
    
    if event['queryStringParameters'].get('warmup') is not None:
        return {
            "statusCode": 202,
            "body": json.dumps({
                "message": "warming up",
                "toTimeout": context.get_remaining_time_in_millis()
            })
        }
    
    question = event['queryStringParameters'].get('question')
    
    if question is not None:
        
        results = chain.invoke(question)
        print(results)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": results,
            }),
        }
    
    return {
        "statusCode": 400,
        "body":{
            json.dumps({
                "message":"either provide question or warmup directive"
            })
        }
    }


