import unittest
import json
import os
from services.loader import load_patients

class TestLoader(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_patients.json"
        data = [
            {
                "name": "Test User",
                "birthdate": "2000-01-01",
                "diseases": ["Flu"]
            }
        ]
        with open(self.test_file, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def tearDown(self):
        os.remove(self.test_file)

    def test_load_patients(self):
        patients = load_patients(self.test_file)
        self.assertEqual(len(patients), 1)
        self.assertEqual(patients[0].name, "Test User")

if __name__ == "__main__":
    unittest.main()
