from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

