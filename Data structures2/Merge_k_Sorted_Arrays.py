import heapq

class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        heap = []
        res = []
        
        # Push first element of each row into heap
        for i in range(K):
            heapq.heappush(heap, (arr[i][0], i, 0))  # (value, row, col)
        
        while heap:
            val, r, c = heapq.heappop(heap)
            res.append(val)
            
            # If more elements in the same row, push next one
            if c + 1 < K:
                heapq.heappush(heap, (arr[r][c+1], r, c+1))
        
        return res
sol = Solution()

# Test 1
print(sol.mergeKArrays([[1,2,3],[4,5,6],[7,8,9]], 3))
# Expected: [1,2,3,4,5,6,7,8,9]

# Test 2
print(sol.mergeKArrays([[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]], 4))
# Expected: [1,2,2,2,3,3,4,4,5,5,6,6,7,8,9,9]

# Test 3
print(sol.mergeKArrays([[1]], 1))
# Expected: [1]

# Test 4
print(sol.mergeKArrays([[1,5,9],[2,6,10],[3,7,11],[4,8,12]], 4))
# Expected: [1,2,3,4,5,6,7,8,9,10,11,12]

# Test 5
print(sol.mergeKArrays([[10,20],[5,15]], 2))
# Expected: [5,10,15,20]
