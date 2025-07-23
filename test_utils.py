# test_utils.py
import unittest
from utils import load_data, calculate_bmi_stats, get_top_patients_by_bmi

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.df = load_data()

    def test_load_data(self):
        self.assertFalse(self.df.empty)
        self.assertIn("BMI", self.df.columns)

    def test_calculate_bmi_stats(self):
        stats = calculate_bmi_stats(self.df)
        self.assertIn("Mean BMI", stats)
        self.assertGreater(stats["Max BMI"], stats["Min BMI"])

    def test_top_patients_by_bmi(self):
        top = get_top_patients_by_bmi(self.df, top_n=3)
        self.assertEqual(len(top), 3)
        self.assertTrue((top["BMI"].diff().dropna() <= 0).all())  # check descending order

if __name__ == '__main__':
    unittest.main()
