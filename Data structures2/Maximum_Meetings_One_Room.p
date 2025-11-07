from typing import List

class Solution:
    def maxMeetings(self, N: int, S: List[int], F: List[int]) -> List[int]:
        # Combine start, finish, and meeting index
        meetings = [(F[i], S[i], i + 1) for i in range(N)]
        meetings.sort()  # Sort by finish time
        
        res = []
        last_end = -1
        
        for end, start, idx in meetings:
            if start > last_end:  # strictly greater condition
                res.append(idx)
                last_end = end
                
        return sorted(res)  # return meeting indices in sorted order
sol = Solution()

# Test Case 1
print(sol.maxMeetings(6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
#  Output: [1, 2, 4, 5]

# Test Case 2
print(sol.maxMeetings(1, [3], [7]))
#  Output: [1]

# Test Case 3
print(sol.maxMeetings(4, [0, 1, 3, 5], [2, 4, 6, 7]))
#  Output: [1, 2, 3, 4]
