def maxAreaOfIsland(grid):
    # Function to perform DFS from a given cell
    def dfs(i, j):
        # Check if the cell is within the grid bounds and has value 1
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            # Mark the cell as visited by setting its value to 0
            grid[i][j] = 0
            # Explore the neighbors of the cell
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        return 0

    # Initialize the maximum area to 0
    max_area = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell has value 1, start a DFS from it and update the maximum area
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area
