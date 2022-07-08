# 17142
from itertools import combinations
from collections import deque

n,m = map(int,input().split())
board  = []
virus  =[]
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 2:
            virus.append((i,j))
    board.append(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def checking(b):
    for i in range(n):
        for j in range(n):
            if b[i][j] == 0:
                return False
    return True

def bfs(g,virs):
    if checking(g):
        return 0
    q = deque()
    min_t = 0
    visited = [[False]*n for _ in range(n)]
    for v in virs:
        r,c = v
        g[r][c] = 3
        q.append((r,c,0))
        visited[r][c] = True
    while q:
        x,y,t = q.popleft()
        min_t = max(min_t,t)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny] and g[nx][ny] != 1:
                if g[nx][ny] == 2:
                    q.append((nx,nx,t))
                else:
                    q.append((nx,nx,t+1))
                visited[nx][ny] = True
                g[nx][ny] = 3

    if checking(g):
        return min_t
    else:
        return -1

ans = 1e9
cases = combinations(virus,m)
for case in cases:
    ans = min(bfs([i[:] for i in board],case),ans)

print(ans)