import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        min_heap = []
        result = []
        
        for num in arr:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
            # If we have fewer than k elements, Kth largest doesn't exist
            if len(min_heap) < k:
                result.append(-1)
            else:
                result.append(min_heap[0])  # The root of min-heap is Kth largest
        
        return result


# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    k1, arr1, n1 = 4, [1, 2, 3, 4, 5, 6], 6
    print(sol.kthLargest(k1, arr1, n1))  # Output: [-1, -1, -1, 1, 2, 3]
    
    k2, arr2, n2 = 1, [3, 4], 2
    print(sol.kthLargest(k2, arr2, n2))  # Output: [3, 4]
    
    k3, arr3, n3 = 3, [5, 2, 1, 4, 3], 5
    print(sol.kthLargest(k3, arr3, n3))  # Output: [-1, -1, 1, 2, 3]
