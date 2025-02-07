from datetime import datetime

def get_time():
    """Gibt die aktuelle Uhrzeit zurück."""
    now = datetime.now()
    return now.strftime("Es ist %H:%M Uhr.")

def get_date():
    """Gibt das aktuelle Datum zurück."""
    now = datetime.now()
    return now.strftime("Heute ist der %d. %B %Y.")
