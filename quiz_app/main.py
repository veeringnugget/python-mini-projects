import quiz_api
from html import unescape
from random import shuffle

# Shuffle the answers randomly
def shuffle_answers(response, q):
    choices = []
    # Append correct answer to list
    choices.append(response["results"][q]["correct_answer"])
    # Append incorrect answers to list
    for ans in response["results"][q]["incorrect_answers"]:
        choices.append(ans)
    # Shuffle the list randomly
    shuffle(choices)
    return choices
    

# Base URL for quiz API
BASE_URL = 'https://opentdb.com/api.php?amount=10'

# Initialise questions and call API
difficulty = quiz_api.get_difficulty()
question_type = quiz_api.get_question_type()
API_URL = quiz_api.build_api_string(BASE_URL, difficulty, question_type)
response = quiz_api.run_api(API_URL)

# Loop quiz
for q in range(10):
    # Print question
    print(f"Q{q + 1}: {unescape(response["results"][q]["question"])}")
    # Merge and print answers
    choices = shuffle_answers(response, q)
    option = 1
    for choice in choices:
        print(f"{option}: {choice}")
        option +=1
    # Have user guess answer
    answer = input("Type out your answer - {option}: > ").lower()
    correct_answer = response["results"][q]["correct_answer"].lower()
    # Check response
    if answer == correct_answer:
        print("Well done!")
    else:
        print(f"Sorry, the answer was {correct_answer}")



