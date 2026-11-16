# Ask the user to enter their move
# If choice is not valid
#   Print a error
# Let computer randomly choose a move
# Print choices using emojis
# Determine the winner
# Ask the user if they want to play again
# If not
#   Terminate


import random


move = input("Rock, Paper, or Scissors?(r/p/s) ")
if move not in ['r', 'p', 's']:
    print("Invalid input. Please choose 'r', 'p', or 's'.")

# Let computer randomly choose a move
computer_move = random.choice(['r', 'p', 's'])

# Print choices using emojis
emojis = {'r': '✊', 'p': '✋', 's': '✌️'}
print(f"You chose: {emojis[move]}")
print(f"Computer chose: {emojis[computer_move]}")

# Determine the winner
if move == computer_move:
    print("It's a tie!")
elif (move == 'r' and computer_move == 's') or \
     (move == 'p' and computer_move == 'r') or \
     (move == 's' and computer_move == 'p'):
    print("You win!")
else:
    print("You Lose.")
