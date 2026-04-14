class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr = sorted(arr)
        l = len(arr)-1
        res = arr[-1] - arr[0]
        mini = 0
        maxi = 0
        for i in range(l):
            mini = min(arr[0]+k, arr[i+1]-k)
            maxi = max(arr[i]+k, arr[-1]-k)
            if mini < 0:
                continue
            min_diff = maxi - mini
            res = min(res, min_diff)
        return res
            
