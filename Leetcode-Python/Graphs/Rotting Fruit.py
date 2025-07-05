from collections import deque
# Personalised Solution based on the previous Walls & Gates Problem
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        Rotten_Found = False
        visit = set()
        q = deque()

        def rotFruit(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 0):
                return
            
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
                    Rotten_Found = True
        
        minutes = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                grid[r][c] = 2
                rotFruit(r + 1, c)
                rotFruit(r - 1, c)
                rotFruit(r, c + 1)
                rotFruit(r, c - 1)
            minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return minutes if Rotten_Found else 0
