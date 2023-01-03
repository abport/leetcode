class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # String length
        K = len(strs[0])

        # Variable to store the count of columns to be deleted
        answer = 0

        # Iterate over each index in the string
        for col in range(K):
            # Iterate over the strings
            for row in range(1, len(strs)):
                # Characters should be in increasing order,
                # If not, increment the counter
                if strs[row][col] < strs[row-1][col]:
                    answer += 1
                    break

        # Return the number of columns that need to be deleted
        return answer
