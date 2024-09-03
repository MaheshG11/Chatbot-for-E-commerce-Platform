import json
with open('augmented505.json', 'r') as file:
    data = json.load(file)
    file.close()
data=data["augmented Data"]
from operations import Database
import os
database=Database(dimension= 384,collectionName="productDetails",
                               metricType="IP",indexType="IVF_FLAT",port=os.getenv("MilvusPort"),
                               host=os.getenv("MilvusHost"))
from Embedder import Sentence_Embedder
embedder=Sentence_Embedder()
done=0
for product in data:
    augmented=product["augmented"]
    del product["augmented"]
    for augmentData in augmented:
        database.insert(product["name"],json.dumps(product),product["link"],embedder.embed(augmentData),product["actual_price"],product["image"])
    done+=1
    print(f"Done {done} of {len(data)}",end="\r")

