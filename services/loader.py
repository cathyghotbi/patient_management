import json
from datetime import datetime
from models.patient import Patient

def load_patients(filename):
    patients = []
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for p in data:
            birthdate = datetime.strptime(p["birthdate"], "%Y-%m-%d").date()
            patients.append(Patient(p["name"], birthdate, p["diseases"]))
    return patients
