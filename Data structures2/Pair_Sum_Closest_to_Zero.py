class Solution:
    def closestToZero(self, arr, n):
        # Sort the array to use two pointers
        arr.sort()
        
        left, right = 0, n - 1
        closest_sum = float('inf')
        
        while left < right:
            curr_sum = arr[left] + arr[right]
            
            # If this sum is closer to zero
            if abs(curr_sum) < abs(closest_sum) or (abs(curr_sum) == abs(closest_sum) and curr_sum > closest_sum):
                closest_sum = curr_sum
            
            # Move pointers to get closer to zero
            if curr_sum < 0:
                left += 1
            else:
                right -= 1
                
        return closest_sum
arr = [-8, -66, -60]
n = len(arr)
# Expected Output: -68
# Explanation: Closest pair (-60, -8) → sum = -68
