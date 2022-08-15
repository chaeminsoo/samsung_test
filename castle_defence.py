# 17135
from itertools import combinations
from collections import deque

n,m,d = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
a = [i  for i in range(m)]
archers = list(combinations(a,3))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def attack(b,r,c,d):
    range_board = [[0]*m for _ in range(n+1)]
    visited = [[False]*m for _ in range(n+1)]
    q = deque()
    q.append([r,c,0])
    visited[r][c] = True
    while q:
        x,y,v = q.popleft()
        range_board[x][y] = v

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n+1 and 0 <= ny < m and not visited[nx][ny]:
                q.append([nx,ny,v+1])
                visited[nx][ny] = True
    hits = []
    for i in range(n):
        for j in range(m):
            if range_board[i][j] <= d and b[i][j] == 1:
                hits.append([i,j,range_board[i][j]])
    hits.sort(key= lambda x:(x[2], x[1]))
    if hits:
        return hits[0][:2]
    else:
        return

def done_(b):
    for i in range(n):
        for j in range(m):
            if b[i][j] == 1:
                return False
    return True

def moving(b,ar):
    ref = [[0]*m for _ in range(n)]
    ref.append(ar)
    for i in range(n):
        for j in range(m):
            if i == n-1 and b[i][j] == 1:
                continue
            if b[i][j] == 1:
                ref[i+1][j] = 1
    return ref

ans = 0
for i in archers:
    arch_row = [0]*m
    for j in range(m):
        if j in i:
            arch_row[j] = -1
    ref_board = [ii[:] for ii in board]
    ref_board.append(arch_row)
    cnt = 0
    while not done_(ref_board):
        hits = []
        for j, k in enumerate(ref_board[n]):
            if k == -1:
                hit = attack(ref_board,n,j,d)
                if hit:
                    hits.append(hit)
        for j,k in hits:
            if ref_board[j][k] == 1:
                ref_board[j][k] = 0
                cnt += 1
        ref_board = moving(ref_board,arch_row)
    ans = max(ans,cnt)
print(ans)