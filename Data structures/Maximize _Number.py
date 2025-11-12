class Solution:
    def maxOnes(self, arr, k):
        left = 0
        max_len = 0
        zero_count = 0
        
        for right in range(len(arr)):
            # Count zeros in the current window
            if arr[right] == 0:
                zero_count += 1
            
            # Shrink the window if zeros exceed k
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update max window size
            max_len = max(max_len, right - left + 1)
        
        return max_len
sol = Solution()

print(sol.maxOnes([1, 0, 1], 1))                # ✅ Output: 3
print(sol.maxOnes([1, 0, 0, 1, 0, 1, 0, 1], 2)) # ✅ Output: 5
print(sol.maxOnes([1, 1], 2))                   # ✅ Output: 2
print(sol.maxOnes([0, 0, 0, 1, 1, 1, 0], 3))    # ✅ Output: 7
print(sol.maxOnes([1, 0, 1, 1, 0, 0, 1], 1))    # ✅ Output: 4
