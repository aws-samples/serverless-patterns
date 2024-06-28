import os
from langchain.prompts import PromptTemplate
from langchain.llms.bedrock import Bedrock
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

def get_llm():
    
    model_kwargs = { #AI21
        "maxTokens": 8000, 
        "temperature": 0, 
        "topP": 0.5, 
        "stopSequences": [], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock(
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1", #set the foundation model
        model_kwargs=model_kwargs) #configure the properties for Claude
    
    return llm

pdf_path = "uploaded_file.pdf"

def get_example_file_bytes(): #provide the file bytes so the user can download a ready-made example
    with open("2022-Shareholder-Letter.pdf", "rb") as file:
        file_bytes = file.read()
    
    return file_bytes


def save_file(file_bytes): #save the uploaded file to disk to summarize later
    
    with open(pdf_path, "wb") as f: 
        f.write(file_bytes)
    
    return f"Saved {pdf_path}"

def get_docs():
    
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "], chunk_size=4000, chunk_overlap=100 
    )
    docs = text_splitter.split_documents(documents=documents)
    
    return docs

def get_summary(return_intermediate_steps=False):
    
    map_prompt_template = "{text}\n\nWrite a few sentences summarizing the above:"
    map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])
    
    combine_prompt_template = "{text}\n\nWrite a detailed analysis of the above:"
    combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=["text"])
    
    
    llm = get_llm()
    docs = get_docs()
    
    chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=map_prompt, combine_prompt=combine_prompt, return_intermediate_steps=return_intermediate_steps)
    
    if return_intermediate_steps:
        return chain({"input_documents": docs}, return_only_outputs=True) #make return structure consistent with chain.run(docs)
    else:
        return chain.run(docs)

