import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        # Sort both arrays in descending order
        a.sort(reverse=True)
        b.sort(reverse=True)

        n = len(a)
        max_heap = []
        visited = set()

        # Initial sum combination (a[0] + b[0]) with indices (0, 0)
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))

        result = []

        while k > 0 and max_heap:
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-current_sum)

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

            k -= 1

        return result
sol = Solution()
print(sol.topKSumPairs([3, 2], [1, 4], 2))  # Output: [7, 6]
print(sol.topKSumPairs([1, 4, 2, 3], [2, 5, 1, 6], 3))  # Output: [10, 9, 9]
