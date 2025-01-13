from myArt import chest

print("Welcome to The Treasure Island! Your mission is to find the treasure.")
print(f"{chest}")
choice1 = input("You're at a cross road. Where do you want to go? Right or left?: ").lower()
if choice1 == 'left':
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake."
                    'Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors."
                        " One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == 'yellow':
            print("You won! Enjoy the treasure!")
        elif choice3 == 'red':
            print('Burned by fire, Game over!')
        elif choice3 == 'blue':
            print('Eaten by beasts, Game over!')
        else:
            print('Game over!')
    else:
        print("You're attacked by a trout. Game over!")

else:
    print("You fell into a hole. Game over!")
