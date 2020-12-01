# Boris Paul Pizha  
# Simple Game Project 

# User Name
user = "Boris Pizha"

# Printing a welcome for user
print("\n Rock Paper Scissors game in Python by " + user)

# Importing Randit so user 
from random import choice, randint


def randomint():
    return randint(1, 3)

# Choice for users to play game
def choice_string(choice):
    if choice == 0:
        return 'Quit'
    elif choice == 1:
        return 'Scissor'
    elif choice == 2:
        return 'Rock'
    else:
        return 'Paper'
    
    

def main():
    # Validation 
    while True:
        try:
            # User will play againt computer that will get random numbers from list the next line 
            computer_choice = randomint()
            # User choice To start the game
            user_choice = int(input('\n\n Here are your options: \n 0. quit \n 1.Rock \n 2.Paper \n 3.Scissors' '\n Please enter your choice: '))

            # If Computer choice and user choice are the same there will be a tie 
            if (computer_choice == 1 and user_choice == 1) or (computer_choice == 2 and user_choice == 2) or (computer_choice == 3 and user_choice == 3):
                print('\n The computer choice is: ', computer_choice)
                print("\n There is a TIE")
                # User Will get a message every time there is a Tie 
                if computer_choice == user_choice:
                    print("\n Please try Again! ")
      

            # Computer will win if it gets the right choice 
            elif (computer_choice == 1 and user_choice == 3) or (computer_choice == 2 and user_choice == 1) or (computer_choice == 3 and user_choice == 2):
                print('\n The computer choice is:', computer_choice)
                print("\n Computer WON. You Lost ")
        
            # Or user will win intead 
            elif (computer_choice == 3 and user_choice == 1) or (computer_choice == 1 and user_choice == 2) or (computer_choice == 2 and user_choice == 3):
                print('\n The computer choice is: ', computer_choice)
                print("\n CONGRATS You WON " + user)
            # Quiting application by hitting 0

            elif (user_choice == 0):
                print("\n See you Later ")
                break
                
            # Validation and will display message to enter a valid entry
            else:
                raise ValueError()
        except:
            print("\n Enter valid input from User Choice List\n ")

main()

