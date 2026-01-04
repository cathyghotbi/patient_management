import json
import csv

def save_to_json(groups, filename):
    data = {
        disease: [p.to_dict() for p in patients]
        for disease, patients in groups.items()
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_to_csv(groups, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Disease", "Name", "Birthdate", "Age"])
        for disease, patients in groups.items():
            for p in patients:
                writer.writerow([
                    disease,
                    p.name,
                    p.birthdate.isoformat(),
                    p.age()
                ])
