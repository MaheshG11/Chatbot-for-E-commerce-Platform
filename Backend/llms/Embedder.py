from transformers import BertTokenizer, BertModel
import torch
from transformers import AutoTokenizer, AutoModel
from torch.cuda import is_available
from sentence_transformers import SentenceTransformer
device="cuda" if is_available() else "cpu"


# large Embedding models

class Sentence_Embedder:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    dimension=384
    def embed(self,text:str):
        return list((self.model.encode(text)))
        



# Sample text

# Tokenize the text

# Generate embeddings using ELECTRA



# from llama_index.readers.json import JSONReader
# from llama_index.core import SimpleDirectoryReader, StorageContext

# from llama_index.core import VectorStoreIndex, Settings

# from llama_index.vector_stores.milvus import MilvusVectorStore
# from llama_index.embeddings.fastembed import FastEmbedEmbedding


# parser = JSONReader()
# file_extractor = {".json": parser}  # Add other CSV formats as needed
# documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

# embedding_model = FastEmbedEmbedding(
#     model_name="mixedbread-ai/mxbai-embed-large-v1", max_length=1024
# )

# vector_store = MilvusVectorStore(
#     uri="http://localhost:19530",
#     collection_name="podcast_data_head",
#     dim=1024,
#     overwrite=True,
# )

# Settings.embed_model = embedding_model

# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(
#     documents, storage_context=storage_context, show_progress=True
# )