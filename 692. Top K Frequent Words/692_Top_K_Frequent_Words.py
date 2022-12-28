from collections import Counter
import heapq


def topKFrequent(words, k):
    # Count the frequency of each word
    word_count = Counter(words)

    # Create a min heap to store the words sorted by their frequency and lexicographical order
    heap = [(-count, word) for word, count in word_count.items()]
    heapq.heapify(heap)

    # Pop the first k elements from the heap and return them
    return [heapq.heappop(heap)[1] for _ in range(k)]
