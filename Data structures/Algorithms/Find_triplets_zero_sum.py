class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        n = len(arr)
        arr.sort()
        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                total = arr[i] + arr[l] + arr[r]
                if total == 0:
                    return True
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return False
sol = Solution()

# Test Case 1: Valid triplet exists
print(sol.findTriplets([0, -1, 2, -3, 1]))  # Expected: True

# Test Case 2: No such triplet
print(sol.findTriplets([1, 2, 3]))  # Expected: False

# Test Case 3: Triplet using negative and positive numbers
print(sol.findTriplets([-5, 3, 2, -1, 0, 1]))  # Expected: True

# Test Case 4: All elements are zero
print(sol.findTriplets([0, 0, 0]))  # Expected: True

# Test Case 5: Only two elements
print(sol.findTriplets([1, -1]))  # Expected: False

# Test Case 6: Larger array, multiple valid triplets
print(sol.findTriplets([-10, 1, 2, -1, -2, 3, 4, 5, -3]))  # Expected: True

# Test Case 7: No triplet, all positive
print(sol.findTriplets([1, 2, 4, 5, 6]))  # Expected: False
