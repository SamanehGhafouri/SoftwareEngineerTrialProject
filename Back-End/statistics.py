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
        return math.floor(female_percent * 100) / 100

    def percentage_names_start_with_A_to_M_vs_N_to_Z_helper(self, parts_of_name) -> float:
        count_A_M = 0
        count_N_Z = 0
        for obj in self.json_data["results"]:
            name = obj["name"]
            if re.match(r"^[A-M]", name[parts_of_name][0]):
                count_A_M += 1
            elif re.match(r"^[N-Z]", name[parts_of_name][0]):
                count_N_Z += 1
        percentage_A_M = (count_A_M / (count_A_M + count_N_Z)) * 100
        return math.floor(percentage_A_M * 100) / 100

    def percentage_first_names_start_with_A_to_M_vs_N_to_Z(self) -> float:
        return self.percentage_names_start_with_A_to_M_vs_N_to_Z_helper("first")

    def percentage_last_names_start_with_A_to_M_vs_N_to_Z(self) -> float:
        return self.percentage_names_start_with_A_to_M_vs_N_to_Z_helper("last")

    def top_ten_populous_states_and_total_population(self):
        population_each_state = {}
        total_population = 0
        for obj in self.json_data["results"]:
            total_population += 1
            state = obj["location"]["state"]
            if state in population_each_state:
                population_each_state[state] += 1
            else:
                population_each_state[state] = 1
        top_ten_populous_states = {k: v for k, v in
                                   sorted(population_each_state.items(), key=lambda item: item[1])[-10:]}
        return top_ten_populous_states, total_population

    def percentage_people_in_each_state_top_10_populous_states(self):
        top_ten_populous_states = self.top_ten_populous_states_and_total_population()[0]
        total_population = self.top_ten_populous_states_and_total_population()[1]

        for state, population in top_ten_populous_states.items():
            percentage = (population / total_population) * 100
            top_ten_populous_states[state] = round(percentage, 2)

        other_states = 100 - sum(top_ten_populous_states.values())
        top_ten_populous_states["Others"] = round(other_states, 2)
        return top_ten_populous_states

    def percentage_gender_in_each_state_top_10_helper(self, gender):
        top_ten_populous_states = self.top_ten_populous_states_and_total_population()[0]

        count_female_in_each_state = {}
        for obj in self.json_data["results"]:
            state = obj["location"]["state"]
            if obj["gender"] == gender:
                if state in count_female_in_each_state:
                    count_female_in_each_state[state] += 1
                else:
                    count_female_in_each_state[state] = 1

        percentage_of_gender_in_top_ten = {}
        for key, val in count_female_in_each_state.items():
            if key in top_ten_populous_states:
                percentage = (val / top_ten_populous_states[key]) * 100
                percentage_of_gender_in_top_ten[key] = round(percentage, 2)
        return percentage_of_gender_in_top_ten

    def percentage_females_in_each_state_top_10_populous_states(self):
        return self.percentage_gender_in_each_state_top_10_helper("female")

    def percentage_males_in_each_state_top_10_populous_states(self):
        return self.percentage_gender_in_each_state_top_10_helper("male")

    def percentage_people_in_age_ranges(self):
        group_under_20 = 0
        group_21_40 = 0
        group_41_60 = 0
        group_61_80 = 0
        group_81_100 = 0
        group_100_above = 0
        total_people = len(self.json_data["results"])

        for obj in self.json_data["results"]:
            age = obj["dob"]["age"]
            if age < 21:
                group_under_20 += 1
            elif age < 41:
                group_21_40 += 1
            elif age < 61:
                group_41_60 += 1
            elif age < 81:
                group_61_80 += 1
            elif age < 101:
                group_81_100 += 1
            else:
                group_100_above += 1
        age_range_dict = {"0-20": group_under_20, "21-40": group_21_40, "41-60": group_41_60,
                          "61-80": group_61_80, "81-100": group_81_100, "100+": group_100_above}

        for age_range, groups in age_range_dict.items():
            percentage = (groups / total_people) * 100
            age_range_dict[age_range] = round(percentage, 2)
        return age_range_dict

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
    with open("third_json_data.json", "r") as f:
        data_obj = json.load(f)

        get_json = Statistics(data_obj, "json")
        get_xml = Statistics(data_obj, "xml")
        get_txt = Statistics(data_obj, "txt")

        print(get_json.formatted_response())
        print(get_txt.formatted_response())
        print(get_xml.formatted_response())




