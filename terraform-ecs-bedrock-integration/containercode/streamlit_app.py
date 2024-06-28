import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import json
import boto3


def clear_text():
    st.session_state["input"] = ""

"""
# Welcome to GenAI App Build on AWS
"""
prompt_type = st.radio(
            "Set Option on what you want to do 👇",
            key="visibility",
            label_visibility="visible",
            horizontal=True,
            options=["paraphrase", "explain", "tell me something"],
)

user_text = st.text_input(label="Please type below",
                            key="input", 
                            label_visibility="visible",
                            disabled=False,
                            placeholder=""
)

boto3_invoke_bedrock = boto3.client('bedrock-runtime')
if user_text:
    prompt_data_text=prompt_type + " " + user_text
    body = json.dumps({"prompt": "Human:" + prompt_data_text + "\nAssistant:", "max_tokens_to_sample":600})

    modelId='anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'
    response = boto3_invoke_bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    st.write("Bot Response: ", response_body.get('completion'))