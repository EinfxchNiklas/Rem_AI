import time
import threading
import json
from voice import speak

REMINDER_FILE = "reminders.json"

def load_reminders():
    """Lädt gespeicherte Erinnerungen aus einer Datei"""
    try:
        with open(REMINDER_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_reminders(reminders):
    """Speichert Erinnerungen in einer Datei"""
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f)

def add_reminder(text, seconds):
    """Erinnerung speichern und Timer starten"""
    reminders = load_reminders()
    reminder_time = time.time() + seconds
    reminders.append({"text": text, "time": reminder_time})
    save_reminders(reminders)

    threading.Thread(target=reminder_timer, args=(text, seconds)).start()

def reminder_timer(text, seconds):
    """Wartet die angegebene Zeit und erinnert dann den Nutzer"""
    time.sleep(seconds)
    speak(f"Erinnerung: {text}")
    print(f"🔔 Erinnerung: {text}")

    reminders = load_reminders()
    reminders = [r for r in reminders if r["text"] != text]  
    save_reminders(reminders)

def check_reminders():
    """Überprüft gespeicherte Erinnerungen und startet sie automatisch"""
    reminders = load_reminders()
    current_time = time.time()
    for r in reminders:
        remaining_time = r["time"] - current_time
        if remaining_time > 0:
            threading.Thread(target=reminder_timer, args=(r["text"], remaining_time)).start()

def list_reminders():
    """Listet aktuelle Erinnerungen auf"""
    reminders = load_reminders()
    if not reminders:
        return "Du hast keine aktiven Erinnerungen."
    
    reminder_texts = [f"- {r['text']} in {int((r['time'] - time.time()) / 60)} Minuten" for r in reminders]
    return "\n".join(reminder_texts)

def delete_reminder(text):
    """Löscht eine bestimmte Erinnerung"""
    reminders = load_reminders()
    new_reminders = [r for r in reminders if text.lower() not in r["text"].lower()]
    
    if len(new_reminders) < len(reminders):
        save_reminders(new_reminders)
        return f"Die Erinnerung '{text}' wurde gelöscht."
    else:
        return f"Ich konnte keine Erinnerung mit dem Text '{text}' finden."
    
def parse_reminder(user_input):
    """Erkennt Zeitangaben und speichert die Erinnerung"""
    words = user_input.split()
    time_units = {"sekunden": 1, "minute": 60, "minuten": 60, "stunde": 3600, "stunden": 3600}

    for i, word in enumerate(words):
        if word.isdigit() and i + 1 < len(words) and words[i + 1] in time_units:
            seconds = int(word) * time_units[words[i + 1]]
            text = " ".join(words[i + 2:])
            add_reminder(text, seconds)
            return f"Okay, ich erinnere dich in {word} {words[i + 1]} {text}."

    return "Ich konnte die Zeit nicht verstehen."
