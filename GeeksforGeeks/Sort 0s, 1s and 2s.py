class Solution:
    def sort012(self, arr):
        # code here
        l = len(arr)
        z = []
        o = []
        t = []
        for i in range(l):
            if arr[i] == 0:
                z.append(arr[i])
            elif arr[i] == 1:
                o.append(arr[i])
            elif arr[i] == 2:
                t.append(arr[i])
        arr[:] = z+o+t
        return arr
