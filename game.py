# import modules
import random

# start the game
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Type in your choice:")

# options for the game
options = ["rock", "paper", "scissors"]
robot_choice = random.choice(options)

# user results
if user_choice == "rock" and robot_choice == "scissors":
    print(f"robot choice is: {robot_choice}")
    print("You win!")
elif user_choice == "paper" and robot_choice == "rock":
    print(f"robot choice is: {robot_choice}")
    print("You win!")
elif user_choice == "scissors" and robot_choice == "paper":
    print(f"robot choice is: {robot_choice}")
    print("You win!")
elif user_choice == robot_choice:
    print(f"robot choice is: {robot_choice}")
    print("draw")
else:
    print(f"robot choice is: {robot_choice}")
    print("You lose :(")
