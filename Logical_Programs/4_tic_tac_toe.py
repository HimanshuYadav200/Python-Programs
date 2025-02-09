def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  

def is_draw(board):
    
    for row in board:
        for cell in row:
            if cell == " ":
                return False  
    return True  


board = [[" " for _ in range(3)] for _ in range(3)]

print("Tic Tac Toe Game!")
print_board(board)

players = ["X", "O"]
turn = 0

while True:
    print(f"Player {players[turn % 2]}'s turn.")
    
 
    row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())

 
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = players[turn % 2]
        turn += 1
    else:
        print("Invalid move, try again!")
        continue

    print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
        break

 
    if is_draw(board):
        print("It's a draw!")
        break
