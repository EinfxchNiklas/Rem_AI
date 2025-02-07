import speech_recognition as sr

def listen():
    """Hört auf Sprache und gibt den erkannten Text zurück"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Zuhören...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="de-DE")
            print(f"Du: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return "Ich konnte keine Verbindung zur Spracherkennung herstellen."
