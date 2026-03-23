import random

# CPU selects one of the options randomly
def cpu_selection():
    choices = {1 : 'r', 2 : 'p', 3 : 's'}
    random_number = random.randrange(1, 4)
    return choices[random_number]

# Find out who won each round
def find_winner(user, cpu):
    if user == 'r' and cpu == 'p':
        return 'user'
    elif cpu == 'r' and user == 'p':
        return 'cpu'
    elif user == 'p' and cpu == 's':
        return 'user'
    elif cpu == 'p' and user == 's':
        return 'cpu'
    elif user == 's' and cpu == 'r':
        return 'user'
    elif cpu == 's' and user == 'r':
        return 'cpu'
    elif user == 'r' and cpu == 'r':
        return 'draw'
    elif user == 'p' and cpu == 'p':
        return 'draw'
    elif user == 's' and cpu == 's':
        return 'draw'
    
# Print how many rounds user wants to play - check errors later
rounds = int(input("How many rounds would you like to play?: "))

# Declare score variabes
user_score = 0
cpu_score = 0

for round in range(rounds):
    # User enters rock, paper or scissors
    user_selection = input("Type (r) rock, (p) paper or (s) scissors: ")

    # Computer selects rock, paper or scissors
    cpu_result = cpu_selection()
    
    # Find the winner of the round
    winner = find_winner(user_selection, cpu_result)

    # Add one point to winner
    if winner == 'user':
        user_score += 1
    elif winner == 'cpu':
        cpu_score += 1

    # Print Scoreline
    print("---- SCORE ----")
    print(f"Winner: {winner} - User Score: {user_score} / CPU Score: {cpu_score}")

if user_score > cpu_score:
    print("You win!")
elif cpu_score > user_score:
    print("You lose!")
else:
    print("It's a draw")

    
    




