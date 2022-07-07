# 17142
from itertools import combinations

n,m = map(int,input().split())
board = []
virus = []
for i in range(n):
    info = list(map(int,input().split()))
    for j in range(n):
        if info[j] == 2:
            virus.append((i,j))
    board.append(info)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

previous = [p[:] for p in board]

def diffusion():
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 3:
                for k in range(k):
                    nx = i + dx[k]
                    ny = i + dy[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] != 1 and board[nx][ny] != 3:
                        new_board[nx][ny] = 3
    for i in range(n):
        for j in range(n):
            if new_board[i][j] == 3:
                board[i][j] = 3
    if board == previous:
        return True
    else:
        previous = [p[:] for p in board]
        return False

def cheaking():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return True
    return False
# def dfs(a,b,c,cnt,swit,m):
#     if swit:
#         for i in range(n):
#             for j in range(n):
#                 if board[i][j] == 0:
#                     return -1
#             return cnt
#     swit = diffusion()
#     cnt += 1
test_set = list(combinations(virus,m))
chk = False
ans = 1e9
for i in test_set:
    for j in i:
        x,y = j
        board[x][y] = 3
    cnt = 0
    if cheaking():
        chk = True
        break
    while diffusion():
        cnt += 1
    
    if chk:
        ans = -1
        break
    else:
        ans = min(ans,cnt)

print(ans)