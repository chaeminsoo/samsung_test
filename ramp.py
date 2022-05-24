# 14890
n,l = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
    
ans = 0
for i in board:
    st = 0
    ed = 1
    