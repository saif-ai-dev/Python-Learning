import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()


print("Computer Choices:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("Computer wins!")

elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("Computer wins!")

elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid input! please choose rock, paper, or scissors.")