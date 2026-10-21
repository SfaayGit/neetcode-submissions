class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(grid), len(grid[0])
        minutes = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                rows, cols = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + rows, dc + cols
                    if (0 <= nr< row and 0<= nc < col and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1
        return -1 if fresh > 0 else minutes