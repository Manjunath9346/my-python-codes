from collections import Counter

class Solution:
    # Function to sort the array according to frequency of elements.
    def sortByFreq(self, arr):
        freq = Counter(arr)  # Count frequency of each element
        # Sort by (-frequency, element) -> decreasing frequency, increasing element if tie
        arr.sort(key=lambda x: (-freq[x], x))
        return arr
sol = Solution()

# Test 1
print(sol.sortByFreq([5, 5, 4, 6, 4]))  
# Output: [4, 4, 5, 5, 6]

# Test 2
print(sol.sortByFreq([9, 9, 9, 2, 5]))  
# Output: [9, 9, 9, 2, 5]

# Test 3
print(sol.sortByFreq([1,2,3,4,5]))  
# Output: [1,2,3,4,5] (all frequency 1, sorted increasing)

# Test 4
print(sol.sortByFreq([3,3,3,2,2,1]))  
# Output: [3,3,3,2,2,1]
