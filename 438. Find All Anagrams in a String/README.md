This is solution for the coding problem [438. Find All Anagrams in a String from LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/description):

To solve this problem, we can use a sliding window approach. We can maintain a window of size `len(p)` and slide it through the string `s`, checking at each step if the current window is an anagram of `p`. If it is, we can add the start index of the window to the result.

Here is one way to implement this solution in Python:

```python
from collections import Counter

def findAnagrams(s: str, p: str) -> List[int]:
    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])
    for i in range(len(s) - len(p)):
        if window_count == p_count:
            result.append(i)
        window_count[s[i]] -= 1
        if window_count[s[i]] == 0:
            del window_count[s[i]]
        window_count[s[i + len(p)]] += 1
    if window_count == p_count:
        result.append(len(s) - len(p))
    return result
```

This solution has a time complexity of O(n) and a space complexity of O(m), where `n` is the length of `s` and `m` is the length of `p`.

We start by creating a `Counter` object for `p`, which will keep track of the frequency of each character in `p`. Then, we create a `Counter` object for the initial window in `s`, which is the first `len(p)` characters of `s`.

We then use a loop to slide the window through `s`. At each iteration, we check if the current window is an anagram of `p` by comparing the `Counter` objects. If they are equal, we add the start index of the current window to the result.

After each iteration, we update the `Counter` object for the current window by decrementing the count of the character at the current start index and incrementing the count of the character at the current end index. This allows us to efficiently update the `Counter` object as we slide the window through `s` without having to recreate it from scratch at each step.

Finally, we check if the last window is an anagram of `p` by comparing the `Counter` objects one last time and adding the start index of the last window to the result if they are equal.
