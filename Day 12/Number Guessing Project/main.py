from art import logo
from random import randint

TURNS = [5,10]

def set_game_as_per_difficulty(user_difficulty_level):
    if user_difficulty_level == 'easy':
        guesses = TURNS[1]
        print(f"You have {guesses} turns")
    else:
        guesses = TURNS[0]
        print(f"You have {guesses} turns")
    return guesses

def check_answer(answer, turns_left):
    guess = int(input("Enter your guess: "))
    while turns_left != 0:
        if guess < answer:
            print("Too low")
            turns_left -= 1
            guess = int(input("Enter your guess: "))
        elif guess > answer:
            print("Too high")
            turns_left -= 1
            guess = int(input("Enter your guess: "))
        elif guess == answer:
            print(f"You Won!!! with {turns_left} turns left. WooHoo...")
            turns_left = 0
    print("Game over!")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm Thinking of a integer number between 1 and 100")
    user_difficulty_level = input("Choose a difficulty: 'Easy' or 'Hard' :").lower()
    turns = set_game_as_per_difficulty(user_difficulty_level)
    random = randint(1,100)
    print(f"Pss...The answer is : {random}")
    check_answer(random, turns)
game()