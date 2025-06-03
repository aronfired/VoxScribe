from pydub import AudioSegment
import noisereduce as nr
import soundfile as sf

def converti_audio(input_file, output_file="lezione.wav"):
    """
    Converte un file audio (ad esempio MP3) in WAV a 16 kHz e in modalità mono.
    """
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_file, format="wav")
    print(f"Conversione completata: {output_file}")
    return output_file

def riduci_rumore(input_wav, output_wav="lezione_clean.wav"):
    """
    Applica una riduzione del rumore al file WAV.
    """
    data, rate = sf.read(input_wav)
    data_clean = nr.reduce_noise(y=data, sr=rate)
    sf.write(output_wav, data_clean, rate)
    print(f"Riduzione del rumore completata: {output_wav}")
    return output_wav
