class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        freshFruits = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c, 0)) #r, c and time
                elif grid[r][c] == 1:
                    freshFruits += 1

        
        minutes = 0

        while queue:
            r, c, t = queue.popleft()
            minutes = t   

            for dr, dc in [(1,0), (-1,0),(0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if nr < rows and nr >= 0 and nc < cols and nc >= 0 and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, t+1))
                    freshFruits -= 1

        return minutes if freshFruits == 0 else -1