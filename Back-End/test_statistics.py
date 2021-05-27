import unittest
from statistics import Statistics
import json


female_vs_male_json = "test_percentage_female_vs_male.json"


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class Test(unittest.TestCase):

    def test_percentage_female_vs_male(self):
        stat = Statistics(read_json(female_vs_male_json), 'json')
        actual = stat.percentage_female_versus_male()
        expected = 85.71
        self.assertEqual(expected, actual, expected == actual)


if __name__ == '__main__':
    unittest.main()