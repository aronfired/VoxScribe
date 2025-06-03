# moduli_trascrizione.py
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio

def trascrivi_audio_wav2vec2(audio_file):
    """
    Trascrive l'audio usando Wav2Vec2 (modello fine-tuned per l'italiano).
    """
    modello_nome = "facebook/wav2vec2-large-xlsr-53-italian"  # Verifica la disponibilità del modello su Hugging Face
    processor = Wav2Vec2Processor.from_pretrained(modello_nome)
    model = Wav2Vec2ForCTC.from_pretrained(modello_nome)
    
    # Carica l'audio
    waveform, sample_rate = torchaudio.load(audio_file)
    if sample_rate != 16000:
        waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
    
    # Prepara l'input per il modello
    input_values = processor(waveform.squeeze().numpy(), return_tensors="pt", sampling_rate=16000).input_values
    # Ottieni il risultato dall'output del modello
    logits = model(input_values).logits
    predicted_ids = logits.argmax(dim=-1)
    testo = processor.decode(predicted_ids[0])
    print("Trascrizione (Wav2Vec2):", testo)
    return testo
