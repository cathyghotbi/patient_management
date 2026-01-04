import unittest
from datetime import date
from models.patient import Patient

class TestPatient(unittest.TestCase):

    def test_age_calculation(self):
        birthdate = date(2000, 1, 1)
        patient = Patient("Alice", birthdate, ["Asthma"])

        expected_age = date.today().year - 2000
        self.assertTrue(patient.age() == expected_age or patient.age() == expected_age - 1)

    def test_to_dict(self):
        birthdate = date(1990, 5, 10)
        patient = Patient("Bob", birthdate, ["Diabetes"])

        data = patient.to_dict()
        self.assertEqual(data["name"], "Bob")
        self.assertEqual(data["birthdate"], "1990-05-10")
        self.assertEqual(data["diseases"], ["Diabetes"])

if __name__ == "__main__":
    unittest.main()
