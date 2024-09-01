from fastapi import FastAPI,Request
import uvicorn
import os
from dotenv import load_dotenv
import json
from torch.cuda import is_available 
from llmops import llmInteractions
load_dotenv()
app = FastAPI()

device="cuda:0" if is_available() else "cpu"

llm=llmInteractions()
@app.post("/ingest")
async def ingestion(request:Request):
    data= await request.json()
    await llm.ingest(data)
    return {"message": "Hello World"}

@app.get("/infer")
async def inference(request:Request):
    data= await request.json()
    response= await llm.inference(data['query'])
    
    return response
if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("ApiHost"),
        port=int(os.getenv("ApiPort")),
    )