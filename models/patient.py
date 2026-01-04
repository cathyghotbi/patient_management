from datetime import date

class Patient:
    def __init__(self, name, birthdate, diseases):
        self.name = name
        self.birthdate = birthdate
        self.diseases = diseases

    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )

    def to_dict(self):
        return {
            "name": self.name,
            "birthdate": self.birthdate.isoformat(),
            "diseases": self.diseases
        }
