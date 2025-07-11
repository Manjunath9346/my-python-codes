class Solution:
    def removeUtil(self, S: str) -> str:
        def remove_adjacent(s):
            n = len(s)
            i = 0
            res = ""
            while i < n:
                # Skip all adjacent duplicates
                if i < n - 1 and s[i] == s[i + 1]:
                    ch = s[i]
                    while i < n and s[i] == ch:
                        i += 1
                else:
                    res += s[i]
                    i += 1
            return res

        prev = ""
        while prev != S:
            prev = S
            S = remove_adjacent(S)
        return S
sol = Solution()

# Test Case 1
print(sol.removeUtil("geeksforgeek"))  
# Output: "gksforgk"

# Test Case 2
print(sol.removeUtil("abccbccba"))  
# Output: ""

# Test Case 3
print(sol.removeUtil("abcd"))  
# Output: "abcd"

# Test Case 4
print(sol.removeUtil("aaaabcccba"))  
# Output: "b"
