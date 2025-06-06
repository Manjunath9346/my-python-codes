# Problem 3: Rotate Array Left by k Positions


def rotate(arr, r):
    n = len(arr)
    for i in range(r):
        temp = arr[0]                   # has corrected
        for j in range(1, n):
            arr[j-1] = arr[j]
        arr[n-1] = temp
    return arr


# drive code

arr = list(map(int, input('enter list of array (separated by space): ').split(" ")))
r = int(input("enter rotation: "))
print(rotate(arr, r))
