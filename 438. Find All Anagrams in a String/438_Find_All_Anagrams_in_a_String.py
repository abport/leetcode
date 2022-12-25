from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:
    # Initialize an empty list to store the start indices of p's anagrams in s
    result = []

    # Create a Counter object for p, which will keep track of the frequency of each character in p
    p_count = Counter(p)

    # Create a Counter object for the initial window in s, which is the first len(p) characters of s
    window_count = Counter(s[:len(p)])

    # Loop through the characters in s, starting at the index len(p)
    for i in range(len(s) - len(p)):
        # If the current window is an anagram of p, add the start index of the window to the result
        if window_count == p_count:
            result.append(i)

        # Update the Counter object for the current window by decrementing the count of the character at the current start index
        # and incrementing the count of the character at the current end index
        window_count[s[i]] -= 1
        if window_count[s[i]] == 0:
            del window_count[s[i]]
        window_count[s[i + len(p)]] += 1

    # Check if the last window is an anagram of p and add the start index of the last window to the result if it is
    if window_count == p_count:
        result.append(len(s) - len(p))

    # Return the result
    return result
