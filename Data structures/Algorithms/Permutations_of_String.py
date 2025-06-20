class Solution:
    def findPermutation(self, s):
        res = set()
        
        def backtrack(start, chars):
            if start == len(chars):
                res.add("".join(chars))
                return
            
            for i in range(start, len(chars)):
                chars[start], chars[i] = chars[i], chars[start]
                backtrack(start + 1, chars)
                chars[start], chars[i] = chars[i], chars[start]  # backtrack

        backtrack(0, list(s))
        return sorted(list(res))
sol = Solution()

print(sol.findPermutation("ABC"))
# Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

print(sol.findPermutation("AAA"))
# Output: ['AAA']

print(sol.findPermutation("ABSG"))
# Output: 24 unique permutations in sorted order
