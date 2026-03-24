""" Contains code pertaining to handling API call and response """
"""
TODO:
1. Find out difficulty from the user
2. Find out type of question (Bool or Multiple Choice)
3. Build formatted string
4. API call
5. Check response
"""

# Base URL for quiz API
BASE_URL = 'https://opentdb.com/api.php?amount=10'

# Initialise difficulty
def get_difficulty():
    return input("Select difficulty (1, 2, 3 or 4):\n" \
    "1. Easy\n2. Medium\n3. Hard\n4. Any\n> ")

# Initialise question type
def get_question_type():
    return input("Select type of questions (1, 2 or 3):\n" \
    "1. Multiple choice\n2. True / False\n3. Any\n> ")


