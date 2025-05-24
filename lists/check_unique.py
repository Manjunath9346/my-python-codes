arr = tuple(map(int, input().split()))
arr1 = []
arr2 = []
for i in arr:
    if i in arr1:
        arr2.append(i)
    else:
        arr1.append(i)
if arr2:
    print("False")
else:
    print("True")
