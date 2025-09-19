from collections import Counter

class Solution:
    def topKFrequent(self, arr, k):
        """
        Find the k most frequent elements, breaking ties by choosing the larger number.
        """
        freq = Counter(arr)  # Count frequencies
        # Sort by frequency descending, then by number descending
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
        return [num for num, count in sorted_items[:k]]  # Take top k elements

# Test cases
sol = Solution()

# Example 1
arr1 = [3, 1, 4, 4, 5, 2, 6, 1]
k1 = 2
print(sol.topKFrequent(arr1, k1))  # Output: [4, 1]

# Example 2
arr2 = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k2 = 4
print(sol.topKFrequent(arr2, k2))  # Output: [5, 11, 7, 10]

# Additional Test Case
arr3 = [1, 1, 1, 2, 2, 3]
k3 = 2
print(sol.topKFrequent(arr3, k3))  # Output: [1, 2]
Top K Frequent in Array
