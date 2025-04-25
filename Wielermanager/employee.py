# --- Werknemers ---
class Employee:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'time_value': 0,   # Hoe waardevol zijn werk was
            'coffee': 0,       # Aantal koffies
            'tires_changed': 0,# Aantal banden
            'returns': 0,      # Aantal terugkomers (lager is beter)
            'service_score': 0,# Klanttevredenheid (0-100)
            'lateness': 0      # Keer te laat
        }

