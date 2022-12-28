class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # This creates a new list called heap which contains the negative values of each element in the piles list
        heap = [-num for num in piles]
        # So if the piles list is [5, 4, 9], the heap list will be [-5, -4, -9]

        # This rearranges the elements in the heap list so that they follow the rules of a heap data structure
        heapq.heapify(heap)
        # A heap is a tree-like data structure where the parent nodes are either greater than or less than their child nodes (depending on the type of heap)
        # In this case, we are using a "min heap", which means that the parent nodes are always less than their child nodes

        for _ in range(k):  # This starts a loop that will run for k number of times
            # This removes and returns the smallest element from the heap (which is the first element in the list since the list is now a heap)
            curr = -heapq.heappop(heap)
            # The heappop function also rearranges the remaining elements in the list so that they continue to follow the rules of a heap
            # The smallest element is then negated and stored in a variable called curr
            # For example, if k is 2 and the heap list is [-5, -4, -9], the first time through the loop curr would be 9

            remove = curr // 2  # This calculates the value of remove by dividing curr by 2 and using the "//" operator to round the result down to the nearest integer
            # For example, if curr is 9, remove would be 4

            # This adds a new element to the heap
            heapq.heappush(heap, -(curr - remove))
            # The new element is the negative of the value of curr minus remove
            # For example, if curr is 9 and remove is 4, the new element would be -(9 - 4) which is -5
            # The heappush function also rearranges the elements in the list so that they continue to follow the rules of a heap

        # This returns the negative sum of all the elements in the heap
        return -sum(heap)
        # It does this by using the sum function to add up all the elements in the heap and then negating the result
