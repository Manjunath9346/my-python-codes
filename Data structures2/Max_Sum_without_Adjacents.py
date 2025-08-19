# User function Template for python3
class Solution:
	
	def findMaxSum(self, arr):
		if not arr:
			return 0
		n = len(arr)
		if n == 1:
			return arr[0]
		
		# Initialize two variables: prev and prev2
		prev = arr[0]     # Max sum including first element
		prev2 = 0         # Max sum excluding first element
		
		for i in range(1, n):
			pick = arr[i] + prev2   # Pick current element + sum excluding previous
			not_pick = prev         # Skip current element, keep previous sum
			curr = max(pick, not_pick)
			prev2 = prev
			prev = curr
		
		return prev

# Example usage:
sol = Solution()
print(sol.findMaxSum([5, 5, 10, 100, 10, 5]))  # Output: 110
print(sol.findMaxSum([3, 2, 7, 10]))           # Output: 13
print(sol.findMaxSum([9, 1, 6, 10]))           # Output: 19
