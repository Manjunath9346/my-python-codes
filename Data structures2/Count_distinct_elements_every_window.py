from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        freq = defaultdict(int)
        result = []
        
        # Initialize the first window
        for i in range(k):
            freq[arr[i]] += 1
        result.append(len(freq))
        
        # Slide the window
        for i in range(k, len(arr)):
            # Remove the first element of previous window
            freq[arr[i - k]] -= 1
            if freq[arr[i - k]] == 0:
                del freq[arr[i - k]]
            
            # Add the new element
            freq[arr[i]] += 1
            
            result.append(len(freq))
        
        return result
# Test Case 1
print(Solution().countDistinct([1, 2, 1, 3, 4, 2, 3], 4))  # Output: [3, 4, 4, 3]

# Test Case 2
print(Solution().countDistinct([4, 1, 1], 2))              # Output: [2, 1]

# Test Case 3
print(Solution().countDistinct([1, 1, 1, 1, 1], 3))         # Output: [1, 1, 1]

# Test Case 4
print(Solution().countDistinct([1, 2, 3, 4, 5], 3))         # Output: [3, 3, 3]
