from transformers import BertTokenizer, BertModel

class Embedder:
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained("bert-base-uncased")
    def embed(self,text:str):
        encoded_input = self.tokenizer(text, return_tensors='pt')
        return (self.model(**encoded_input)).last_hidden_state.mean(dim=1).squeeze().tolist()
