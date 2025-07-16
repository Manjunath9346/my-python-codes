class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if not arr:
            return []

        # Step 1: Find candidates using Boyer-Moore
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Validate candidates
        result = []
        if arr.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and arr.count(candidate2) > n // 3:
            result.append(candidate2)

        return sorted(result)
sol = Solution()

print(sol.findMajority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(sol.findMajority([1, 2, 3, 4, 5]))                   # Output: []
print(sol.findMajority([1, 1, 1]))                         # Output: [1]
print(sol.findMajority([1, 2, 3, 1, 2, 1, 2, 2]))           # Output: [1, 2]
