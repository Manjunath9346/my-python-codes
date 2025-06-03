import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # Convert list into a min-heap
        heapq.heapify(arr)
        
        # Remove k-1 smallest elements
        for _ in range(k - 1):
            heapq.heappop(arr)
        
        # The kth smallest element
        return heapq.heappop(arr)


# Driver Code
if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    sol = Solution()
    result = sol.kthSmallest(arr, k)
    print(f"{k}rd smallest element is: {result}")  # Output: 7
