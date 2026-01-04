import unittest
from datetime import date
from models.patient import Patient
from services.search import (
    search_by_name,
    search_by_disease,
    filter_by_min_age
)

class TestSearchFunctions(unittest.TestCase):

    def setUp(self):
        self.p1 = Patient("Alice Smith", date(2000, 1, 1), ["Asthma"])
        self.p2 = Patient("Bob Jones", date(1980, 6, 15), ["Diabetes"])
        self.patients = [self.p1, self.p2]

    def test_search_by_name(self):
        result = search_by_name(self.patients, "alice")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Alice Smith")

    def test_search_by_disease(self):
        result = search_by_disease(self.patients, "Diabetes")
        self.assertEqual(result[0].name, "Bob Jones")

    def test_filter_by_min_age(self):
        result = filter_by_min_age(self.patients, 40)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Bob Jones")

if __name__ == "__main__":
    unittest.main()
