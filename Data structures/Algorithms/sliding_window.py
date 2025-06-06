
#  Problem 4: Maximum Sum Subarray of Size k (Sliding Window)

import array

def max_sub_arr(arr, l):
    n = len(arr)
    maxi = 0
    for i in range(n - l + 1):
        Sum = 0
        for j in range(l):
            Sum += arr[i + j]
        if Sum > maxi:
            maxi = Sum
    return maxi

arr = array.array('i', [2, 1, 5, 1, 3, 2])
l = int(input("enter l: "))
print(max_sub_arr(arr, l))
