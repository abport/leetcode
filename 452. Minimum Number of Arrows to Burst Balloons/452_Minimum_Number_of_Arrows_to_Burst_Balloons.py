from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    # if the input list is empty, we don't need any arrows
    if not points:
        return 0

    # sort the points by their end position in increasing order
    points.sort(key=lambda x: x[1])

    # initialize the current end position to the end position of the first point
    # and the count to 1 (we need at least one arrow)
    current_end = points[0][1]
    count = 1

    # iterate through the points
    for start, end in points[1:]:
        # if the start position of the current point is after the current end position,
        # it means we need a new arrow for this point
        if start > current_end:
            current_end = end  # update the current end position
            count += 1  # increment the count
    return count  # return the final count
