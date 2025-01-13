import random
from randomSelection import rock,paper,scissors

game = True
while(game):

    game = input('Do you want to play?: y or n : ').lower()
    
    if game != 'y':
        game = False
        
    else: #TODO- Try Catch block for invalid inputs
        user_choice = int(input('Choose : 1 = Rock or 2 = Paper or 3 = Scissor : '))

        if user_choice not in range(1,4) :
            print("Enter valid choice. Choose : 1 = Rock or 2 = Paper or 3 = Scissor ")
        else:
            computer_choice = random.randint(1,3)
            game_images = [rock,paper,scissors]
            print(game_images[computer_choice - 1])
            

            if computer_choice == user_choice:
                print("Tie!!! Play again.")
            elif (user_choice == 1 and computer_choice == 3):
                print("You won! yay!")
            elif (user_choice == 2 and computer_choice == 1):
                print("You won! yay!")
            elif (user_choice == 3 and computer_choice == 2):   
                print("You won! yay!")
            else:
                print("Computer won! LoOSER!")
