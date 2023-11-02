# Serverless RAG with Lambda, S3, and LanceDB - Data Ingestion

This data ingestion pipeline allows you to create embeddings from your PDF 
documents and make them available to LanceDB in your Lambda function.

## Prerequisites

As you'll be running this locally, make sure your `aws cli` is configured with
permissions to PUT files on S3 and invoke models on Amazon Bedrock.

## Usage

1. Make sure you have deployed the stack to your AWS account first. More info in
the [`README`](../README.md) in the root of this repository
1. `pip install -r requirements.txt`
1. Copy all the `.pdf` documents you want to ingest to `./docs`. Make sure they 
all have `.pdf` extensions. In this example, we'll only ingest PDF documents.
1. Get your stack name from `../samconfig.toml`


```bash
cd data-pipeline
pip install -r requirements.txt
chmod u+x run.sh # ensure you can execute the file
./run.sh <your-stack-name>
```

## Notes

Once you've run the script, you can find your embeddings in `./embeddings`.  
To produce such embeddings we're making use of 
[Amazon's Titan Embedding model](https://aws.amazon.com/bedrock/titan/#Titan_Embeddings_.28generally_available.29).