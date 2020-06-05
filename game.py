# import modules
import random

# start the game
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Type in your choice:")

# options for the game
options = ["rock", "paper", "scissors"]
robot_choice = random.choice(options)

# results for rock
if user_choice == "rock" and robot_choice == "scissors":
    print("robot choice is:")
    print(robot_choice)
    print("You win!")
elif user_choice == "paper" and robot_choice == "rock":
    print("robot choice is:")
    print(robot_choice)
    print("You win!")
elif user_choice == "scissors" and robot_choice == "paper":
    print("robot choice is:")
    print(robot_choice)
    print("You win!")
elif user_choice == robot_choice:
    print(robot_choice)
    print("draw")
else:
    print("robot choice is:")
    print(robot_choice)
    print("You lose :(")

# logic of the game
