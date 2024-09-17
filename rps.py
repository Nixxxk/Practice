import random
user_choice = int(input("Enter your choice: Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors \n"))

if user_choice <0 or user_choice > 2:
    print("You entered the wrong input hence you loose buddy.")
else:
    computer_choice = random.randint(0,2)
    print("Computer choose: ")
    print(computer_choice)
    if computer_choice == user_choice:
        print("Its Draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif user_choice > computer_choice:
       print("You win.")
    elif user_choice < computer_choice:
        print("You loose.")



