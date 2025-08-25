class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if arr[mid] is peak
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
                return mid
            # If left neighbor is greater, move left
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:  # Otherwise move right
                low = mid + 1
        return -1  # Should not reach here

# Test cases
sol = Solution()

arr1 = [1, 2, 4, 5, 7, 8, 3]
print(sol.peakElement(arr1))  # Possible output: 5 (element 8)

arr2 = [10, 20, 15, 2, 23, 90, 80]
print(sol.peakElement(arr2))  # Possible outputs: 1 (element 20) or 5 (element 90)

arr3 = [5]
print(sol.peakElement(arr3))  # Output: 0 (single element is always peak)
