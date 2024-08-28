from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

class Database:
    def __init__(self) -> None:
        # Connect to MilvusDB
        connections.connect(host="localhost", port=19530)

        # Load data and preprocess
         # Replace with appropriate data loading method
        # Apply preprocessing steps as needed

        # Create MilvusDB collection schema
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, pk=True,auto_id=True),
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=1024),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
        ]
        schema = CollectionSchema(name="productDetails", fields=fields)

        # Create MilvusDB collection
        self.collection = Collection(schema)
        self.collection.create_index(field_name="embedding", index_type="IVF_FLAT")

    def insert(self,text,embedding):
        self.collection.insert([text, embedding])
    