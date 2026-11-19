class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        queue_pacific = deque()
        queue_atlantic = deque()

        for r in range(rows):
            for c in range(cols):
                if r - 1 < 0 or c - 1 < 0:
                    queue_pacific.append((r,c))
                if r + 1 == rows or c + 1 == cols:
                    queue_atlantic.append((r,c))
        
        visitedPacific = set(queue_pacific)

        while queue_pacific:
            r, c = queue_pacific.popleft()

            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if nr < rows and nr >= 0 and nc < cols and nc >= 0 and (nr,nc) not in visitedPacific and heights[nr][nc] >= heights[r][c]:

                    visitedPacific.add((nr, nc))
                    queue_pacific.append((nr, nc))

        visitedAtlantic = set(queue_atlantic)

        while queue_atlantic:
            r, c = queue_atlantic.popleft()

            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if nr < rows and nr >= 0 and nc < cols and nc >= 0 and (nr,nc) not in visitedAtlantic and heights[nr][nc] >= heights[r][c]:
                    
                    visitedAtlantic.add((nr, nc))
                    queue_atlantic.append((nr, nc))

        res = []

        for r, c in visitedPacific:
            if (r, c) in visitedAtlantic:
                res.append([r, c])

        return res