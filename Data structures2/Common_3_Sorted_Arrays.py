class Solution:
    def commonElements(self, arr1, arr2, arr3):
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        result = []
        prev = None   # to avoid duplicates in result
        
        while i < n1 and j < n2 and k < n3:
            # If all three are equal
            if arr1[i] == arr2[j] == arr3[k]:
                if prev != arr1[i]:      # avoid duplicates
                    result.append(arr1[i])
                    prev = arr1[i]

                i += 1
                j += 1
                k += 1
            
            # Move the smallest pointer
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        
        # If no common elements
        if not result:
            return [-1]
        
        return result
obj = Solution()

print(obj.commonElements(
    [1, 5, 10, 20, 40, 80],
    [6, 7, 20, 80, 100],
    [3, 4, 15, 20, 30, 70, 80, 120]
))
# Expected: [20, 80]

print(obj.commonElements(
    [1, 2, 3, 4, 5],
    [6, 7],
    [8, 9, 10]
))
# Expected: [-1]

print(obj.commonElements(
    [1, 1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [1, 1, 1, 1, 2, 2, 2, 2]
))
# Expected: [1, 2]
