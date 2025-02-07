from chat_ai import ask_ai
from voice import speak
#from piper_voice import speak
from speech import listen
from Datums_Zeit_Abfrage import get_time, get_date
from reminders import parse_reminder, list_reminders, delete_reminder, check_reminders
from wetter import get_weather, get_city_coordinates, extract_city_from_text

def main():
    """Hauptprogramm: Wartet auf 'Rem' und antwortet"""
    check_reminders()  # Lädt alte Erinnerungen beim Start

    while True:
        user_input = listen()
        city_name = extract_city_from_text(user_input)
        if user_input:
            if "exit" in user_input or "stop" in user_input:
                print("Rem wird beendet...")
                break

            if "erinnere mich" in user_input.lower():
                response = parse_reminder(user_input)
            elif "welche erinnerungen habe ich" in user_input.lower():
                response = list_reminders()
            elif "lösche erinnerung" in user_input.lower():
                text_to_delete = user_input.replace("lösche erinnerung", "").strip()
                response = delete_reminder(text_to_delete)
            elif "wie spät ist es" in user_input.lower() or "uhrzeit" in user_input.lower():
                response = get_time()
            elif "welches datum ist heute" in user_input.lower() or "datum" in user_input.lower():
                response = get_date()
            elif city_name:
                city = get_city_coordinates(city_name)

                if city:
                    response = get_weather(city)
                else:
                    response = "Ich konnte die Stadt nicht finden."            
            else:
                response = ask_ai(user_input)

            print("Rem:", response)
            speak(response) #TTS Ausgabe der Antwort

if __name__ == "__main__":
    main()