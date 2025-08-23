class Solution:
    def areRotations(self, s1, s2):
        # if lengths differ, can't be rotations
        if len(s1) != len(s2):
            return False
        # check if s2 is in s1+s1
        return s2 in (s1 + s1)
if __name__ == "__main__":
    sol = Solution()
    
    # Testcases
    test_cases = [
        ("abcd", "cdab", True),    # 2 right rotations
        ("aab", "aba", True),      # 1 left rotation
        ("abcd", "acbd", False),   # not a rotation
        ("aaaa", "aaaa", True),    # same string
        ("abc", "cab", True),      # 2 left rotations
        ("abc", "bca", True),      # 1 left rotation
        ("abc", "bac", False)      # not a rotation
    ]
    
    for s1, s2, expected in test_cases:
        result = sol.areRotations(s1, s2)
        print(f"s1={s1}, s2={s2} | Output: {result} | Expected: {expected}")
