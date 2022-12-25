class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count will store the number of times each character appears in the current substring
        count = {}
        # res will store the maximum length of a substring with all the same letter found so far
        res = 0

        # l is the start of the current substring, and r is the end
        l = 0
        # we will iterate through the string with r, starting from the second character
        for r in range(len(s)):
            # add one to the count of the current character in the substring
            count[s[r]] = 1 + count.get(s[r], 0)

            # while the number of different characters in the substring is greater than k
            while (r - l + 1) - max(count.values()) > k:
                # remove the character at the start of the substring from the count
                count[s[l]] -= 1
                # move l to the right, shrinking the substring
                l += 1

            # update the maximum length if necessary
            res = max(res, r - l + 1)

        # return the maximum length found
        return res
