class Solution:
    def solve(self, board: list[list[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        # There are three main steps:

        # 1) Turn all entries connected to the edges which contain 'O' to T so that we
        # can ignore them in part 2 (dfs because we also turn all connecting 'O' to 'T')

        # 2) Turn all remaining 'O' to 'X'

        # 3) Turn all 'T' back to 'O'

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O'):
                return
            
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"