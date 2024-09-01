from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection,MilvusClient
import os
class Database:
    def __init__(self,dimension,collectionName,metricType,indexType,port,host) -> None:
        # Connect to MilvusDB
        #connections.connect(host="localhost", port=19530)
        connections.connect(host=host, port=port)
        self.metricType=metricType
        self.indexType=indexType
        self.collectionName=collectionName
        self.client=MilvusClient(
                uri=f"http://{os.getenv("MilvusHost")}:{os.getenv("MilvusPort")}"
            )
        # Load data and preprocess
         # Replace with appropriate data loading method
        # Apply preprocessing steps as needed
        self.search_params = {"metric_type": self.metricType, "params": {"nprobe": 10}}
        # Create MilvusDB collection schema
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, description="primary id",auto_id=True),
            FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=1024),
            FieldSchema(name="Description", dtype=DataType.VARCHAR, max_length=10240),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dimension),
            FieldSchema(name="link", dtype=DataType.VARCHAR, max_length=1024),
        ]
        Schema = CollectionSchema(name="productDetails", fields=fields)

        # Create MilvusDB collection
 
        index_params = {
          "metric_type":self.metricType,
          "index_type":self.indexType,
          "params":{"nlist":1024}
        }
        self.collection = Collection(name=collectionName,schema=Schema)
        self.collection.create_index("embedding",index_params=index_params)

    def insert(self,name,desc,link,embedding):
        data=[
            {
                "name":name,
                "Description":desc,
                "embedding":embedding,
                "link":link   
            }
        ]
        self.collection.insert(data=data)
    def search(self,embedding):
        results = self.collection.search(
            data=embedding,
            anns_field="embedding", 
            param=self.search_params, 
            limit=10, 
            expr=None,
            consistency_level="Strong"
        )
        return results

if __name__=="__main__":
        
    database=Database(dimension= 2,collectionName="name",metric="L2",indexType="IVF_FLAT",port=19530,host="localhost")
    database.insert("something","sdf","dfgdfg",[1024,1024])