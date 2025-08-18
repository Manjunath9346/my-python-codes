# User function Template for python3

class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def combinationSum(self, arr, target):
        result = []
        
        def backtrack(start, path, total):
            if total == target:        # Current path sums to target
                result.append(path[:])
                return
            if total > target:         # Exceeded target
                return
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i, path, total + arr[i])  # Reuse element
                path.pop()  # Backtrack
                
        arr.sort()  # Optional: sort for ordered combinations
        backtrack(0, [], 0)
        return result

# Example usage:
sol = Solution()
print(sol.combinationSum([2, 4, 6, 8], 8))    # [[2,2,2,2],[2,2,4],[2,6],[4,4],[8]]
print(sol.combinationSum([2, 7, 6, 5], 16))   # [[2,2,2,2,2,2,2,2],[2,2,2,2,2,6],[2,2,2,5,5],[2,2,5,7],[2,2,6,6],[2,7,7],[5,5,6]]
print(sol.combinationSum([6, 5, 7], 8))       # []
