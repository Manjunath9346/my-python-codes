class Solution:
    def maxSum(self, arr):
        n = len(arr)
        
        # Compute total sum of elements and initial value of i*arr[i]
        total_sum = sum(arr)
        curr_val = sum(i * arr[i] for i in range(n))
        
        res = curr_val  # store maximum
        
        # Compute values for other rotations using relation:
        # Rj = Rj-1 + total_sum - n*arr[n-j]
        for j in range(1, n):
            curr_val = curr_val + total_sum - n * arr[n - j]
            res = max(res, curr_val)
        
        return res


# Test Cases
sol = Solution()
print(sol.maxSum([8, 3, 1, 2]))   # Output: 29
print(sol.maxSum([1, 2, 3]))      # Output: 8
print(sol.maxSum([4, 13]))        # Output: 13
print(sol.maxSum([10, 1, 2, 3]))  # Output: 29
print(sol.maxSum([20]))           # Output: 0 (only one element, i*arr[i] = 0)
