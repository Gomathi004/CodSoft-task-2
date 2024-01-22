import copy

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != '-' for i in range(3) for j in range(3))

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    scores = {
        'X': 1,
        'O': -1,
        'tie': 0
    }

    if check_winner(board, 'X'):
        return scores['X']
    elif check_winner(board, 'O'):
        return scores['O']
    elif is_board_full(board):
        return scores['tie']

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '-'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    best_score = min(score, best_score)
        return best_score

# Function for the AI's move using Minimax
def ai_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = 'X'

# Function to play the game
def play_game():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'O'

    while True:
        print_board(board)

        if current_player == 'O':
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != '-':
                print("Invalid move. Try again.")
                continue
            board[row][col] = 'O'
        else:
            ai_move(board)

        if check_winner(board, 'O'):
            print("Congratulations! You won!")
            break
        elif check_winner(board, 'X'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

play_game()