class Solution:
    def nextPermutation(self, arr):
        # code here
        l = len(arr)-1
        k = len(arr)-2
        
        while k >= 0 and arr[k] >= arr[k+1]:
            k -= 1
        
        if k >= 0:
            while arr[l] <= arr[k]:
                l -= 1
            arr[k], arr[l] = arr[l], arr[k]
        
        arr[k+1:] = arr[k+1:][::-1]
        return arr

arr = [2,3,6,8,1,5,4,9]
obj = Solution()
print(obj.nextPermutation(arr))
