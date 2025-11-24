class Solution:
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
Input: 8
Output: true
Input: 98
Output: false
