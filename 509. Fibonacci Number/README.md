This is a solution for the Coding Problem [509. Fibonacci Number from LeetCode](https://leetcode.com/problems/fibonacci-number/description):

Dynamic programming is a technique that can be used to improve the efficiency of recursive algorithms by storing the results of subproblems and reusing them when needed. Here is an example of how you can solve the Fibonacci sequence problem using dynamic programming in Python:

```python
def fibonacci(n):
    # Create a list to store the results of subproblems
    memo = [0] * (n+1)

    # Base case: F(0) = 0 and F(1) = 1
    memo[0] = 0
    memo[1] = 1

    # Use a loop to calculate the remaining values
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    # Return the result
    return memo[n]
```

This solution has a **time complexity of O(n)**, since it only calculates each value in the Fibonacci sequence once. It also has a **space complexity of O(n)**, since it stores the results of the subproblems in a list.

Here is an example of how you can use this function:

```python
print(fibonacci(2)) # Output: 1
print(fibonacci(3)) # Output: 2
print(fibonacci(4)) # Output: 3
```
