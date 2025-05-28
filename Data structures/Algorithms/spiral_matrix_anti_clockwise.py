matrix = [[1,2,3,4], 
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

n = len(matrix)

top, bottom, left, right, seed = 0, n-1, 0, n-1, 0

while top <= bottom and left <= right:
    # on left fromtop to bottom
    for row in range(top, bottom+1, 1):
        print(matrix[row][left], end = " ")
    # set left to col right of it
    left = left + 1
    # on bottom  from left to right
    for col in range(left, right+1, 1):
        print(matrix[bottom][col], end = " ")
    # set bottom to row above it
    bottom = bottom - 1
    # on rgiht move from bottom to top
    for row in range(bottom, top-1, -1):
        print(matrix[row][right], end = " ")
    # set right to its immediate left col
    right = right - 1
    # on top move from right to left
    for col in range(right, left-1, -1):
        print(matrix[top][col], end = " ")
    # set top to row immediately below it
    top = top + 1
