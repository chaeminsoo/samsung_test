# 17406
from itertools import permutations

n,m,k = map(int,input().split())
board = []
ordrs = []
for _ in range(n):
    board.append(list(map(int,input().split())))
for _ in range(k):
    ordrs.append(list(map(int,input().split())))

ordrs = list(permutations(ordrs,k))

ans = 1e9

def checking(l):
    rslt = 1e9
    for i in l:
        rslt = min(sum(i),rslt)
    return rslt

def at(b,r,c,n):
    for i in range(1,n+1):
        ref = b[r-i][c-i]
        for j in range(r-i,r+i):
            b[j][c-i] = b[j+1][c-i]
        for j in range(c-i,c+i):
            b[r+i][j] = b[r+i][j+1]
        for j in range(r+i,r-i,-1):
            b[j][c+i] = b[j-1][c+i]
        for j in range(c+i,c-i,-1):
            b[r-i][j] = b[r-i][j-1]
        b[r-i][c-i+1] = ref
    return b

for ordr in ordrs:
    ref_board = [i[:] for i in board]
    for i,j,k in ordr:
        ref_board = at(ref_board,i-1,j-1,k)
    ans = min(ans,checking(ref_board))

print(ans)