# 19238
from collections import deque

n,m,f = map(int,input().split())
board = []
st = []
ed = []
for _ in range(n):
    board.append(list(map(int,input().split())))
taxi =list( map(int,input().split()))
visited = [[False]*n for _ in range(n)]
for i in range(2):
    taxi[i] -= 1
for i in range(m):
    a,b,c,d = map(int,input().split())
    st.append((a-1,b-1,i))
    ed.append((c-1,d-1,i))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs1(brd):
    global f, taxi,visited
    local_visited = [[False]*n for _ in range(n)]
    ref_board = [i[:] for i in brd]
    q = deque()
    q.append((taxi[0],taxi[1]))
    local_visited[taxi[0]][taxi[1]] = True
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and 0 <= ny < n and ref_board[nx][ny] != 1 and not local_visited[nx][ny]:
                ref_board[nx][ny] = ref_board[x][y] +1
                q.append((nx,ny))
                local_visited[nx][ny] = True
    ppls = []
    for r,c,num in st:
        if visited[r][c]:
            continue
        elif local_visited[r][c]:
            ppls.append((ref_board[r][c],r,c,num))
    try:            
        g,r,c,nm = min(ppls)
    except ValueError:
        return False, False
    visited[r][c] = True
    if f >= g:
        f -= g
        taxi = [r,c]
        return True, nm
    else:
        return False, False

def bfs2(brd,num):
    global f, taxi,visited
    local_visited = [[False]*n for _ in range(n)]
    ref_board = [i[:] for i in brd]
    q = deque()
    q.append((taxi[0],taxi[1]))
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and 0 <= ny < n and ref_board[nx][ny] != 1 and not local_visited[nx][ny]:
                ref_board[nx][ny] = ref_board[x][y] +1
                q.append((nx,ny))
                local_visited[nx][ny] = True
    r,c,nm = ed[num]
    if not local_visited[r][c]:
        return False
    g = ref_board[r][c]
    if f >= g:
        f-=g
        taxi = [r,c]
        f+=(g*2)
        return True
    else:
        return False

cnt = 0
ans = True
while cnt < m:
    rslt, goal = bfs1(board)
    if rslt:
        if bfs2(board,goal):
            cnt +=1
        else:
            ans = False
            break
    else:
        ans = False
        break
if ans:
    print(f)
else:
    print(-1)