# 15683
n,m = map(int, input().split())
room = []
cctvs = []
for i in range(n):
    a = list(map(int,input().split()))
    room.append(a)
    for j in range(m):
        if a[j] != 0 and a[j] != 6:
            cctvs.append((a[j],i,j))
l = len(cctvs)

cctv_d = [
    [],
    [[0], [1], [2], [3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3], [3,0]],
    [[0,1,3], [0,1,2], [1,2,3], [0,2,3]],
    [[0,1,2,3]]
]
# clockwise
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def checking(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7
                    
ans = 1e9
def dfs(depth, arr):
    global ans

    if depth == l:
        cnt = 0
        for i in range(n):
            cnt += arr[i].count(0)
        ans = min(ans,cnt)
        return
    
    standard = [i[:] for i in arr]
    cctv_num, x, y = cctvs[depth]
    for i in cctv_d[cctv_num]:
        checking(standard,i,x,y)
        dfs(depth+1,standard)
        standard = [i[:] for i in arr]

dfs(0,room)
print(ans)