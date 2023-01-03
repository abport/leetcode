This is a solution for the coding problem [944. Delete Columns to Make Sorted from LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/description) in Python:

**[Click here for the official Solution from LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/solutions/2868555/delete-columns-to-make-sorted/)**

Today, we're going to learn about a problem called "Delete Columns to Make Sorted". The problem goes like this:

You are given a list of strings, and your task is to delete some of the columns (characters) from the strings such that the remaining strings are in lexicographical order (dictionary order). In other words, the characters in each string should be in non-descending order from left to right.

For example, given the following list of strings:

```python
['cba', 'daf', 'ghi']
```

We can delete the second column (the `b` in the first string and the `a` in the second string) to get the following list of strings:

```python
['ca', 'df', 'gi']
```

Now, the strings are in lexicographical order.

Your task is to write a function that takes in a list of strings and returns the minimum number of columns that need to be deleted to make the strings lexicographically sorted.

Here is an example of how your function should work:

```python
>>> delete_columns(['cba', 'daf', 'ghi'])
1
>>> delete_columns(['a', 'b', 'c'])
0
>>> delete_columns(['a', 'ab', 'abc'])
0
>>> delete_columns(['zyx', 'wvu', 'tsr'])
3
```

Can you solve this problem?

---

**Solution:**

Here is a solution in Python:

```python
class Solution:
    def delete_columns(self, strs: List[str]) -> int:
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
```

**Explanation:**

- The function `delete_columns` takes in a list of strings and returns an integer.
- First, we find the length of the first string (which are all the same length). This will be used to loop over the characters in each string.
- We create a variable called `answer` which will be used to store the number of columns that need to be deleted. Initially, this is set to 0.
- We have a nested loop. The outer loop iterates over each index (column) in the strings. The inner loop iterates over the strings.
- For each string, we check if the character at the current index (`col`) is lexicographically smaller than the character at the same index in the previous string (`row-1`). If it is, we increment `answer` by 1 and break out of the inner loop.
- Finally, we return `answer`, which is the number of columns that need to be deleted.

**Time Complexity: O(N\*K)**

In the worst case, we will have to compare every character in every string. Since there are N strings, each with K characters, the time complexity of this solution is O(N\*K).

**Space Complexity: O(1)**

We only use a constant amount of space to store the answer and some variables for looping, so the space complexity of this solution is O(1).

That's it! We have successfully solved the "Delete Columns to Make Sorted" problem. I hope you enjoyed this problem and learned something new.

Talk to you in the next one!
