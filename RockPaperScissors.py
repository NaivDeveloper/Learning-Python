# Simple Rock Paper Scissors game i made from scratch without any help from tutorials

import random

player = input("You're name: ")
choice = input("Rock, paper, scissors! ").lower()
choice_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice_options)

if (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):
   print( f"{player} chose {choice} and computer chose {computer_choice}. You win!")
elif choice == computer_choice:
   print( f"{player} chose {choice} and the computer chose {computer_choice}. Its a tie!")
else:
   print( f"{player} chose {choice} and the computer chose {computer_choice}. You lose!")