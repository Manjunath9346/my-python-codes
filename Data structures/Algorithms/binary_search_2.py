#2. binary search

def binarysearch(arr, target):
    arr = sorted(arr)
    n = len(arr)
    left, right = 0, n - 1
    mid = (left+right)//2
    while left < right:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = left - 1
        elif arr[mid] > target:
            right = right + 1
    return -1


arr = [1,2,3,4,5,6,7]
target = int(input("enter a number: "))
print(binarysearch(arr, target))
