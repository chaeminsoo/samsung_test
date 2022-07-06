# 17143
r,c,m = map(int,input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x,y,s,d,z = map(int,input().split())
    board[x-1][y-1].append((s,d,z))

dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]

def shark_move():
    new_board = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                for shark in board[i][j]:
                    x,y = i,j
                    s,d,z = shark
                    cnt = s
                    while s>0:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx < 0 or nx >= r or ny <0 or ny >= c:
                            if d == 1:
                                d = 2
                            elif d == 2:
                                d = 1
                            elif d == 3:
                                d = 4
                            elif d == 4:
                                d = 3
                            continue
                        s-=1
                        x,y = nx,ny
                    new_board[x][y].append((cnt,d,z))
    
    for i in range(r):
        for j in range(c):
            if new_board[i][j]:
                new_board[i][j].sort(reverse=True, key=lambda x:x[2])
                new_board[i][j] = new_board[i][j][:1]
    return new_board

def fishing(num):
    ref = (0,0,0)
    for i in range(r):
        if board[i][num]:
            ref = board[i][num].pop()
            break
    return ref[2]

ans = 0
for i in range(c):
    ans+= fishing(i)
    board = shark_move()
print(ans)