def floodFill(image, sr, sc, color):
    # base case: return the image if the starting pixel is already the target color
    if image[sr][sc] == color:
        return image

    # store the original color of the starting pixel
    original_color = image[sr][sc]

    # create a queue to store the pixels that need to be colored
    queue = [(sr, sc)]

    # create a set to store the pixels that have been visited
    visited = set()

    # perform a breadth-first search to find all connected pixels of the same color as the starting pixel
    while queue:
        r, c = queue.pop(0)

        # skip this pixel if it has already been visited
        if (r, c) in visited:
            continue

        # mark this pixel as visited
        visited.add((r, c))

        # color this pixel if it is the same color as the starting pixel
        if image[r][c] == original_color:
            image[r][c] = color

            # add the 4-connected neighbors to the queue
            if r > 0:
                queue.append((r-1, c))
            if r < len(image) - 1:
                queue.append((r+1, c))
            if c > 0:
                queue.append((r, c-1))
            if c < len(image[0]) - 1:
                queue.append((r, c+1))

    # return the modified image
    return image
