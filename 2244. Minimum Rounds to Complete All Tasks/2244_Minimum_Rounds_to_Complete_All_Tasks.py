from collections import Counter


def minimumRounds(tasks: List[int]) -> int:
    # Store the frequencies in the map.
    freq = Counter(tasks)

    minimum_rounds = 0
    # Iterate over the task's frequencies.
    for task, count in freq.items():
        # If the frequency is 1, it's not possible to complete tasks.
        if count == 1:
            return -1

        if count % 3 == 0:
            # Group all the task in triplets.
            minimum_rounds += count // 3
        else:
            # If count % 3 = 1; (count // 3 - 1) groups of triplets and 2 pairs.
            # If count % 3 = 2; (count // 3) groups of triplets and 1 pair.
            minimum_rounds += count // 3 + 1

    return minimum_rounds
