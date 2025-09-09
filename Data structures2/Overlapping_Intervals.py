class Solution:
    def mergeOverlap(self, arr):
        # Sort intervals by start time
        arr.sort(key=lambda x: x[0])
        
        merged = []
        for interval in arr:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


# Test Cases
sol = Solution()
print(sol.mergeOverlap([[1, 3], [2, 4], [6, 8], [9, 10]]))  # [[1, 4], [6, 8], [9, 10]]
print(sol.mergeOverlap([[6, 8], [1, 9], [2, 4], [4, 7]]))   # [[1, 9]]
print(sol.mergeOverlap([[1, 2], [3, 4], [5, 6]]))           # [[1, 2], [3, 4], [5, 6]]
print(sol.mergeOverlap([[1, 10], [2, 3], [4, 8]]))          # [[1, 10]]
print(sol.mergeOverlap([[5, 5], [1, 2]]))                   # [[1, 2], [5, 5]]
