import unittest
from statistics import Statistics
import json

first_json = "first_json_data.json"
second_json = "second_json_data.json"
third_json = "third_json_data.json"


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class Test(unittest.TestCase):

    def test_percentage_female_vs_male(self):
        stat = Statistics(read_json(first_json), "json")
        actual = stat.percentage_female_versus_male()
        expected = 85.71
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_first_names_start_with_A_to_M_vs_N_to_Z(self):
        stat = Statistics(read_json(first_json), "json")
        actual = stat.percentage_first_names_start_with_A_to_M_vs_N_to_Z()
        expected = 71.42
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_last_names_start_with_A_to_M_vs_N_to_Z(self):
        stat = Statistics(read_json(first_json), "json")
        actual = stat.percentage_last_names_start_with_A_to_M_vs_N_to_Z()
        expected = 28.57
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_people_in_each_state_top_10_populous_states(self):
        stat = Statistics(read_json(second_json), "json")
        actual = stat.percentage_people_in_each_state_top_10_populous_states()
        expected = {"New York": 18.33, "Bayern": 16.67, "Galway": 15.00, "Baden": 13.33, "Rioja": 11.67,
                    "Colorado": 8.33, "Marlborough": 6.67, "Ceuta": 5.00, "Bay": 3.33, "Brooklyn": 1.67, "Others": 0.00}
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_people_in_each_state_top_10_populous_states_second_test(self):
        stat = Statistics(read_json(third_json), "json")
        actual = stat.percentage_people_in_each_state_top_10_populous_states()
        expected = {"New York": 18.03, "Bayern": 16.39, "Galway": 14.75, "Baden": 13.11, "Rioja": 9.84,
                    "Colorado": 8.20, "Marlborough": 6.56, "Ceuta": 4.92, "Bay": 3.28, "Brooklyn": 3.28, "Others": 1.64}
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_females_in_each_state_top_10_populous_states(self):
        stat = Statistics(read_json(third_json), "json")
        actual = stat.percentage_females_in_each_state_top_10_populous_states()
        expected = {"New York": 36.36, "Bayern": 60.00, "Galway": 44.44, "Baden": 62.5, "Rioja": 66.67,
                    "Colorado": 40.00, "Marlborough": 25.00, "Bay": 50.00, "Brooklyn": 100.00}
        self.assertEqual(expected, actual, expected == actual)

    def test_percentage_males_in_each_state_top_10_populous_states(self):
        stat = Statistics(read_json(third_json), "json")
        actual = stat.percentage_males_in_each_state_top_10_populous_states()
        expected = {"New York": 63.64, "Bayern": 40.00, "Galway": 55.56, "Baden": 37.50, "Rioja": 33.33,
                    "Colorado": 60.00, "Marlborough": 75.00, "Bay": 50.00, "Ceuta": 100.00}
        self.assertEqual(expected, actual, expected == actual)


if __name__ == '__main__':
    unittest.main()

