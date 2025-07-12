class Solution:
    def minSwaps(self, arr):
        n = len(arr)
        # Pair element with its original index
        arrpos = [(val, idx) for idx, val in enumerate(arr)]
        # Sort based on values
        arrpos.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            # If already visited or already in correct position
            if visited[i] or arrpos[i][1] == i:
                continue

            # Compute the cycle size
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][1]
                cycle_size += 1

            # If cycle has more than one node, we need (size - 1) swaps
            if cycle_size > 1:
                swaps += (cycle_size - 1)

        return swaps
sol = Solution()

# Test Case 1
print(sol.minSwaps([2, 8, 5, 4]))  
# Output: 1

# Test Case 2
print(sol.minSwaps([10, 19, 6, 3, 5]))  
# Output: 2

# Test Case 3
print(sol.minSwaps([1, 3, 4, 5, 6]))  
# Output: 0

# Test Case 4
print(sol.minSwaps([4, 3, 2, 1]))  
# Output: 2
