""" Contains code pertaining to handling API call and response """

"""
TODO:
1. Build formatted string
2. API call
3. Check response
"""

# Initialise difficulty
def get_difficulty():
    difficulty_dict = {1 : 'easy', 2 : 'medium', 3 : 'hard', 4 : 'any'}
    difficulty = int(input("Select difficulty (1, 2, 3 or 4):\n" \
    "1. Easy\n2. Medium\n3. Hard\n4. Any\n> "))
    return difficulty_dict[difficulty]

# Initialise question type
def get_question_type():
    type_dict = {1 : 'multiple choice', 2 : 'bool', 3 : 'any'}
    type = int(input("Select type of questions (1, 2 or 3):\n" \
    "1. Multiple choice\n2. True or False\n3. Any\n> "))
    return type_dict[type]

# Build formatted string
def build_api_string(BASE_URL, difficulty, question_type):
    pass


