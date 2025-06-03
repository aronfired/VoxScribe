# main.py
from moduli_audio import converti_audio, riduci_rumore
from moduli_trascrizione import trascrivi_audio_wav2vec2
from moduli_feedback import feedback_interface, salva_feedback_file

def main():
    # 1. Conversione dell'audio (es. da MP3 a WAV)
    wav_file = converti_audio("lezione.mp3")
    
    # 2. Riduzione del rumore
    wav_clean = riduci_rumore(wav_file)
    
    # 3. Trascrizione usando Wav2Vec2
    trascrizione = trascrivi_audio_wav2vec2(wav_clean)
    if trascrizione is None:
        print("Impossibile ottenere la trascrizione. Controlla il file audio o i parametri.")
        return
    
    # 4. Raccolta del Feedback
    feedback_interface(trascrizione, salva_feedback_file)
    
    print("Elaborazione completata.")

if __name__ == "__main__":
    main()
