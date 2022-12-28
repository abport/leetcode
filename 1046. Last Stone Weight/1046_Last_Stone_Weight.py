import heapq


def lastStoneWeight(stones):
    # create a max heap
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    # keep removing the heaviest two stones and combining them until
    # there is at most one stone left in the heap
    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        if x != y:
            # insert the lighter stone back into the heap with its new weight
            heapq.heappush(heap, x - y)

    # return the weight of the remaining stone (if there is one) or 0
    return -heap[0] if heap else 0


# test the function
stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))  # should print 1

stones = [1]
print(lastStoneWeight(stones))  # should print 1
