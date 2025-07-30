# User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [0] * n
        dp[0] = 0
        
        for i in range(1, n):
            one_step = dp[i-1] + abs(height[i] - height[i-1])
            two_step = dp[i-2] + abs(height[i] - height[i-2]) if i > 1 else float('inf')
            dp[i] = min(one_step, two_step)
        
        return dp[-1]  # ✅ Only return, no print
if __name__ == "__main__":
    obj = Solution()

    test_cases = [
        ([20, 30, 40, 20], 20),
        ([30, 20, 50, 10, 40], 30),
        ([10], 0),
        ([10, 50], 40),
        ([10, 20, 30, 40, 50], 40),
        ([100, 80, 60, 40, 20], 80),
        ([10, 30, 40, 20, 50], 40)
    ]

    for heights, expected in test_cases:
        result = obj.minCost(heights)
        print(f"Input: {heights} | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
