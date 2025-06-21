class Solution:
    def findPermutation(self, s):
        def backtrack(path, used):
            if len(path) == len(s):
                res.add("".join(path))
                return
            for i in range(len(s)):
                if not used[i]:
                    used[i] = True
                    path.append(s[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        res = set()
        s = sorted(s)
        used = [False] * len(s)
        backtrack([], used)
        return sorted(list(res))
sol = Solution()
print(sol.findPermutation("ABC"))  # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(sol.findPermutation("AAA"))  # Output: ['AAA']
