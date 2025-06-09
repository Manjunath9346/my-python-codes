
def getMaxGold(mine):
    m, n = len(mine), len(mine[0])
    maxGold = 0
    for j in range(0, n, 1):
        gold = getGold(mine, 0, j, m, n)
        print(gold, " ")
        maxGold = max(maxGold, gold)
    return maxGold

def getGold(mine, i, j, m, n):
    if (i > m-1) or  (j < 0) or (j > n-1):
        return 0
    else:
        opt1 = mine[i][j] + getGold(mine, i+1, j-1, m, n)
        opt2 = mine[i][j] + getGold(mine, i+1, j, m, n)
        opt3 = mine[i][j] + getGold(mine, i+1, j+1, m, n)
        return max(opt1, opt2, opt3)
        
mine = [[3,2,12,15,10],
        [6,19,7,11,17], 
        [8,5,12,32,21], 
        [3,20,2,9,7]]
print("\n", getMaxGold(mine))
