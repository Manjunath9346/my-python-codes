# User function Template for python3
class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        if n == 2:
            return 3
        
        # dp[i] = number of valid strings of length i
        dp = [0] * (n + 1)
        dp[1], dp[2] = 2, 3
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]  # Fibonacci-like relation
        
        return dp[n]
obj = Solution()

print(obj.countStrings(1))   # Output: 2  -> "0","1"
print(obj.countStrings(2))   # Output: 3  -> "00","01","10"
print(obj.countStrings(3))   # Output: 5  -> "000","001","010","100","101"
print(obj.countStrings(4))   # Output: 8
print(obj.countStrings(5))   # Output: 13
print(obj.countStrings(10))  # Output: 144
