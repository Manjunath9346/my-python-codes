class Solution:
    def findMissing(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]  # trivial

        # compute consecutive differences
        diffs = [arr[i] - arr[i-1] for i in range(1, n)]

        # determine the common difference d robustly
        if diffs[0] > 0:
            d = min(diffs)   # increasing sequence -> smallest positive step
        else:
            d = max(diffs)   # decreasing sequence -> largest (least negative) step

        # find the place where difference breaks
        for i in range(1, n):
            if arr[i] - arr[i-1] != d:
                return arr[i-1] + d

        # if no break, return next element in AP
        return arr[-1] + d

print(Solution().findMissing([2, 4, 8, 10, 12, 14]))  #  6
print(Solution().findMissing([1, 6, 11, 16, 21, 31])) #  26
print(Solution().findMissing([4, 7, 10, 13, 16]))     #  19
print(Solution().findMissing([20, 15, 10, 0]))        #  5 (Descending AP)
