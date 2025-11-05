import heapq

class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        min_heap = []
        
        # Push first element of each row into heap
        for r in range(n):
            heapq.heappush(min_heap, (mat[r][0], r, 0))
        
        # Extract min k-1 times
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (mat[r][c + 1], r, c + 1))
        
        return heapq.heappop(min_heap)[0]
print(Solution().kthSmallest([
    [16, 28, 60, 64],
    [22, 41, 63, 91],
    [27, 50, 87, 93],
    [36, 78, 87, 94]
], 3))  # ✅ Output: 27

print(Solution().kthSmallest([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [24, 29, 37, 48],
    [32, 33, 39, 50]
], 7))  # ✅ Output: 30

print(Solution().kthSmallest([[1, 2], [3, 4]], 2))  # ✅ Output: 2
print(Solution().kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6))  # ✅ Output: 11
print(Solution().kthSmallest([[5]], 1))  # ✅ Output: 5
