def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()
def is_safe(board, row, col):
    n = len(board)
    return all(
        board[i][col] == 0 for i in range(row)
    ) and all(
        board[i][j] == 0 
        for i, j in zip(range(row, -1, -1), range(col, -1, -1))
    ) and all(
        board[i][j] == 0 
        for i, j in zip(range(row, -1, -1), range(col, n))
    )
def solve_n_queens(board, row):
    if row >= len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1)
            board[row][col] = 0

def n_queens(n, first_row, first_col):
    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1
    solve_n_queens(board, 1)

# Example: Solve for a 4x4 board with the first queen at (0, 1)
n = 4
first_row = 0
first_col = 0
n_queens(n, first_row, first_col)