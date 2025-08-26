import heapq

class Solution:
    def minCost(self, arr):
        if len(arr) <= 1:
            return 0

        heapq.heapify(arr)  # convert array into min-heap
        total_cost = 0

        while len(arr) > 1:
            # Pop two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)

            # Cost of connecting them
            cost = first + second
            total_cost += cost

            # Push back the new rope
            heapq.heappush(arr, cost)

        return total_cost
sol = Solution()

print(sol.minCost([4, 3, 2, 6]))     # Output: 29
print(sol.minCost([4, 2, 7, 6, 9])) # Output: 62
print(sol.minCost([10]))            # Output: 0
