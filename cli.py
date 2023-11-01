from logic import make_empty_board, get_winner, other_player

def display_board(board):
    """Displays the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(cell or " " for cell in row))
        print("-" * 9)

def get_user_move(board, current_player):
    """Gets a valid user move for the given player."""
    while True:
        try:
            row = int(input(f"Player {current_player}, enter the row (0-2): "))
            col = int(input(f"Player {current_player}, enter the column (0-2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] is None:
                return row, col
            else:
                print("Invalid input or that cell is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column values (0-2).")



def play_tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = make_empty_board()
    winner = None
    current_player = "X"

    print("Let's play Tic-Tac-Toe!")

    while winner is None:
        display_board(board)
        row, col = get_user_move(board, current_player)
        board[row][col] = current_player

        # Switch to the next player.
        current_player = other_player(current_player)

        winner = get_winner(board)

        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
        elif all(all(cell is not None for cell in row) for row in board):
            display_board(board)
            print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
