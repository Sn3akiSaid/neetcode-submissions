class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1,0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            # Mark as 0 and append it - visited
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                # Pop a cell into a local row, col variable
                row, col = queue.popleft()

                # For an increment in each direction
                for dr, dc in directions:
                    # Explore a direction from current cell
                    nr, nc =  row + dr, col + dc

                    # If: 
                    if (nr < 0 or # Outside of map start horizontally
                        nc < 0 or # Outside of map start vertically
                        nr >= ROWS or # Outside of map end horizontally
                        nc >= COLS or # Outside of map end vertically
                        grid[nr][nc] == "0"): # Or that neighbour cell is water
                        # Move on
                        continue
                    # Otherwise we add that cell into the queue, because it's land
                    queue.append((nr, nc))
                    # And mark it as 0, i.e. visited
                    grid[nr][nc] = "0"

        # Traverse each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If it is land, run bfs from that cell
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands