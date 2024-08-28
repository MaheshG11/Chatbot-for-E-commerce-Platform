import time

import numpy as np
import string
import random

from pymilvus import MilvusClient, DataType, client

fmt = "\n=== {:30} ===\n"
search_latency_fmt = "search latency = {:.4f}s"
num_entities, dim = 3000, 8

#################################################################################
# 1. connect to Milvus
# Add a new connection alias `default` for Milvus server in `localhost:19530`
# Actually the "default" alias is a buildin in PyMilvus.
# If the address of Milvus is the same as `localhost:19530`, you can omit all
# parameters and call the method as: `connections.connect()`.
#
# Note: the `using` parameter of the following methods is default to "default".
print(fmt.format("start connecting to Milvus"))
milvus_client = MilvusClient(host="0.0.0.0", port=9091) # Replace with your Milvus server address
# print(milvus_client.create_database("db1"))
print(milvus_client.create_collection("col1",dimension=2))
print(milvus_client.has_collection("col1"))
print(milvus_client.list_databases())
# has = client.has_collection("hello_milvus")
# print(f"Does collection hello_milvus exist in Milvus: {has}")
