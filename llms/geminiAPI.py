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
    def summary(self,ProductDetailsJson:str):
        Instructions="Given Product Details, write a product description. Note: This description is to be written such that Embeddings generated using this description can be used for storing into database which then can be used for efficient and accurate vector searches for RAG implementation. Do not output anything other than product description"
        Instructions='''
        About Query: This query is to generate augmented data for a single product. The augmented data is to be used to convert it into embeddings which will perform efficiently on retrival tasks.
        System: This is an agent on a e-commerce website which augments data based on given rules for a single product, Output format is as mentioned below and product details will be given in a JSON format at the end of this query.
        Rules:
        1)Remove unnecessary words and characters: Eliminate any words or characters that do not add value to the product information.
        2)Restructure data: If necessary, reorganize the information into a more concise and informative format.
        3)Generate augmented versions: Create variations of the product name, description, and other relevant fields while preserving the core meaning and every augmented version should be appended as a new string in output list.
        4)Maintain consistency: Ensure that the augmented data remains consistent with the original product information.
        5)Remove web-addresses: Remove all the web-addresses and any information associated with them
        6)Augmented Versions Limit: Limit Augmented versions to 4 and try to maximize the difference between these version
        Output:
        1)The output shall be a list of string of augmented data and no other information.
        2) Try to keep the output as small as possible while following the rules.
        
        '''
        response = self.model.generate_content([Instructions,ProductDetailsJson])
        return response.text       

    def query_restructure(self,query:str):
        Instructions='''
        About Query: This query is to generate augmented data for a single product. The augmented data is to be used to convert it into embeddings which will perform efficiently on retrival tasks.
        System: This is an agent on a e-commerce website which augments data based on given rules for a single product, Output format is as mentioned below and product details will be given in a JSON format at the end of this query.
        Rules:
        1)Remove unnecessary words and characters: Eliminate any words or characters that do not add value to the product information.
        2)Restructure data: If necessary, reorganize the information into a more concise and informative format.
        3)Generate augmented versions: Create variations of the product name, description, and other relevant fields while preserving the core meaning and every augmented version should be appended as a new string in output list.
        4)Maintain consistency: Ensure that the augmented data remains consistent with the original product information.
        5)Remove web-addresses: Remove all the web-addresses and any information associated with them
        6)Augmented Versions Limit: Limit Augmented versions to 4 and try to maximize the difference between these version
        Output:
        1)The output shall be a list of string of augmented data and no other information.
        2) Try to keep the output as small as possible while following the rules.
        
        '''
        response = self.model.generate_content([Instructions,query])
        return response.text       


# obj=InferGemini()
# # json.loads(obj.firstInference("what are the shoes that you sell?"))
# print(obj.firstInference("what are the shoes that you sell?"))