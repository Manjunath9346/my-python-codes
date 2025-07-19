class Solution:
    def countSubstr(self, s, k):
        return self.atMostKDistinct(s, k) - self.atMostKDistinct(s, k - 1)

    def atMostKDistinct(self, s, k):
        from collections import defaultdict
        count = defaultdict(int)
        left = res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            res += right - left + 1
        return res
test_cases = [
    ("abc", 2, 2),
    ("aba", 2, 3),
    ("aa", 1, 3),
    ("a", 1, 1),
    ("a", 2, 0),
    ("abc", 4, 0),
    ("aaa", 1, 6),
    ("abcde", 5, 1),
    ("abcabc", 3, 10),
    ("aabacbebebe", 3, 23),
    ("abcdabc", 2, 10),
    ("a" * 100000, 1, 5000050000),
]

sol = Solution()
for i, (s, k, expected) in enumerate(test_cases, 1):
    result = sol.countSubstr(s, k)
    print(f"Test Case {i}: s = '{s[:10] + '...' if len(s) > 10 else s}', k = {k}")
    print(f"Expected: {expected}, Got: {result}")
    print("Pass " if result == expected else "Fail ", end="\n\n")








