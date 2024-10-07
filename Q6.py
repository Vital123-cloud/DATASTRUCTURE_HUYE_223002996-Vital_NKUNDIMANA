# Create a 3x3 tic-tac-toe board initialized with empty spaces
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check for a winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Example game play
board[0][0] = 'X'
board[0][1] = 'X'
board[0][2] = 'X'  # X wins
print_board()
winner = check_winner()

if winner:
    print(f"The winner is: {winner}")
else:
    print("No winner yet.")
