import subprocess
import os
from config import PIPER_PFAD, STIMMEN_PFAD
# Konfiguration: Passe den Pfad zu Piper und dem Modell an

OUTPUT_FILE = "output.wav"  # Name der Audio-Datei

def speak(text):
    """
    Konvertiert Text in Sprache mit Piper und spielt die generierte Audio-Datei ab.
    """
    if not os.path.exists(PIPER_PFAD):
        print("Fehler: Piper wurde nicht gefunden. Überprüfe den Pfad.")
        return
    
    if not os.path.exists(STIMMEN_PFAD):
        print("Fehler: Stimmenmodell wurde nicht gefunden. Überprüfe den Pfad.")
        return

    try:
        # Piper-Befehl ausführen
        command = f'echo "{text}" | "{PIPER_PFAD}" --model "{STIMMEN_PFAD}" --output-file "{OUTPUT_FILE}"'
        subprocess.run(command, shell=True, check=True)

        # Die generierte Audio-Datei abspielen
        subprocess.run(f'start {OUTPUT_FILE}', shell=True)  # Für Windows
    except Exception as e:
        print(f"Fehler: {e}")
