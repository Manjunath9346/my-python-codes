from typing import List
from collections import deque

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        MOD = 100000
        dist = [float('inf')] * MOD
        dist[start] = 0

        queue = deque()
        queue.append((start, 0))

        while queue:
            num, steps = queue.popleft()

            if num == end:
                return steps

            for multiplier in arr:
                new_num = (num * multiplier) % MOD
                if dist[new_num] > steps + 1:
                    dist[new_num] = steps + 1
                    queue.append((new_num, steps + 1))

        return -1
arr = [2, 5, 7]
start = 3
end = 30
print(Solution().minimumMultiplications(arr, start, end))  # Output: 2
