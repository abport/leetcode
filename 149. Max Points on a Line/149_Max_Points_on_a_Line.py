from collections import Counter


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # If there are less than 3 points, the maximum number of points that can
        # lie on the same line is the number of points
        n = len(points)
        if n < 3:
            return n

        result = 0
        # For each point, calculate the number of points that lie on the same
        # line with it
        for i in range(n):
            # Create a dictionary to count the number of points that have the
            # same slope as the current point
            slopes = Counter()
            # Keep track of the number of points that are the same as the
            # current point
            same_point = 1
            # Iterate over the remaining points
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    # If the current point is the same as the comparison point,
                    # increment the count of same points
                    same_point += 1
                    continue

                # Calculate the slope of the line between the current point and
                # the comparison point
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0:
                    # If the x-coordinates are the same, the slope is infinite
                    slope = float("inf")
                else:
                    slope = dy / dx

                # Increment the count of points with the same slope
                slopes[slope] += 1

            # Update the result to be the maximum of the current result and the
            # number of same points
            result = max(result, same_point)
            # Update the result to be the maximum of the current result and the
            # number of same points plus the number of points with the same
            # slope as the current point
            for slope, count in slopes.items():
                result = max(result, count + same_point)

        return result
