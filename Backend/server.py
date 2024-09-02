from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv
import json
from torch.cuda import is_available 
from llmops import llmInteractions
load_dotenv()
app = FastAPI()
origins = [
    '*',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

device="cuda:0" if is_available() else "cpu"

llm=llmInteractions()
@app.post("/ingest")
async def ingestion(request:Request):
    data= await request.json()
    invalid=[]
    for i in data:
        if(type(data[i])!=list):
            invalid.append(i)
        else:
            data[i]=data[i][0]
    if(len(invalid)):
        response={"message":"Empty Fields Found. CANNOT INGEST","Invalid Fields":invalid}
    else:
        await llm.ingest(data)
        response={"message": "Data Entered Successfully"}
    return response

@app.post("/infer")
async def inference(request:Request):
    data= await request.json()
    # data=request.body()
    # print(request)
    print((data))
    response="hehe"
    response= await llm.inference(data['query'])
    # response=data
    return response
if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("ApiHost"),
        port=int(os.getenv("ApiPort")),
    )