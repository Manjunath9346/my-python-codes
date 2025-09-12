class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        res = []
        
        # generate all subsequences using bitmasking
        for mask in range(1, 1 << n):   # from 1 to 2^n - 1
            sub = ""
            for i in range(n):
                if mask & (1 << i):
                    sub += s[i]
            res.append(sub)
        
        # sort lexicographically
        res.sort()
        return res
s = Solution()

print(s.AllPossibleStrings("abc"))
# Expected: ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']

print(s.AllPossibleStrings("aa"))
# Expected: ['a', 'a', 'aa']

print(s.AllPossibleStrings("bca"))
# Expected: ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'] (after sorting)
