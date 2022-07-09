# 17142
from itertools import combinations
from collections import deque

n,m = map(int,input().split())
board  = []
virus  =[]
znt = 0
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 2:
            virus.append((i,j))
        if data[j] == 0: 
            znt+=1 
    board.append(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(g,virs,znt):
    if znt == 0:
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

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny] and g[nx][ny] != 1:
                if g[nx][ny] == 0:
                    znt-=1
                q.append((nx,ny,t+1))
                min_t = max(min_t,t+1)
                visited[nx][ny] = True
                g[nx][ny] = 3
        if znt == 0:
            break

    if znt == 0:
        return min_t
    else:
        return -1

ans = 1e9
cases = combinations(virus,m)
for case in cases:
    ref = bfs([i[:] for i in board],case,znt)
    if ref == -1:
        continue
    else:
        ans = min(ref,ans)
if ans == 1e9:
    print(-1)
else:
    print(ans)