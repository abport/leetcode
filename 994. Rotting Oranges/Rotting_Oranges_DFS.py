def orangesRotting(grid):
    # store the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # store the coordinates of the rotten oranges in a stack
    stack = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                stack.append((i, j))

    # initialize the number of minutes to 0
    minutes = 0

    # define the four directions in which an orange can rot
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # keep track of the number of fresh oranges that remain
    remaining_fresh_oranges = sum(
        1 for row in grid for cell in row if cell == 1)

    # continue rotting oranges until there are no more fresh oranges or the stack is empty
    while stack and remaining_fresh_oranges > 0:
        # process all the rotten oranges in the current minute
        for _ in range(len(stack)):
            i, j = stack.pop()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[
