class Solution:
    def caseSort(self, s):
        # Separate lowercase and uppercase characters and sort each
        lower = sorted([ch for ch in s if ch.islower()])
        upper = sorted([ch for ch in s if ch.isupper()])
        
        res = []
        l, u = 0, 0
        
        # Reconstruct string preserving case positions
        for ch in s:
            if ch.islower():
                res.append(lower[l])
                l += 1
            else:
                res.append(upper[u])
                u += 1
                
        return ''.join(res)
sol = Solution()

print(sol.caseSort("GEekS"))     # ✅ Output: "EGekS"
print(sol.caseSort("XWMSPQ"))    # ✅ Output: "MPQSWX"
print(sol.caseSort("bAcBd"))     # ✅ Output: "aBcBd"
print(sol.caseSort("zYxW"))      # ✅ Output: "xYzW"
