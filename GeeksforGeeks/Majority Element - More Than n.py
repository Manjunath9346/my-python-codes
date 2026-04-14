class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        k = n//3
        dict1 = {}
        m = []
        for i in arr:
            if i not in dict1:
                dict1[i] = 1
            elif i in dict1:
                dict1[i] += 1
        for i,j in dict1.items():
            if j > k:
                m.append(i)
        return sorted(m)
