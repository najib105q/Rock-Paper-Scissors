import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("=== Rock Paper Scissors ===\n")

while True:
    rounds = int(input("Best of how many rounds? (must be an odd number): "))

    if rounds % 2 == 1:
        break

    print("Please enter an odd number.")
    
to_reach = rounds // 2 + 1

while player_score < to_reach and computer_score < to_reach:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Draw!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score: You {player_score} - {computer_score} Computer")

print("\n=== Game Over ===")
if player_score > computer_score:
    print("You won the match!")
else:
    print("Computer won the match!")