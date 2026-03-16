import random

def play_game():
    random_number = randomiser()
    guesses = get_guesses()
    take_guesses(random_number, guesses)


def randomiser():
    return int(random.random() * 100)

def get_guesses():
    while True:
        try:
            guesses = int(input("Pick how many guesses you'd like between 1 and 10: "))
            if guesses < 0 or guesses > 10:
                print("Oops! Please choose a number between 1 and 10...")
            else:
                return guesses
        except ValueError:
            print("Oops! Please enter a valid number...")

def take_guesses(random, guesses):
    for x in range(guesses):
        guesses_left = guesses - x
        if guesses > 1:
            print(f"You have {guesses_left} guesses left.")
        else:
            print(f"You have {guesses_left} guess left.")
        guess = int(input("Guess: "))
        if guess > random:
            print("Too high! Try lower.")
        elif guess < random:
            print("Too low! Try higher.")
        elif guess == random:
            print("Well done, you guessed correctly!")
            return
    print(f"Better luck next time, the answer was {random}")

play_game()