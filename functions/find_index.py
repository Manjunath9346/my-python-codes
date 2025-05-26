def check_index(arr, x):
    if x in arr:
        return (arr.index(x))


arr = tuple(map(int, input().split()))
x = int(input())
print(check_index(arr, x))
