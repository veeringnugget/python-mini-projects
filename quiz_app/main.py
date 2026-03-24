import quiz_api

# Base URL for quiz API
BASE_URL = 'https://opentdb.com/api.php?amount=10'

# Initialise questions and call API
difficulty = quiz_api.get_difficulty()
question_type = quiz_api.get_question_type()