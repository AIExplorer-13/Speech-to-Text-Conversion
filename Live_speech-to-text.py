import speech_recognition as sr
import pyttsx3 


def record_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source2, duration=1)
            print("Listening...")
            try:
                audio2 = r.listen(source2, timeout=5, phrase_time_limit=10)  # Set timeout and phrase time limit
                print("Processing...")
                text = r.recognize_google(audio2)
                print(text)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
    except KeyboardInterrupt:
        print("Recording interrupted by user")
    return None

txt = record_text()
