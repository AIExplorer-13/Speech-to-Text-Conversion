import whisper
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Explicitly specify the path to ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-master-latest-win64-gpl\bin"

try:
    print("Getting into Model")
    model = whisper.load_model("base")
    print("Model Loaded")

    result = model.transcribe(r"C:\Users\vidya\OneDrive\Desktop\Prodian-infotech\Inbuilt\audio.mp3")
    print("Transcription completed successfully.")

    with open("transcription_mp3.txt", "w") as f:
        print("Writing transcription to file.")
        f.write(result["text"])

    print("Done")
except Exception as e:
    print(f"An error occurred: {e}")
