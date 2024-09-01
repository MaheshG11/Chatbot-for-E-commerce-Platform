
from llms.Embedder import Electra_Embedder,Bert_Embedder,Sentence_Embedder
from Database.operations import Database
from llms.geminiAPI import InferGemini
import json
import os

userInformation="User Information:{name:Mahesh, Occupation: Engineering Student,gender:Male}"
PurchaseHistory="Purchase History:Previously purchased Items include protien powder, Iphone 15 pro, Peanut butter, beardo's Face Serum, sunscreen, Hard Disk."
conversationHistory=[]
previouslyViewedProducts={}

class llmInteractions:
    
    def __init__(self) -> None:
        
        self.embedder=Sentence_Embedder()
        self.Gemini=InferGemini()
        self.database=Database(dimension= self.embedder.dimension,collectionName="productDetails",
                               metricType="IP",indexType="IVF_FLAT",port=os.getenv("MilvusPort"),
                               host=os.getenv("MilvusHost"))
        print("IP")

    async def ingest(self,data:dict):
        link= data["image"] if "image" in data else "www.example.com"
        text=json.dumps(data)
        # print(type(data)) # = string
        augmentedDataList=self.Gemini.augment(text)
    
        for augmentedData in augmentedDataList:
            embedding=self.embedder.embed(text=augmentedData)
            self.database.insert(name=data["name"],desc=text,embedding=embedding,link=link)

    async def inference(self,query):
        # speech to text to be integrated
        query="User's Query: "+query
        finalResponse=self.Gemini.Inference(query=query,conversationHistory=json.dumps(conversationHistory),
                                            PurchaseHistory=PurchaseHistory,userInformation=userInformation,
                                            PreviouslyViewedProducts=previouslyViewedProducts)
        
        conversationHistory.append({query:finalResponse['response']})
        if(len(conversationHistory)>5):
            conversationHistory.remove(0)
        response={"response":finalResponse['response']}
        if(finalResponse['rag_required']):
            search_text=finalResponse['search_phrase'] if 'search_phrase' in finalResponse else finalResponse['response']
            response={"search_phrase":search_text}
            search_vector=[self.embedder.embed(search_text)]
            print(search_text)
            topk=self.database.search(search_vector)
            products=[]
            for i in topk[0]:
                print(i)
                data=(self.database.client.get(collection_name=self.database.collectionName,ids=[i.id]))[0]

                del data['embedding']
                products.append(data)
            response["products"]=products
            previouslyViewedProducts={"Previously Viewed Products":products}
            
        return response
































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