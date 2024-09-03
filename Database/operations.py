from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection,Milvus,Connections
class Database:
    def __init__(self,dimension,collectionName,metricType,indexType,port,host) -> None:
        # Connect to MilvusDB
        #connections.connect(host="localhost", port=19530)
        connections.connect(host=host, port=port)
        self.metricType=metricType
        self.indexType=indexType
        # Load data and preprocess
         # Replace with appropriate data loading method
        # Apply preprocessing steps as needed
        self.search_params = {"metric_type": self.metricType, "params": {"nprobe": 10}}
        # Create MilvusDB collection schema
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, description="primary id",auto_id=True),
            FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=1024),
            FieldSchema(name="price", dtype=DataType.VARCHAR, max_length=103),
            FieldSchema(name="Description", dtype=DataType.VARCHAR, max_length=10240),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dimension),
            FieldSchema(name="link", dtype=DataType.VARCHAR, max_length=1024),
            FieldSchema(name="imgUrl", dtype=DataType.VARCHAR, max_length=1024)
        ]
        Schema = CollectionSchema(name=collectionName, fields=fields)

        # Create MilvusDB collection
 
        index_params = {
          "metric_type":self.metricType,
          "index_type":self.indexType,
          "params":{"nlist":1024}
        }
        self.collection = Collection(name=collectionName,schema=Schema)
        self.collection.create_index("embedding",index_params=index_params)

    def insert(self,name,desc,link,embedding,price,imgUrl):
        data=[
            {
                "name":name,
                "Description":desc,
                "embedding":embedding,
                "link":link,
                "price":price,
                "imgUrl":imgUrl   
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

        
# database=Database(dimension= 2,collectionName="name",metric="L2",indexType="IVF_FLAT",port=19530,host="localhost")
# database.insert("something","sdf","dfgdfg",[1024,1024])