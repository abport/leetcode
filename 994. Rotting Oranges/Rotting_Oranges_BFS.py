from collections import deque


def orangesRotting(grid):
    # store the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # store the coordinates of the rotten oranges in a queue
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))

    # initialize the number of minutes to 0
    minutes = 0

    # define the four directions in which an orange can rot
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # keep track of the number of fresh oranges that remain
    remaining_fresh_oranges = sum(
        1 for row in grid for cell in row if cell == 1)

    # continue rotting oranges until there are no more fresh oranges or the queue is empty
    while queue and remaining_fresh_oranges > 0:
        # process all the rotten oranges in the current minute
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    # mark the fresh orange as rotten and add it to the queue
                    grid[ni][nj] = 2
                    queue.append((ni, nj))
                    # decrease the count of remaining fresh oranges
                    remaining_fresh_oranges -= 1
        # increase the number of minutes by 1
        minutes += 1

    # return -1 if there are still fresh oranges remaining, otherwise return the number of minutes
    return -1 if remaining_fresh_oranges > 0 else minutes
