
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
LANG_ID = "en"
MODEL_ID = "jonatasgrosman/wav2vec2-large-xlsr-53-english"
freq = 16000
SAMPLES = 10


processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
duration=2
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)

# Record audio for the given number of seconds
print("talk")
sd.wait()
inputs = processor(recording, sampling_rate=16000, return_tensors="pt", padding=True)
with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

# predicted_ids = torch.argmax(logits, dim=-1)
# predicted_sentences = processor.batch_decode(predicted_ids)
# print(predicted_sentences)