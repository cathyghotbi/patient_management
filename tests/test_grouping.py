import unittest
from datetime import date
from models.patient import Patient
from services.grouping import group_by_disease

class TestGrouping(unittest.TestCase):

    def test_group_by_disease(self):
        p1 = Patient("Alice", date(2000, 1, 1), ["Asthma"])
        p2 = Patient("Bob", date(1980, 1, 1), ["Asthma", "Diabetes"])

        groups = group_by_disease([p1, p2])

        self.assertIn("Asthma", groups)
        self.assertIn("Diabetes", groups)
        self.assertEqual(len(groups["Asthma"]), 2)
        self.assertEqual(len(groups["Diabetes"]), 1)

if __name__ == "__main__":
    unittest.main()
