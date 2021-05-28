import unittest
from statistics import Statistics
import json


first_json = "first_json_data.json"


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class Test(unittest.TestCase):

    def test_percentage_female_vs_male(self):
        stat = Statistics(read_json(first_json), 'json')
        actual = stat.percentage_female_versus_male()
        expected = 85.71
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_first_names_start_with_A_to_M_vs_N_to_Z(self):
        stat = Statistics(read_json(first_json), 'json')
        actual = stat.percentage_first_names_start_with_A_to_M_vs_N_to_Z()
        expected = 71.42
        self.assertEqual(expected, actual, expected == actual)


if __name__ == '__main__':
    unittest.main()