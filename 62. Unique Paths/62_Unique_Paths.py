def uniquePaths(m: int, n: int) -> int:
    # create the dp array and initialize the first row and column with 1
    dp = [[1] * n for _ in range(m)]

    # fill the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # return the number of unique paths from the top-left corner to the bottom-right corner
    return dp[m-1][n-1]
