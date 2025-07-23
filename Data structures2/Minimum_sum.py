class Solution:
    def minSum(self, arr):
        # Sort the digits
        arr.sort()
        
        # Form two numbers by picking digits alternately
        num1, num2 = "", ""
        for i in range(len(arr)):
            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])

        # Helper to add two strings without converting to int
        def addStrings(s1, s2):
            i, j = len(s1) - 1, len(s2) - 1
            carry = 0
            res = []
            while i >= 0 or j >= 0 or carry:
                d1 = int(s1[i]) if i >= 0 else 0
                d2 = int(s2[j]) if j >= 0 else 0
                total = d1 + d2 + carry
                res.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1
            return ''.join(res[::-1]).lstrip('0') or '0'

        return addStrings(num1, num2)
sol = Solution()

print(sol.minSum([6, 8, 4, 5, 2, 3]))  # Output: "604"
print(sol.minSum([5, 3, 0, 7, 4]))     # Output: "82"
print(sol.minSum([9, 4]))             # Output: "13"
print(sol.minSum([5]))                # Output: "5"
print(sol.minSum([0, 0, 0]))          # Output: "0"
print(sol.minSum([1, 1, 1, 1]))       # Output: "22"
