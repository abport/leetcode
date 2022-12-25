class Solution {
    // This function takes in an array of integers called 'nums' and an array of integers called 'queries'
    // It returns an array of integers called 'res'
    public int[] answerQueries(int[] nums, int[] queries) {
        // Sort the elements in 'nums' in ascending order
        Arrays.sort(nums)
        // Find the length of 'nums' and store it in the variable 'len'
        int len = nums.length
        // Create an array called 'presum' that has the same length as 'nums'
        int[] presum = new int[len]
        // Set the first element in 'presum' to be the first element in 'nums'
        presum[0] = nums[0]
        // Loop through the rest of the elements in 'nums'
        for (int i=1
             i < len
             i++) {
            // Set the ith element in 'presum' to be the sum of the previous element in 'presum' and the ith element in 'nums'
            presum[i] = presum[i - 1] + nums[i]
        }

        // Find the length of 'queries' and store it in the variable 'm'
        int m = queries.length
        // Create an array called 'res' that has the same length as 'queries'
        int[] res = new int[m]
        // Loop through 'queries'
        for (int i=0
             i < m
             i++) {
            // Call the helper function and pass it 'presum' and the ith element in 'queries'
            // Store the result in the variable 'j'
            int j = helper(presum, queries[i])
            // Set the ith element in 'res' to be 'j' plus 1
            res[i] = j + 1
        }
        // Return 'res'
        return res
    }

    // This function takes in an array of integers called 'nums' and an integer called 'target'
    // It returns an integer
    private int helper(int[] nums, int target) {
        // Set the left and right indices for the binary search to be the start and end of 'nums', respectively
        int left = 0
        int right = nums.length - 1
        // Initialize the result to be - 1
        int res = -1
        // Run the binary search until the left index is greater than the right index
        while (left <= right) {
            // Find the middle index between the left and right indices
            int mid = left + (right - left) / 2
            // If the middle element in 'nums' is less than or equal to 'target'
            if (nums[mid] <= target) {
                // Update the result to be the middle index
                res = mid
                // Set the left index to be one index to the right of the middle index
                left = mid + 1
            } else {
                // Set the right index to be one index to the left of the middle index
                right = mid - 1
            }
        }
        // Return the result
        return res
    }
}
