import heapq

class Solution:
    def nearlySorted(self, arr, k):  
        n = len(arr)
        heap = []
        idx = 0
        
        # Step 1: Push first k+1 elements into min heap
        for i in range(min(k + 1, n)):
            heapq.heappush(heap, arr[i])
        
        # Step 2: For remaining elements, pop smallest and push new
        for i in range(k + 1, n):
            arr[idx] = heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
            idx += 1
        
        # Step 3: Pop remaining elements from heap
        while heap:
            arr[idx] = heapq.heappop(heap)
            idx += 1
        
        return arr
print(Solution().nearlySorted([2, 3, 1, 4], 2))   # [1, 2, 3, 4]
print(Solution().nearlySorted([7, 9, 14], 1))     # [7, 9, 14]
print(Solution().nearlySorted([6, 5, 3, 2, 8, 10, 9], 3))  # [2, 3, 5, 6, 8, 9, 10]
