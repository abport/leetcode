def minCostClimbingStairs(cost):
    # Get the number of steps
    n = len(cost)

    # Initialize an array dp of size n+1 with all elements set to 0
    dp = [0] * (n + 1)

    # Loop through the array from index 2 to n+1 (since we can either start from index 0 or 1)
    for i in range(2, n + 1):
        # Calculate the minimum cost to reach the current step by taking the minimum of
        # the cost to reach the previous step plus the cost of the current step,
        # and the cost to reach the step before that plus the cost of the step before that
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    # Return the minimum cost to reach the top of the floor, which is stored at index n in the dp array
    return dp[n]
