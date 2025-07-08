import math

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full():
    return all(all(cell != " " for cell in row) for row in board)

def minimax(is_ai):
    if check_winner("X"):
        return 1
    if check_winner("O"):
        return -1
    if is_full():
        return 0

    if is_ai:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(False)
                    board[i][j] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(True)
                    board[i][j] = " "
                    best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "X"

# Game loop
while True:
    print_board()
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if board[row][col] != " ":
        print("Invalid move.")
        continue
    board[row][col] = "O"

    if check_winner("O"):
        print_board()
        print("You win!")
        break
    if is_full():
        print_board()
        print("It's a draw!")
        break

    ai_move()

    if check_winner("X"):
        print_board()
        print("AI wins!")
        break
    if is_full():
        print_board()
        print("It's a draw!")
        break
