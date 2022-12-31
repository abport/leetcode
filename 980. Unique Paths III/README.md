This is a solution for the coding problem [980. Unique Paths III from LeetCode](https://leetcode.com/problems/unique-paths-iii/description):

Have you ever played a game where you have to find your way through a maze? Well, today we are going to learn how to write a program that can find the number of unique paths through a maze!

Our program will take a grid as input, where each cell in the grid can be one of the following:

- 0: an empty cell that we can walk through
- 1: the starting position
- 2: the ending position
- -1: an obstacle that we cannot walk through

We will use a technique called depth-first search (DFS) to find all the unique paths from the starting position to the ending position. DFS is a way of searching through a tree or a graph by starting at the root (in our case, the starting position) and exploring as far as possible along each branch before backtracking.

Let's start by defining a class to hold our solution. Inside the class, we will define the main function `uniquePathsIII` that takes in a grid and returns the number of unique paths.

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # code goes here
```

Inside the main function, we will initialize some variables to store the starting position, the number of empty cells, and the number of steps. We will also iterate through the grid to find the starting position and count the number of empty cells.

```python
        startx = starty = empty = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                cell = grid[row][col]
                if cell >= 0:  # if the cell is not -1 (obstacle), it is an empty cell
                    empty += 1
                if cell == 1:  # if the cell is 1, it is the starting position
                    startx, starty = row, col
```

Now we are ready to start the DFS! To make the code easier to understand, we will define a helper function `dfs` that takes in the grid, the current position, and the number of steps. The helper function will use DFS to find the number of unique paths from the current position.

```python
    def dfs(self, grid, x, y, step):
        # code goes here
```

Inside the helper function, we will first check if we have reached the ending position (cell with value 2). If we have, we will return 1 if we have visited all the empty cells, else we will return 0.

```python
        if grid[x][y] == 2:
            return step == 1
```

Next, we will initialize a variable `ret` to store the number of unique paths. We will also store the value of the current cell in a temporary variable `cur` and mark it as visited by setting it to -2. This will ensure that we do not visit the same cell again during the DFS.

```python
        ret = 0
        cur = grid[x][y]
        grid[x][y] = -2
```

Now it's time to explore the different paths! We will try moving to all four directions (up, down, left, right) and search for unique paths from those positions. We will use a loop to try each direction.

```python
        for dirx, diry in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # calculate the new position
            tx, ty = x + dirx, y + diry
            # if the new position is within the grid and is an empty cell, search for unique paths from that position
            if 0 <= tx < len(grid) and 0 <= ty < len(grid[0]) and grid[tx][ty] >= 0:
                ret += self.dfs(grid, tx, ty, step - 1)
```

Finally, we will restore the value of the current cell and return the number of unique paths.

```python
        grid[x][y] = cur
        return ret
```

And that's it! We have written a program that can find the number of unique paths through a maze.

**Time complexity:** O(4^n), where n is the number of empty cells. This is because we are using DFS and there are at most 4 paths to explore at each empty cell.

**Space complexity:** O(n), where n is the number of empty cells. This is because we are using DFS and the maximum depth of the recursion stack is the number of empty cells.

I hope this helps and that you now have a better understanding of how to find the number of unique paths through a maze using DFS. Let me know if you have any questions or if there is anything else I can do to help.
