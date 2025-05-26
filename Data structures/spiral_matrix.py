
n = 10
arr = [[0 for j in range(n)] for i in range(n)]

top, bottom, left, right = 0, n-1, 0, n-1
seed = 1
while top < bottom and left <= right:
    for col in range(left, right+1, 1):
        arr[top][col] = seed
        seed = seed + 1     
    top = top +1
    # in right col travel from top to bottom
    for row in range(top, bottom+1, 1):
        arr[row][right] = seed
        seed = seed + 1
    right = right - 1
    # in right row travel from right to left 
    for col in range(right, left-1, -1):
        arr[bottom][col] = seed
        seed = seed + 1
    # change bottom row to its next upper one
    bottom = bottom - 1
    for row in range(bottom, top-1, -1):
        arr[row][left] = seed
        seed = seed + 1
    # step into next left column
    left = left + 1


for i in range(n):
    for j in range(n):
        print("%4d"%(arr[i][j]), end = " ")
    print()
