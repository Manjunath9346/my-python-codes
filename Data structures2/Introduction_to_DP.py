MOD = 10**9 + 7

class Solution:
    # Top-Down DP (Memoization)
    def topDown(self, n):
        memo = [-1] * (n + 1)
        
        def fib(k):
            if k == 0: 
                return 0
            if k == 1: 
                return 1
            if memo[k] != -1:
                return memo[k]
            memo[k] = (fib(k-1) + fib(k-2)) % MOD
            return memo[k]
        
        return fib(n)
    
    # Bottom-Up DP (Tabulation)
    def bottomUp(self, n):
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        return dp[n]


# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.topDown(5))     # Output: 5
    print(sol.bottomUp(5))    # Output: 5
    
    print(sol.topDown(6))     # Output: 8
    print(sol.bottomUp(6))    # Output: 8
    
    print(sol.topDown(50))    # Output: 12586269025 % MOD
    print(sol.bottomUp(50))   # Output: 12586269025 % MOD
Introduction to DP.py
