class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        best_area = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and (r,c) not in visited):
                    visited.add((r,c))
                    q = deque([(r,c)])
                    area = 0
                    while q:
                        row, col = q.popleft()
                        area+=1
                        for dr, dc in directions:
                            nr, nc = row+dr, dc+col
                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited):
                                visited.add((nr,nc))
                                q.append((nr,nc))
                    best_area = max(area, best_area)
        return best_area
