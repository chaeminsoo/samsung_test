# 23288
from collections import deque

n,m,k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

# udfblr
# 012345
dice = [1,6,5,2,4,3,0,0,1]

def dice_move(dice,d):
    if d == 0:
        ref_dice = [dice[2],dice[3],dice[1],dice[0],dice[4],dice[5],dice[6],dice[7],dice[8]]
    if d == 1:
        ref_dice = [dice[4],dice[5],dice[2],dice[3],dice[1],dice[0],dice[6],dice[7],dice[8]]
    if d == 2:
        ref_dice = [dice[3],dice[2],dice[0],dice[1],dice[4],dice[5],dice[6],dice[7],dice[8]]
    if d == 3:
        ref_dice = [dice[5],dice[4],dice[2],dice[3],dice[0],dice[1],dice[6],dice[7],dice[8]]
    return ref_dice

# d: clock
def choose_d(x,y,dice,d):
    if dice[1] > board[x][y]:
        return (d+1)%4
    if dice[1] == board[x][y]:
        return d
    if dice[1] < board[x][y]:
        return (d+3)%4

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def get_score(r,c):
    visited = [[False]*m for _ in range(n)]
    ref = board[r][c]
    cnt = 0
    q = deque()
    q.append([r,c])
    visited[r][c] = True
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == ref and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = True
    return cnt*ref

ans = 0
for _ in range(k):
    x,y,d = dice[-3:]
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= n or nx < 0 or ny >= m or ny < 0:
        d = (d+2)%4
        nx = x + dx[d]
        ny = y + dy[d]
    dice[-3] = nx
    dice[-2] = ny
    dice = dice_move(dice,d)
    ans += get_score(nx,ny)
    dice[-1] = choose_d(nx,ny,dice,d)

print(ans)