class Solution:
 
    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
    
    def merge(self, arr, l, m, r):
        # Create temporary arrays
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        i = j = 0
        k = l
        
        # Merge the temporary arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy any remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy any remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
arr1 = [4, 1, 3, 9, 7]
sol = Solution()
sol.mergeSort(arr1, 0, len(arr1) - 1)
print(arr1)  # Output: [1, 3, 4, 7, 9]

arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sol.mergeSort(arr2, 0, len(arr2) - 1)
print(arr2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr3 = [1, 3, 2]
sol.mergeSort(arr3, 0, len(arr3) - 1)
print(arr3)  # Output: [1, 2, 3]
