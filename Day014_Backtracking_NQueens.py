## Problem
Place N queens on an N x N chessboard such that:
No two queens share the same row
No two queens share the same column
No two queens share the same diagonal
Return all valid board configurations.
Example for n = 4 (2 solutions):

. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .


SOLUTION: # Day 14: N-Queens

def solveNQueens(n):
    result = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # place queen
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # remove queen (backtrack)
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


## LOGIc was One queen per row (always)
So recursion level = row number
At each row → try placing queen in every column.

Why diagonals are row - col and row + col
All cells on same diagonal share these values
That’s geometry, not tric
Why no used[] here

Because:
Rows are fixed by recursion
Columns tracked by cols
Diagonals tracked separately
Different problem, different constraint logic.

@@ Mental model (important)
“I place queens row by row, and I kill bad branches early.”
That’s intelligent recursion.
