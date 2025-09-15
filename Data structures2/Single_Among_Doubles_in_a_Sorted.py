class Solution:
    def single(self, arr):
        n = len(arr)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even (pairs should start at even index)
            if mid % 2 == 1:
                mid -= 1

            if arr[mid] == arr[mid + 1]:
                # Pair is valid → single must be on right
                low = mid + 2
            else:
                # Pair breaks here → single is on left or at mid
                high = mid

        return arr[low]
sol = Solution()
print(sol.single([1,1,2,2,3,3,4,50,50,65,65]))  # 4
print(sol.single([5]))                          # 5
print(sol.single([1,2,2,3,3]))                  # 1
