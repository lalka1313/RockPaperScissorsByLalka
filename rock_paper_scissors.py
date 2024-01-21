
import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_1_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_1_move == "r":
    player_1_move = rock
elif player_1_move == "p":
    player_1_move = paper
elif player_1_move == "s":
    player_1_move = scissors
else:
    raise SystemExit("Invalid Input. Try again ...")

computer_random_number = random.randint(1, 3)
computer_move = " "
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors
print(f"The computer chose {computer_move}.")

if player_1_move == computer_move:
    print("Draw!")
elif player_1_move == rock and computer_move == paper:
    print("You lose")
elif player_1_move == rock and computer_move == scissors:
    print("You win")
elif player_1_move == paper and computer_move == rock:
    print("You win")
elif player_1_move == paper and computer_move == scissors:
    print("You lose")
elif player_1_move == scissors and computer_move == rock:
    print("You lose")
elif player_1_move == scissors and computer_move == paper:
    print("You win")