from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0  # Base case: out of bounds or water

            grid[r][c] = 0  # Mark cell as visited
            area = 1  # Count current land cell

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)  # Add area from neighbors

            return area

        maxarea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # Start DFS when we find land
                    maxarea = max(maxarea, dfs(r, c))  # Captain call

        return maxarea
