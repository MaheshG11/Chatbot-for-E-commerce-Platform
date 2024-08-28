import google.generativeai as genai
import os
import json 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


class InferGemini:
    def __init__(self) -> None:
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")


    def firstInference(self,query,conversationHistory="",PreviouslyViewedProducts="",userInformation=""):
        structure_of_request='''[relevant information and query structure, format of response required,conversation history,previously viewed products, user information, query]'''
        relevantInformationAndQueryStructure=f"Assume that you are an AI who is specialized in selling product.The structure of this request is {structure_of_request}"
        response_format='''Respond in this Json format {"answer":string,"isRAG_Required":bool}.Do not give any other additional information.
        'answer'If RAG is not required then 'answer' is the answer for the 'query' based on given information, 
        else if RAG is required then the 'answer' field shall be the string that will perform better for RAG search, include any information necessary from any of given information.
        Description: isRAG_Required: is it required to get data from database or perform a RAG call? Note This value is False if more information is needed. Allowed values : true or flase,
        '''

        request_body=[relevantInformationAndQueryStructure,response_format,conversationHistory,PreviouslyViewedProducts,userInformation,query]
        response = self.model.generate_content(request_body)
        return json.loads(response.text)
    def IngestionSummary(self,ProductDetailsJson):
        Instructions="Given Product Details, write a product description. Note: This description is to be written such that Embeddings generated using this description can be used for storing into database which then can be used for efficient and accurate vector searches for RAG implementation. Do not output anything other than product description"
        response = self.model.generate_content([Instructions,ProductDetailsJson])
        return json.loads(response.text)        


obj=InferGemini()
# json.loads(obj.firstInference("what are the shoes that you sell?"))
print(obj.firstInference("what are the shoes that you sell?"))