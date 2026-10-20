class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and (r,c) not in visited):
                    visited.add((r,c))
                    islands+=1
                    q = deque([(r,c)])
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == "1":
                                visited.add((nr,nc))
                                q.append((nr,nc))
        return islands