This is a solution for the coding problem [149. Max Points on a Line from LeetCode](https://leetcode.com/problems/max-points-on-a-line/description) in Python:

## Problem: Maximum Points on a Line

Given a set of points on a 2D plane, we want to find the maximum number of points that lie on the same straight line.

For example, given the following set of points:

```python
[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
```

We can see that all 5 points lie on the same straight line, so the maximum number of points on a line is 5.

On the other hand, given the following set of points:

```python
[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]
]
```

We can see that all 10 points still lie on the same straight line, so the maximum number of points on a line is still 5.

## Solution

To solve this problem, we can iterate over all pairs of points and calculate the slope of the line between them. If the slope is the same for two points, it means that they lie on the same line.

To calculate the slope of a line, we can use the formula:

```python
slope = (y2 - y1) / (x2 - x1)
```

Where `(x1, y1)` and `(x2, y2)` are the coordinates of the two points.

We can use a dictionary to count the number of points that have the same slope as a particular point. Then, for each point, we can update a result variable to be the maximum of the current result and the number of points with the same slope as the current point, plus the number of points that are the same as the current point.

Here is some sample code that demonstrates this approach:

```python
from collections import Counter

def max_points(points):
    n = len(points)
    if n < 3:
        return n

    result = 0
    for i in range(n):
        slopes = Counter()
        same_point = 1
        for j in range(i + 1, n):
            if points[i] == points[j]:
                same_point += 1
                continue

            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                slope = float("inf")
            else:
                slope = dy / dx

            slopes[slope] += 1

        result = max(result, same_point)
        for slope, count in slopes.items():
            result = max(result, count + same_point)

    return result

print(max_points([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]))
print(max_points([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]))
```

## Time and Space Complexity

The **time complexity** of this solution is **O(n^2)** because we iterate over all pairs of points and use a dictionary to count the number of points that have the same slope as a particular point. The **space complexity** is also **O(n^2)** because the dictionary used to count the number of points with the same slope can have at most n entries.

## Conclusion

In this problem, we saw how to find the maximum number of points that lie on the same straight line. We solved the problem by iterating over all pairs of points and using a dictionary to count the number of points with the same slope as a particular point. The time complexity of this solution is O(n^2) and the space complexity is O(n^2).

I hope this helps! Let me know if you have any questions.
