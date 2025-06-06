#1. linear search

import array

def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"'{i}' found at position"
    else:
        return f"Not Found!"
arr = array.array('i', [10, 20, 30, 40, 50, 60])
target = int(input("enter number to find: "))
print(linearsearch(arr, target))
