import re
import random

choice_array = ['r', 'p', 's']

while(1):
    print("Please make a selection: ");
    print("Rock(R)    Paper(P)    Scissors(S)    Quit(Q)");
    player_choice = input("Choice: ").strip().lower()

    if not (len(player_choice) == 1 and re.match(r'[rpsq]', player_choice)):
        print("Please enter a valid option!!")
        continue

    if(player_choice == "q"):
        print("Thanks for playing!!")
        break

    comp_choice = choice_array[random.randint(0,2)]
    #print(comp_choice)

    if(player_choice == comp_choice):
        print("Draw!!")
        continue

    if(player_choice == 'r'):
        if(comp_choice == 'p'):
            print("Computer chooses paper. Computer wins!!")
        else:
            print("Computer chooses scissors. You win!!")
    if(player_choice == 'p'):
        if (comp_choice == 'r'):
            print("Computer chooses rock. You win!!")
        else:
            print("Computer chooses scissors. Computer wins!!")
    if (player_choice == 's'):
        if (comp_choice == 'r'):
            print("Computer chooses rock. Computer wins!!")
        else:
            print("Computer chooses paper. You win!!")

    print("\n\n")