class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        area = 0

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))
            res = 1
            
            while queue:
                row, col = queue.popleft()
                for dr,dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr < 0 or
                        nc < 0 or
                        nr>= ROWS or
                        nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
                    
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
                
        return area