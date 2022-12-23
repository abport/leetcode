def fibonacci(n):
    # Base case: handle input of 0
    if n == 0:
        return 0
    
    # Create a list to store the results of subproblems
    memo = [0] * (n+1)
    
    # Base case: F(1) = 1
    memo[1] = 1
    
    # Use a loop to calculate the remaining values
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    # Return the result
    return memo[n]
