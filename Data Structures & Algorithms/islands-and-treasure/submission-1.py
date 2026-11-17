class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            cell = queue.popleft()
            row, col = cell[0], cell[1]

            for r, c in ((1,0), (-1, 0), (0, 1), (0, -1)):
                if row + r >= 0 and row + r < rows and col + c >= 0 and col + c < cols and grid[row + r][col + c] == INF:
                    grid[row + r][col + c] = grid[row][col] + 1
                    queue.append((row + r, col + c))
