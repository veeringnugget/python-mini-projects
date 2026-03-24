""" Contains code pertaining to handling API call and response """

import requests

# Initialise difficulty
def get_difficulty():
    difficulty_dict = {1 : 'easy', 2 : 'medium', 3 : 'hard', 4 : 'any'}
    difficulty = int(input("Select difficulty (1, 2, 3 or 4):\n" \
    "1. Easy\n2. Medium\n3. Hard\n4. Any\n> "))
    return difficulty_dict[difficulty].lower()

# Initialise question type
def get_question_type():
    type_dict = {1 : 'multiple', 2 : 'boolean', 3 : 'any'}
    type = int(input("Select type of questions (1, 2 or 3):\n" \
    "1. Multiple choice\n2. True or False\n3. Any\n> "))
    return type_dict[type].lower()

# Build formatted string
def build_api_string(BASE_URL, difficulty, question_type):
    # both "any"
    if difficulty == "any" and question_type == "any":
        return BASE_URL
    # difficulty = "any", question_type != any
    elif difficulty == "any" and question_type != "any":
        return f"{BASE_URL}&type={question_type}"
    # difficulty != any, question_type = "any"
    elif difficulty != "any" and question_type == "any":
        return f"{BASE_URL}&difficulty={difficulty}"
    # both != any
    else:
        return f"{BASE_URL}&difficulty={difficulty}&type={question_type}"

def run_api(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error. Status Code {response.status_code}")
    return response.json()