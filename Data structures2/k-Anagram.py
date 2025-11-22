class Solution:
    def areKAnagrams(self, s1, s2, k):
        # If lengths differ → cannot be k-anagrams
        if len(s1) != len(s2):
            return False
        
        from collections import Counter
        
        c1 = Counter(s1)
        c2 = Counter(s2)
        
        # Count how many chars in s1 exceed s2 (need changes)
        changes = 0
        for ch in c1:
            if c1[ch] > c2[ch]:
                changes += c1[ch] - c2[ch]
        
        return changes <= k
sol = Solution()

print(sol.areKAnagrams("fodr", "gork", 2))       # True
print(sol.areKAnagrams("geeks", "eggkf", 1))     # False
print(sol.areKAnagrams("adb", "fdab", 2))        # False
print(sol.areKAnagrams("abc", "bca", 0))         # True
print(sol.areKAnagrams("aaaa", "bbbb", 4))       # True
print(sol.areKAnagrams("aaaa", "bbbb", 3))       # False
print(sol.areKAnagrams("xxyyzz", "yyxxzz", 0))   # True
print(sol.areKAnagrams("abcde", "abzzz", 2))     # False
print(sol.areKAnagrams("pqr", "stu", 3))         # True
print(sol.areKAnagrams("aaaab", "baaaa", 0))     # True
