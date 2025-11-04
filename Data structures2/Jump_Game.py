class Solution:
    def canReach(self, arr):
        max_reach = 0
        n = len(arr)
        for i in range(n):
            if i > max_reach:  # if we can’t reach this index, stop
                return False
            max_reach = max(max_reach, i + arr[i])
            if max_reach >= n - 1:  # if we can reach or exceed last index
                return True
        return True
print(Solution().canReach([1, 2, 0, 3, 0, 0]))   # ✅ True
print(Solution().canReach([1, 0, 2]))            # ❌ False
print(Solution().canReach([3, 2, 1, 0, 4]))      # ❌ False
print(Solution().canReach([2, 3, 1, 1, 4]))      # ✅ True
print(Solution().canReach([0]))                  # ✅ True (already at end)
print(Solution().canReach([2, 0, 0]))            # ✅ True
print(Solution().canReach([1, 1, 1, 1, 1]))      # ✅ True
