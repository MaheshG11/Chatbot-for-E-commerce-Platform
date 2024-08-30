
from llms.Embedder import Electra_Embedder
from Database.operations import Database
from llms.geminiAPI import InferGemini
import json
from fastapi import Request
class llmInteractions:
    
    def __init__(self) -> None:
        
        self.embedder=Electra_Embedder()
        self.database=Database(self.embedder.dimension,"productDetails",)
        self.Gemini=InferGemini()
        self.database=Database(dimension= self.embedder.dimension,collectionName="productDetails",metric="L2",indexType="IVF_FLAT",port=19530,host="localhost")

    async def ingest(self,data:dict):
        link= data["link"] if "link" in data else "www.example.com"
        text=json.dumps(data)
        # print(type(data)) # = string
        augmentedDataList=self.Gemini.augment(text)
        for augmentedData in augmentedDataList:
            embedding=self.embedder.embed(text=augmentedData)
            self.database.insert(name=data["name"],desc=text,embedding=embedding,link=link)

    async def inference(self,query):
        return self.Gemini.firstInference(query=query)
































'''
# Connect to MilvusDB
connections.connect(host="localhost", port=19530)

# Load data and preprocess
 # Replace with appropriate data loading method
# Apply preprocessing steps as needed

# Create MilvusDB collection schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, pk=True),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=1024),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
]
schema = CollectionSchema(name="your_collection", fields=fields)

# Create MilvusDB collection
collection = Collection(schema)

# Load LLM model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Iterate over data and create embeddings
for index, row in data.iterrows():
    text = row["text"]  # Replace with appropriate column name
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

    # Insert data into MilvusDB
    collection.insert([index, text, embedding])

# Create index for efficient search
collection.create_index(field_name="embedding", index_type="IVF_FLAT")

# Example search query
query_text = "your_query_text"
query_inputs = tokenizer(query_text, return_tensors="pt")
query_outputs = model(**query_inputs)
query_embedding = query_outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

search_results = collection.search(query_embedding, top_k=5)
print(search_results)
'''