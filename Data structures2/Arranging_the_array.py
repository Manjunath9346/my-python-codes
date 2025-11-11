from typing import List

class Solution:
    def Rearrange(self, n: int, arr: List[int]) -> None:
        # Separate negatives and non-negatives while maintaining order
        negatives = [x for x in arr if x < 0]
        non_negatives = [x for x in arr if x >= 0]
        
        # Combine them back into original array
        arr[:] = negatives + non_negatives
sol = Solution()

arr1 = [-3, 3, -2, 2]
sol.Rearrange(len(arr1), arr1)
print(arr1)  #  Output: [-3, -2, 3, 2]

arr2 = [-3, 1, 0, -2]
sol.Rearrange(len(arr2), arr2)
print(arr2)  #  Output: [-3, -2, 1, 0]

arr3 = [1, 2, 3, -1, -2, -3]
sol.Rearrange(len(arr3), arr3)
print(arr3)  #  Output: [-1, -2, -3, 1, 2, 3]

arr4 = [0, -1, 2, -3, 4, -5]
sol.Rearrange(len(arr4), arr4)
print(arr4)  #  Output: [-1, -3, -5, 0, 2, 4]
