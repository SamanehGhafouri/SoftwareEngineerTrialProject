import json
from json2xml import json2xml
from json2xml.utils import readfromstring
import math
import re


class Statistics:

    def __init__(self, json_data, file_format: str):
        self.json_data = json_data
        self.file_format = file_format

    def percentage_female_versus_male(self) -> float:
        count_female = 0
        count_male = 0
        for obj in self.json_data["results"]:
            if obj["gender"] == "female":
                count_female += 1
            else:
                count_male += 1
        female_percent = (count_female / (count_male + count_female)) * 100
        return math.floor(female_percent * 10 ** 1) / 10 * 1

    def percentage_first_names_start_with_A_to_M_vs_N_to_Z(self) -> float:
        count_A_M = 0
        count_N_Z = 0
        for obj in self.json_data['results']:
            name = obj['name']
            if re.match(r"^[A-M]", name['first'][0]):
                count_A_M += 1
            elif re.match(r"^[N-Z]", name['first'][0]):
                count_N_Z += 1
        percentage_A_M = (count_A_M / (count_A_M + count_N_Z)) * 100
        return math.floor(percentage_A_M * 10 ** 1) / 10 * 1

    def percentage_last_names_start_with_A_to_M_vs_N_to_Z(self) -> float:
        count_A_M = 0
        count_N_Z = 0
        for obj in self.json_data['results']:
            name = obj['name']
            if re.match(r"^[A-M]", name['last'][0]):
                count_A_M += 1
            elif re.match(r"^[N-Z]", name['last'][0]):
                count_N_Z += 1
        percentage_A_M = (count_A_M / (count_A_M + count_N_Z)) * 100
        return math.floor(percentage_A_M * 10 ** 1) / 10 * 1

    def percentage_people_in_each_state_top_10_populous_states(self) -> float:
        return 40.1

    def percentage_females_in_each_state_top_10_populous_states(self) -> float:
        return 50.1

    def percentage_males_in_each_state_top_10_populous_states(self) -> float:
        return 60.1

    def percentage_people_in_age_ranges(self) -> float:
        return 70.1

    def formatted_response_json(self) -> str:
        stats = {
            "percent_stat_1": self.percentage_female_versus_male(),
            "percent_stat_2": self.percentage_first_names_start_with_A_to_M_vs_N_to_Z(),
            "percent_stat_3": self.percentage_last_names_start_with_A_to_M_vs_N_to_Z(),
            "percent_stat_4": self.percentage_people_in_each_state_top_10_populous_states(),
            "percent_stat_5": self.percentage_females_in_each_state_top_10_populous_states(),
            "percent_stat_6": self.percentage_males_in_each_state_top_10_populous_states(),
            "percent_stat_7": self.percentage_people_in_age_ranges(),
        }
        definitions = {
            "percent_stat_1": "Percentage female versus male",
            "percent_stat_2": "Percentage of first names that start with A-M versus N-Z",
            "percent_stat_3": "Percentage of last names that start with A-M versus N-Z",
            "percent_stat_4": "Percentage of people in each state, up to the top 10 most populous states",
            "percent_stat_5": "Percentage of females in each state, up to the top 10 most populous states",
            "percent_stat_6": "Percentage of males in each state, up to the top 10 most populous states",
            "percent_stat_7": "Percentage of people in the following age ranges: 0-20, 21-40, 41-60, 61-80, 81-100, 100+"
        }
        results = {
            "stats": stats,
            "definitions": definitions
        }
        return json.dumps(results, indent=2)

    def formatted_response_txt(self) -> str:
        percent_stat_1 = "Percentage female versus male"
        percent_stat_2 = "Percentage of first names that start with A-M versus N-Z"
        percent_stat_3 = "Percentage of last names that start with A-M versus N-Z"
        percent_stat_4 = "Percentage of people in each state, up to the top 10 most populous states"
        percent_stat_5 = "Percentage of females in each state, up to the top 10 most populous states"
        percent_stat_6 = "Percentage of males in each state, up to the top 10 most populous states"
        percent_stat_7 = "Percentage of people in the following age ranges: 0-20, 21-40, 41-60, 61-80, 81-100, 100+"

        results = f"{percent_stat_1}: {self.percentage_female_versus_male()}\n" \
                  f"{percent_stat_2}: {self.percentage_first_names_start_with_A_to_M_vs_N_to_Z()}\n" \
                  f"{percent_stat_3}: {self.percentage_last_names_start_with_A_to_M_vs_N_to_Z()}\n" \
                  f"{percent_stat_4}: {self.percentage_people_in_each_state_top_10_populous_states()}\n" \
                  f"{percent_stat_5}: {self.percentage_females_in_each_state_top_10_populous_states()}\n" \
                  f"{percent_stat_6}: {self.percentage_males_in_each_state_top_10_populous_states()}\n" \
                  f"{percent_stat_7}: {self.percentage_people_in_age_ranges()}"
        return results

    def formatted_response_xml(self) -> str:
        json_string = readfromstring(self.formatted_response_json())
        return json2xml.Json2xml(json_string).to_xml()

    def formatted_response(self) -> str:
        if self.file_format == "json":
            return self.formatted_response_json()
        if self.file_format == "txt":
            return self.formatted_response_txt()
        if self.file_format == "xml":
            return self.formatted_response_xml()


if __name__ == "__main__":
    with open("test_data.json", "r") as f:
        data_obj = json.load(f)

        get_json = Statistics(data_obj, "json")
        get_xml = Statistics(data_obj, "xml")
        get_txt = Statistics(data_obj, "txt")

        print(get_json.formatted_response())
        print(get_txt.formatted_response())
        print(get_xml.formatted_response())
