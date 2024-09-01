from transformers import FastSpeech2ConformerTokenizer, FastSpeech2ConformerWithHifiGan
import soundfile as sf
import nltk
import time
nltk.download('averaged_perceptron_tagger_eng')
class SpeechHandler:

    def __init__(self) -> None:
        self.modelTTS=FastSpeech2ConformerWithHifiGan.from_pretrained("espnet/fastspeech2_conformer_with_hifigan")
        self.tokenizerTTS=FastSpeech2ConformerTokenizer.from_pretrained("espnet/fastspeech2_conformer")

    def TTS(self,text:str):
        inputs = self.tokenizerTTS(text, return_tensors="pt")
        input_ids = inputs["input_ids"]
        output_dict = self.modelTTS(input_ids, return_dict=True)
        waveform = output_dict["waveform"]
        return waveform
start = time.perf_counter()
print("here")

text="Hello, my dog is cute."
speechHandler=SpeechHandler()
waveform=speechHandler.TTS(text)
print(type(waveform)) # <class 'torch.Tensor'>
sf.write("speech.wav", waveform.squeeze().detach().numpy(), samplerate=22050)
end = time.perf_counter()
ms = (end-start)
print(ms)