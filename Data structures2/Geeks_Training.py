class Solution:
    def maximumPoints(self, arr):
        prev = arr[0]
        for i in range(1, len(arr)):
            cur = [0]*3
            for j in range(3):
                cur[j] = arr[i][j] + max(prev[(j+1)%3], prev[(j+2)%3])
            prev = cur
        return max(prev)
sol = Solution()

print(sol.maximumPoints([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))  
# 11

print(sol.maximumPoints([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))  
# 6

print(sol.maximumPoints([[4, 2, 6]]))  
# 6
