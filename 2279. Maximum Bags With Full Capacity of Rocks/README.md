This is a solution for the coding problem [2279. Maximum Bags With Full Capacity of Rocks from LeetCode](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description):

### [Official Solution from LeetCode](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/solutions/2643763/maximum-bags-with-full-capacity-of-rocks/):

### Overview

In this problem, we are given two arrays `rocks` and `capacity` of the same length `n`, which represent `n` bags. Each bag `i` has a maximum capacity of `capacity[i]` and currently contains `rocks[i]` rocks. We are also given `additionalRock` to fill the bags if they are unfilled.

For example, in the picture below, the first bag has a capacity of `2` and currently contains `0` rocks, thus we can fill it with `2` additional rocks. However, the last bag has a capacity of `6` and currently contains `3` rocks, thus we can't fill it since we only have `2` additonal rocks but it requires `3`.

![img](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/solutions/2643763/Figures/2279/2279-ex.png)

We want to fill as many bags as possible, the question is: how many bags can we fill?

---

### Approach 1: Greedy

#### Intuition

Since we want to fill the bags, thus we only care about the **remaining capacity** of each bag. For example:

- Bag 1 has a capacity of `5` and currently contains `3` rocks.
- Bag 2 has a capacity of `20` and currently contians `18` rocks.

It takes the same amount of rocks (`2`) to fill both bags, so for us there is no difference between the two bags: they both have `2` remaining capacity.

Therefore, we need to calculate the remaining capacity of each bag `i`, by letting its capacity `capacity[i]` substract the number of rocks it currently has `rocks[i]`. That is: `remaining capacity of bag i = capacity[i] - rocks[i]`.

As we would like to full as many bags as possible, we will fill the bag with the smallest remaining capacity first.

Therefore, we should sort all the bags by the order of remaining capacity, then start to fill them using `additionalRocks` from the bag with the smallest remaining capacity. This process stops when we don't have enough rocks to fill the current bag. Since we sort by remaining capacity, all subsequent bags will have no less remaining capacity than the current one, so if we can't fill this bag, it means we can't fill any of the bags after it.

#### Algorithm

1.  Calculate the remaining capacity of each bag and store the values in an array `remaining_capacity`, set `full_bags = 0`.
2.  Sort `remaining_capacity`.
3.  Iterate over the sorted `remaining_capacity`, for each value `cap`, check we have enough `additionalRocks` to fill `cap`.
    - If so, increment `full_bags` by 1, decrement `additionalRocks` by `cap`, and move on to the next bag.
    - Otherwise, stop iterating as we don't have enough rocks to continue.
4.  After we run out of rocks or finish the iteration, return `full_bags`.

#### Implementation

```python
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Sort bags by the remaining capacity.
        remaining_capacity = [cap - rock for cap, rock in zip(capacity, rocks)]
        remaining_capacity.sort()
        full_bags = 0

        # Iterate over sorted bags and fill them using additional rocks.
        for curr_capacity in remaining_capacity:
            # If we can fill the current one, fill it and move on.
            # Otherwise, stop the iteration.
            if additionalRocks >= curr_capacity:
                additionalRocks -= curr_capacity
                full_bags += 1
            else:
                break

        # Return `full_bags` after the iteration stops.
        return full_bags
```

#### Explanation of the code :

This code defines a class `Solution` with a method `maximumBags`, which takes in three arguments:

- `capacity`: a list of integers representing the capacities of the bags
- `rocks`: a list of integers representing the number of rocks already in each bag
- `additionalRocks`: an integer representing the number of additional rocks we can use to fill the bags

The method first calculates the remaining capacity for each bag by subtracting the number of rocks already in the bag from its capacity. It stores the resulting list of remaining capacities in a variable called `remaining_capacity`.

Next, it sorts `remaining_capacity` in ascending order.

It then initializes a variable `full_bags` to 0. This variable will be used to keep track of the number of bags that we can fill using the additional rocks.

The method then iterates over the sorted list of remaining capacities, and for each remaining capacity, it checks if there are enough additional rocks to fill the bag. If there are, it fills the bag by subtracting the remaining capacity from `additionalRocks`, and increments `full_bags` by 1. If there aren't enough additional rocks to fill the bag, the iteration is stopped using the `break` statement.

Finally, the method returns `full_bags`, which is the number of bags that were filled during the iteration.

#### Complexity Analysis

Let nnn be the size of the input array `capacity`.

- Time complexity: O(n⋅log⁡n)

  - We use an array `remaining_capacity` to store the remaining capacity of each bag and it takes O(n) time.
  - Sorting `remaining_capacity` requires O(n⋅log⁡n) time.
  - We iterate over the sorted array `remaining_capacity` and it takes O(n) time.
  - To sum up, the overall time complexity is O(n⋅log⁡n).

- Space complexity: O(n)

  - We use an array of size nnn to store the remaining capacity of each bag.
