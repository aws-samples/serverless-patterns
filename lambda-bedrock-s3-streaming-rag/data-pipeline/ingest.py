import os

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import LanceDB
from langchain.embeddings import BedrockEmbeddings
from langchain.document_loaders import PyPDFDirectoryLoader

import lancedb as ldb
import pyarrow as pa

embeddings = BedrockEmbeddings()

# we split the data into chunks of 1,000 characters, with an overlap
# of 200 characters between the chunks, which helps to give better results
# and contain the context of the information between chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

db = ldb.connect('/tmp/embeddings')

schema = pa.schema(
  [
      pa.field("vector", pa.list_(pa.float32(), 1536)), # document vector with 1.5k dimensions (TitanEmbedding)
      pa.field("text", pa.string()), # langchain requires it
      pa.field("id", pa.string()) # langchain requires it
  ])

tbl = db.create_table("doc_table", schema=schema)

# load the document as before

loader = PyPDFDirectoryLoader("./docs/")

docs = loader.load()
docs = text_splitter.split_documents(docs)

LanceDB.from_documents(docs, embeddings, connection=tbl)
