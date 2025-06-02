class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            seen = set()
            for square in range(9):
                if board[row][square] == '.':
                    continue
                if board[row][square] in seen:
                    return False
                seen.add(board[row][square])

        for column in range(9):
            seen = set()
            for square in range(9):
                if board[square][column] == '.':
                    continue
                if board[square][column] in seen:
                    return False
                seen.add(board[row][square])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):            
                    row = (square // 3)*3 + i
                    column = (square % 3)*3 + j
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])
        return True
    

        