class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        def can_place_cows(distance):
            count = 1
            last_position = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                if count >= k:
                    return True
            return False

        low, high = 1, stalls[-1] - stalls[0]
        best = 0

        while low <= high:
            mid = (low + high) // 2
            if can_place_cows(mid):
                best = mid
                low = mid + 1  # Try for a bigger distance
            else:
                high = mid - 1

        return best
# Test Case 1
stalls = [1, 2, 4, 8, 9]
k = 3
print(Solution().aggressiveCows(stalls, k))  
# Expected Output: 3

# Test Case 2
stalls = [10, 1, 2, 7, 5]
k = 3
print(Solution().aggressiveCows(stalls, k))  
# Expected Output: 4

# Test Case 3
stalls = [2, 12, 11, 3, 26, 7]
k = 5
print(Solution().aggressiveCows(stalls, k))  
# Expected Output: 1
