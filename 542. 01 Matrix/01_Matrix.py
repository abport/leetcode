from collections import deque


def nearestCell(mat):
    # store the number of rows and columns in the matrix
    m, n = len(mat), len(mat[0])

    # create a queue to store the cells that need to be visited
    queue = deque()

    # create a 2D array to store the distance of each cell from the nearest 0
    distances = [[float('inf')] * n for _ in range(m)]

    # add all the 0s in the matrix to the queue and set their distance to 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
                distances[i][j] = 0

    # define the directions to move in the matrix
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # process the cells in the queue
    while queue:
        # get the coordinates of the next cell
        i, j = queue.popleft()

        # visit all the adjacent cells
        for di, dj in directions:
            # calculate the new row and column indices
            ni, nj = i + di, j + dj

            # check if the new indices are within the bounds of the matrix
            # and if the cell has not been visited yet
            if 0 <= ni < m and 0 <= nj < n and distances[ni][nj] == float('inf'):
                # update the distance of the cell
                distances[ni][nj] = distances[i][j] + 1

                # add the cell to the queue to be processed
                queue.append((ni, nj))

    return distances
