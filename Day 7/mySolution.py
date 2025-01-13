import random
from art import stages, logo

print("Let's Play Hangman. Guess a character of a random word.")
print(logo)
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
wl = len(chosen_word)
print(chosen_word)

chosen_word_list = list(chosen_word)
nGuess = 6
game_over = True
correctly_guessed = []
print("_" * wl)
while nGuess > 0:

    display = ''
    guess = input(f"\nGuess a letter. You have {nGuess} lives: ").lower()

    if guess in correctly_guessed:
        print(f"You've already guessed {guess}")

    for each in chosen_word_list:
        if each == guess:
            correctly_guessed.append(each)
            display += each
        elif each in correctly_guessed:
            display += each
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        nGuess -= 1
        print(f"Incorrect guess. Lives left: {nGuess}")
        
        if nGuess == 0:
            print(f"You loose. Correct word is {chosen_word}")

    if "_" not in display:
        print("You won! Well done!")
        break
    print(stages[nGuess])

