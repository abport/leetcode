# define a class to hold the solution
class Solution:

    # define the main function that takes in a grid and returns the number of unique paths
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # initialize variables to store the starting position, the number of empty cells, and the number of steps
        startx = starty = empty = 0

        # iterate through the grid to find the starting position and count the number of empty cells
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                cell = grid[row][col]
                # if the cell is not -1 (obstacle), it is an empty cell
                if cell >= 0:
                    empty += 1
                if cell == 1:  # if the cell is 1, it is the starting position
                    startx, starty = row, col

        # call the helper function to find the number of unique paths
        return self.dfs(grid, startx, starty, empty)

    # define the helper function that uses DFS to find the number of unique paths
    def dfs(self, grid, x, y, step):
        # if we have reached the end cell (cell with value 2), return 1 if we have visited all the empty cells, else return 0
        if grid[x][y] == 2:
            return step == 1

        # initialize a variable to store the number of unique paths
        ret = 0

        # store the value of the current cell in a temporary variable and mark it as visited by setting it to -2
        cur = grid[x][y]
        grid[x][y] = -2

        # try moving to all four directions
        for dirx, diry in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # calculate the new position
            tx, ty = x + dirx, y + diry
            # if the new position is within the grid and is an empty cell, search for unique paths from that position
            if 0 <= tx < len(grid) and 0 <= ty < len(grid[0]) and grid[tx][ty] >= 0:
                ret += self.dfs(grid, tx, ty, step - 1)

        # restore the value of the current cell and return the number of unique paths
        grid[x][y] = cur
        return ret
