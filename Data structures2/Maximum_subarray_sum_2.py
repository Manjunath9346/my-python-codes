import heapq

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        
        # prefix sums
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + arr[i-1]
        
        ans = float("-inf")
        min_heap = []          # stores prefix values (min-heap)
        count_map = {}         # for lazy deletion (to remove old values)
        
        for r in range(a, n+1):
            # add new prefix[r-a]
            val = prefix[r-a]
            heapq.heappush(min_heap, val)
            count_map[val] = count_map.get(val, 0) + 1
            
            # remove prefix[r-b-1] if it exists (out of window)
            if r-b-1 >= 0:
                old_val = prefix[r-b-1]
                count_map[old_val] -= 1
            
            # clean heap top (lazy deletion)
            while min_heap and count_map[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            
            # compute max sum using smallest prefix in window
            ans = max(ans, prefix[r] - min_heap[0])
        
        return ans
sol = Solution()

print(sol.maxSubarrSum([4, 5, -1, -2, 6], 2, 4))  # Expected 9
print(sol.maxSubarrSum([-1, 3, -1, -2, 5, 3, -5, 2, 2], 3, 5))  # Expected 8
print(sol.maxSubarrSum([10], 1, 1))  # Expected 10
print(sol.maxSubarrSum([-5, -2, -3], 1, 2))  # Expected -2
print(sol.maxSubarrSum([1, 2, 3, 4, 5], 2, 5))  # Expected 15
