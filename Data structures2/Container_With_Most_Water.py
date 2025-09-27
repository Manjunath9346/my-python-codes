class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        max_area = 0

        while left < right:
            # width between lines
            width = right - left
            # height of container = min of both heights
            height = min(arr[left], arr[right])
            # calculate area
            max_area = max(max_area, width * height)

            # move the pointer of smaller line inward
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_area
if __name__ == "__main__":
    sol = Solution()

    print(sol.maxWater([1, 5, 4, 3]))            # Expected 6
    print(sol.maxWater([3, 1, 2, 4, 5]))         # Expected 12
    print(sol.maxWater([2, 1, 8, 6, 4, 6, 5, 5])) # Expected 25
    print(sol.maxWater([1, 1]))                  # Expected 1
    print(sol.maxWater([0, 0, 0, 0]))            # Expected 0
