# transcriptor

**Transcriptor** is an audio transcription software implemented in Python. This project leverages the [Wav2Vec2](https://huggingface.co/models?pipeline_tag=automatic-speech-recognition) model from Hugging Face to automatically convert audio files (e.g., lecture recordings) into text. It also includes a simple graphical user interface (GUI) built with Tkinter that allows users to verify and correct the transcriptions, saving user feedback for future improvements.

## Features

- **Audio Conversion:** Converts audio files (e.g., MP3) into WAV format with a sample rate of 16 kHz and a single (mono) channel.
- **Noise Reduction:** Applies noise reduction techniques to improve the audio quality before transcription.
- **Wav2Vec2 Transcription:** Uses a fine-tuned Wav2Vec2 model (e.g., `facebook/wav2vec2-large-xlsr-53-italian`) for transcription.
- **Feedback Interface:** Provides a GUI for users to review and correct transcriptions; the feedback is stored in a JSON file.

## Prerequisites

- **Python 3.9+**
- **FFmpeg:** Pydub requires FFmpeg for audio processing.  
  - **Windows:** Install FFmpeg from [this link](https://www.gyan.dev/ffmpeg/builds/), extract it, and add `ffmpeg\bin` to your system PATH.
  - **macOS:** Use Homebrew with `brew install ffmpeg`.
  - **Linux (Ubuntu/Debian):** Install with `sudo apt install ffmpeg`.
- (Optional) **Virtual Environment:** It is recommended to use a virtual environment to manage dependencies.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/transcriptor.git
   cd transcriptor
   
2. **Create and activate a virtual environment:**

On Windows:

   ```bash
  python -m venv env
  env\Scripts\activate
```

On macOS/Linux:

   ```bash
python3 -m venv env
source env/bin/activate
```

3. **Install the dependencies:**

 ```bash
python3 -m venv env
source env/bin/activate
bash
pip install -r requirements.txt
```

Usage
1. Prepare your audio file: place your audio file (for example, lecture.mp3) in the project root directory.
2. Run the application:

```bash
python main.py
```
