import pyttsx3

def speak(text):
    """Verwandelt den übergebenen Text in Sprache"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Geschwindigkeit der Sprache
        engine.setProperty('volume', 1)  # Lautstärke (zwischen 0 und 1)
        engine.setProperty('voice', 'german')  # Stelle sicher, dass du die deutsche Stimme wählst
        engine.say(text)
        engine.runAndWait()
        #print(f"Gesprochen: {text}")
    except Exception as e:
        print(f"Fehler beim Sprechen: {e}")