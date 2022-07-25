# 21609
from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def clock_turn(l):
    a = zip(*l[::-1])
    return [list(b) for b in a]

def gravity():
    for i in range(n-2,-1,-1):
        for j in range(n-1,-1,-1):
            if board[i][j] != -1 and board[i][j] != -2:
                cnt = 0
                while cnt < n:
                    if 0 <= i+cnt+1 < n and board[i+cnt+1][j] == -2:
                        cnt+=1
                    else:
                        break
                if cnt != 0:
                    board[i+cnt][j] = board[i][j]
                    board[i][j] = -2
                else:
                    continue
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def find_block_group():
    global ans
    group_board = [0]
    groups = []
    visited = [[False]*n for _ in range(n)]

    gnt = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] != 0 and board[i][j] != -1 and board[i][j] != -2:
                ref = board[i][j]
                temp_group = []
                zero_group = []
                cnt = 0
                rnt = 0
                visited[i][j] = True
                q = deque()
                q.append([i,j])
                while q:
                    x,y = q.popleft()
                    temp_group.append([x,y])
                    cnt += 1

                    for k in range(4):
                        nx = x+ dx[k]
                        ny = y+ dy[k]

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (board[nx][ny] == 0 or board[nx][ny] == ref):
                            if board[nx][ny] == 0:
                                rnt += 1
                                zero_group.append([nx,ny])
                            q.append([nx,ny])
                            visited[nx][ny] = True

                groups.append([gnt,cnt,rnt,i,j])
                group_board.append(temp_group)
                for ii,jj in zero_group:
                    visited[ii][jj] = False
                gnt+=1
    groups.sort(key= lambda x:(x[1], x[2], x[3], x[4]))
    try:
        target_group = groups.pop()
    except IndexError:
        return False
    if target_group[1] == 1:
        return False
    else:
        ans += (target_group[1])**2
        for i, j in group_board[target_group[0]]:
            board[i][j] = -2
        return True

while True:
    checking = find_block_group()
    if checking:
        gravity()
        for _ in range(3):
            board = clock_turn(board)
        gravity()
    else:
        break
print(ans)