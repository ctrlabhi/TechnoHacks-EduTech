# Tic Tac Toe game in Python

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win
def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

# Function to check for a tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[row][col] != " ":
                print("This position is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_player

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
