class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	count = 0
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        arr[count], arr[i] = arr[i], arr[count]
    	        count += 1
        return arr
obj = Solution()
print(obj.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
print(obj.pushZerosToEnd([10, 20, 30]))              # [10, 20, 30]
print(obj.pushZerosToEnd([0, 0]))                    # [0, 0]
