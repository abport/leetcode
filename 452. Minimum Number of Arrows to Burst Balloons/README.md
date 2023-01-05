This is a solution for the coding problem [452. Minimum Number of Arrows to Burst Balloons from LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description) in Python:

Today we're going to talk about a problem called "**Minimum Number of Arrows to Burst Balloons**". It's a fun problem that involves shooting arrows at balloons!

The problem gives us a list of balloons, each with a start position and an end position. Our goal is to find the minimum number of arrows needed to burst all the balloons. However, there is a catch: if an arrow is shot at a position between the start and end positions of a balloon, the balloon will burst!

For example, let's say we have the following list of balloons: [[10,16], [2,8], [1,6], [7,12]]. This means that we have 4 balloons at the following positions:

- Balloon 1: [10, 16]
- Balloon 2: [2, 8]
- Balloon 3: [1, 6]
- Balloon 4: [7, 12]

To burst all these balloons, we could use the following arrows:

- Arrow 1: Position 8 (bursts Balloon 2 and Balloon 3)
- Arrow 2: Position 10 (bursts Balloon 1)
- Arrow 3: Position 12 (bursts Balloon 4)

So in this case, we needed 3 arrows to burst all the balloons. Can you figure out how many arrows we would need if the list of balloons was [[1,2], [3,5], [4,7], [5,8], [7,9]]?

Here is the complete code:

```python
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
```

**Time complexity:** **O(nlogn)**, because we are sorting the points list which takes O(nlogn) time.

**Space complexity:** **O(1)**, because we are only using constant extra space regardless of the size of the input.

Happy coding!
