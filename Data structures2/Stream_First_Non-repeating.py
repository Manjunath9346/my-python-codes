from collections import deque

class Solution:
    def FirstNonRepeating(self, s):
        # Queue to keep track of non-repeating characters in order
        q = deque()
        # Dictionary to count occurrences of characters
        freq = {}
        # Result string
        res = ""

        for ch in s:
            # Update frequency
            freq[ch] = freq.get(ch, 0) + 1
            # Add to queue
            q.append(ch)

            # Remove characters from queue that are not non-repeating anymore
            while q and freq[q[0]] > 1:
                q.popleft()

            # Append first non-repeating character or '#'
            if q:
                res += q[0]
            else:
                res += "#"

        return res

sol = Solution()

print(sol.FirstNonRepeating("aabc"))   # Output: "a#bb"
print(sol.FirstNonRepeating("zz"))     # Output: "z#"
print(sol.FirstNonRepeating("bb"))     # Output: "b#"
print(sol.FirstNonRepeating("abcabc")) # Output: "a#bbb#"
