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

def attck(board,loc,d):
    range_board = board[:]
    range_board.append([0]*m)
    r,c = loc
    q = deque()
    q.append([r,c,0])
    visited = [[False]*m for _ in range(n+1)]
    while q:
        x,y,v = q.popleft()
        range_board[x][y] = v

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                q.append([nx,ny,v+1])
                visited[nx][ny] = True
    hits = []
    for i in range(n):
        for j in range(m):
            if range_board[i][j] == d:
                hits.append([i,j])
    hits.sort(key= lambda x: x[1])
    return hits[0]

def checking(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 1:
                return False
    return True

def e_moving(b):
    new_b = b[:]
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 1:
                try:
                    new_b[i+1][j] = 1
                except IndexError:
                    pass
                b[i][j] = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] += new_b[i][j]
    return b

ans = 0
for i in archers:
    ref_board = board[:]
    archer_loc = [0]*m
    for j in i:
        archer_loc[j] = 1
    while checking:
        ref_board.append(archer_loc)
        hits = []
        for j in archer_loc:
            if j == 1:
                hit = attck(ref_board,[n,j],d)
                hits.append(hit)
        for j,k in hits:
            board[j][k] = 0
            ans+=1
        ref_board.pop()
        ref_board = e_moving(ref_board)
print(ans)