print("Enter Player 1's choice")
player1_choice = input()
print("Enter Player 2's choice")
player2_choice = input()
if player1_choice == "rock" and player2_choice == "scissors":
    print("Player 1 wins")
elif player1_choice == "scissors" and player2_choice == "paper":
    print("Player 1 wins")
elif player1_choice == "paper" and player2_choice == "rock":
    print("Player 1 wins")
elif player1_choice == player2_choice:
    print("Its a tie!")
else:
    print("Player 2 wins")