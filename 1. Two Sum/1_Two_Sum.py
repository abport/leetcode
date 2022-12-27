class Solution(object):
    def twoSum(self, nums, target):
        """
        Finds the indices of the two numbers in the given list that add up to the target.
        :param nums: List[int] - list of integers
        :param target: int - target sum
        :return: List[int] - list of indices of the two numbers
        """
        # create an empty dictionary to store the values and their indices
        hashMap = {}
        # loop through all the elements in the list
        for i in range(len(nums)):
            # calculate the difference between the target and the current element
            diff = target - nums[i]
            # check if the difference is already in the dictionary
            if diff in hashMap:
                # if it is, return the indices of the current element and the element with the matching difference
                return [hashMap[diff], i]
            else:
                # if it's not, add the current element and its index to the dictionary
                hashMap[nums[i]] = i
        # if the loop finishes running and we haven't found a solution, return an empty list
        return []
