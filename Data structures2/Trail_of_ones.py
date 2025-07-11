class Solution:
    def countConsec(self, n: int) -> int:
        # Total binary strings of length n
        total = 2 ** n

        # Count of binary strings with no consecutive 1's using DP
        # Let a[i] be count of strings ending with 0 of length i
        # Let b[i] be count of strings ending with 1 of length i
        a = [0] * (n + 1)
        b = [0] * (n + 1)

        a[1] = 1
        b[1] = 1

        for i in range(2, n + 1):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]

        # Total strings without consecutive 1's
        without_consec_1s = a[n] + b[n]

        # Required = total strings - strings without consecutive 1's
        return total - without_consec_1s
sol = Solution()

# Test Case 1
print(sol.countConsec(2))  
# Output: 1

# Test Case 2
print(sol.countConsec(3))  
# Output: 3

# Test Case 3
print(sol.countConsec(5))  
# Output: 19

# Test Case 4
print(sol.countConsec(4))  
# Output: 7
