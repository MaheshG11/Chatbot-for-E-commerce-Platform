
from .llms.Embeddings import Embedder
from Database.operations import Database
class llmInteractions:
    def __init__(self) -> None:
        
        self.embedder=Embedder()
        self.database=Database()

    def ingest(self,text):
        self.database.insert(text,embedding=self.embedder.embed(text=text))



































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