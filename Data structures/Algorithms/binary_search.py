def binsearch(list1, left, right, key):
    pos = -1
    while left <= right:
        mid = (left + right)//2
        if key == list1[mid]:
            return mid
        elif key < list1[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return pos


list1 = [1,2,3,0,8,4,5,6,7,9]

key = int(input("enter: "))
list1 = sorted(list1)
left, right = 0, len(list1)-1

pos = binsearch(list1, left, right, key)

if pos < 0:
    print("not found")
else:
    print("found at position =", pos+1)
