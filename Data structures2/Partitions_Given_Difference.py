from typing import List

class Solution:
    def countPartitions(self, arr: List[int], d: int) -> int:
        total_sum = sum(arr)
        
        # We must have (sum1 - sum2 = d) and (sum1 + sum2 = total_sum)
        # => 2 * sum1 = total_sum + d => sum1 = (total_sum + d) // 2
        if (total_sum + d) % 2 != 0 or total_sum < d:
            return 0
        
        target = (total_sum + d) // 2
        
        # Count subsets with sum == target using DP
        n = len(arr)
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]
sol = Solution()

# Test Case 1
print(sol.countPartitions([5, 2, 6, 4], 3))  
# Output: 1

# Test Case 2
print(sol.countPartitions([1, 1, 1, 1], 0))  
# Output: 6

# Test Case 3
print(sol.countPartitions([1, 2, 1, 0, 1, 3, 3], 11))  
# Output: 2

# Test Case 4
print(sol.countPartitions([1, 2, 3], 1))  
# Output: 1
