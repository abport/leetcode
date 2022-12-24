def numTilings(self, n: int) -> int:
    # Define a constant for the modulo value
    kMod = 1_000_000_007

    # Initialize the dp array with the values for the first 4 positions
    dp = [0, 1, 2, 5] + [0] * 997

    # Iterate from 4 to n
    for i in range(4, n + 1):
        # Compute the number of ways to tile a 2 x i board as the sum of the number of ways to tile
        # a 2 x (i - 1) board using tromino tiles and the number of ways to tile a 2 x (i - 3) board using tromino tiles
        dp[i] = 2 * dp[i - 1] + dp[i - 3]

    # Return the result modulo kMod
    return dp[n] % kMod
