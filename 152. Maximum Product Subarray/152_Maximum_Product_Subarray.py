class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # check if the list is empty
        if not nums:
            return 0
        
        n = len(nums)
        # initialize max_product as the first element in the list
        max_product = nums[0]
        # initialize min_product as the first element in the list
        min_product = nums[0]
        # initialize max_so_far as the first element in the list
        max_so_far = nums[0]
        
        # loop through the list starting from the second element
        for i in range(1, n):
            # if the current element is negative, swap max_product and min_product
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            # update max_product as the maximum of the current element or the current element multiplied by the current max_product
            max_product = max(nums[i], nums[i] * max_product)
            # update min_product as the minimum of the current element or the current element multiplied by the current min_product
            min_product = min(nums[i], nums[i] * min_product)
            
            # update max_so_far as the maximum of the current max_so_far or the current max_product
            max_so_far = max(max_so_far, max_product)
        
        # return the final max_so_far
        return max_so_far

        # --------------------------------------------------
        # Second Solution ----------------------------------
        # We can also use the reduce function from functools library and a lambda function to achieve the same solution.

        # if not nums:
        #     return 0
        
        # return reduce(lambda x, y: max(x, y), [reduce(lambda x, y: (max(x[0]*y, min(x[1]*y, y)), min(x[0]*y, min(x[1]*y, y))), nums])[0]