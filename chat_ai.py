import requests
from config import MISTRAL_API_KEY

def ask_ai(prompt):
    """Sendet eine Anfrage an Mistral AI und gibt die Antwort zurück"""
    try:
        url = "https://api.mistral.ai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": "mistral-medium",
            "messages": [{"role": "system", "content": "Du bist Remm eine AI-Assistentin. Du antwortest kurz. Du wurdest von Niklas, am 31. Januar 2025 erschaffen."},
                {"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post(url, json=data, headers=headers)
        response_json = response.json()

        # Debugging: Zeige die gesamte Antwort der API
        #print("🔍 API Response:", response_json)

        # Prüfe, ob das erwartete Feld vorhanden ist
        #if "choices" in response_json and response_json["choices"]:
        return response_json["choices"][0]["message"]["content"]  #Das muss eins nach rechts eingerückt werden wenn ich debuggen will
        #else:
            #return f"Fehlerhafte API-Antwort: {response_json}"
        
    except Exception as e:
        return f"Fehler bei der AI-Anfrage: {e}"
