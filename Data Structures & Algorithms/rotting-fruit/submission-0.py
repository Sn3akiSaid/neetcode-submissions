class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0],[0, 1],[-1, 0],[0, -1]]
        time = 0
        fresh = 0
        queue = deque() # queue of rotten oranges
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1):
                        
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
            time += 1
            
        
        return time if fresh == 0 else -1
        