
"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Alice Kočířová
email: a.kocirova@gmail.com
"""

print("\n".join([
    "Welcome to Tic Tac Toe",
    "=" * 40,
    "GAME RULES:",
    "Each player can place one mark (or stone) per turn on the 3x3 grid.",
    "The WINNER is the player who succeeds in placing three of their marks",
    "in a horizontal, vertical, or diagonal row.",
    "=" * 40,
    "Let´s start the game"
]))

# Creating a playing field
board = [" " for _ in range(9)]

# Display the playing field
def display_board():
    print("+---+---+---+")
    for i in range(3):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print("+---+---+---+")

# Victory check
def check_winner():
    winning_combinations = [
        # Horizontally
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Vertically
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonally
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if all(board[i] == current_player for i in combo):
            return True
    return False

# First player
current_player = "O"

# The main game
while True:
    print("=" * 40)
    # Displaying the state of the playing field
    display_board()
    position = input(f"Player {current_player} | Please enter your move number (1-9): ")

    # Entry control
    if not position.isdigit():
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    position = int(position) - 1

    if position < 0 or position >= 9:
        print("Out of range. Please choose a number between 1 and 9.")
        continue

    if board[position] != " ":
        print("Position already taken. Choose another field.")
        continue

    board[position] = current_player

    # Victory check
    if check_winner():
        print("=" * 40)
        display_board()
        print(f"Congratulations, the player {current_player} WON!")
        print("=" * 40)
        break

    # Draw check
    if all(cell != " " for cell in board):
        print("=" * 40)
        display_board()
        print("It’s a draw! Well played both players.")
        print("=" * 40)
        break

    # Another player
    current_player = "X" if current_player == "O" else "O"