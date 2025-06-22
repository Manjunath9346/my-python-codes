class Solution:
    
    # Function to check whether there is a subarray with 0-sum
    def subArrayExists(self, arr):
        seen_sums = set()
        curr_sum = 0
        
        for num in arr:
            curr_sum += num
            if curr_sum == 0 or curr_sum in seen_sums:
                return True
            seen_sums.add(curr_sum)
        
        return False
sol = Solution()
print(sol.subArrayExists([4, 2, -3, 1, 6]))   # True
print(sol.subArrayExists([4, 2, 0, 1, 6]))    # True
print(sol.subArrayExists([1, 2, -1]))         # False
