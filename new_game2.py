# 17837
n,k = map(int,input().split())
color_board = []
piece_board = [['']*n for _ in range(n)]
piece_info = []
for _ in range(n):
    color_board.append(list(map(int,input().split())))
for i in range(k):
    a,b,c = map(int,input().split())
    piece_info.append([a-1,b-1,c])
    piece_board[a-1][b-1] += str(i)
    
# 1~4: rlud
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

ans = 1
switch = False
while ans < 10:
    for p in range(k):
        x,y,d = piece_info[p]

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and color_board[nx][ny] != 2:
            if color_board[nx][ny] == 0:
                now = piece_board[x][y]
                idx = now.index(str(p))
                piece_board[x][y] = now[:idx]
                piece_board[nx][ny] += now[idx:]
                if len(piece_board[nx][ny]) >= 4:
                    switch = True
                    break
                for i in piece_board[nx][ny]:
                    i = int(i)
                    piece_info[i][0] = nx
                    piece_info[i][1] = ny

            elif color_board[nx][ny] == 1:
                now = piece_board[x][y]
                idx = now.index(str(p))
                piece_board[x][y] = now[:idx]
                piece_board[nx][ny] += now[idx:][::-1]
                if len(piece_board[nx][ny]) >= 4:
                    switch = True
                    break
                for i in piece_board[nx][ny]:
                    i = int(i)
                    piece_info[i][0] = nx
                    piece_info[i][1] = ny
        else:
            if d ==1: d = 2
            elif d ==2: d = 1
            elif d ==3: d = 4
            elif d ==4: d = 3
            piece_info[p][2] = d

            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and color_board[nx][ny] != 2:
                if color_board[nx][ny] == 0:
                    now = piece_board[x][y]
                    idx = now.index(str(p))
                    piece_board[x][y] = now[:idx]
                    piece_board[nx][ny] += now[idx:]
                    if len(piece_board[nx][ny]) >= 4:
                        switch = True
                        break
                    for i in piece_board[nx][ny]:
                        i = int(i)
                        piece_info[i][0] = nx
                        piece_info[i][1] = ny

                elif color_board[nx][ny] == 1:
                    now = piece_board[x][y]
                    idx = now.index(str(p))
                    piece_board[x][y] = now[:idx]
                    piece_board[nx][ny] += now[idx:][::-1]
                    if len(piece_board[nx][ny]) >= 4:
                        switch = True
                        break
                    for i in piece_board[nx][ny]:
                        i = int(i)
                        piece_info[i][0] = nx
                        piece_info[i][1] = ny
                else:
                    continue
    if switch:
        break
    ans +=1

if ans > 1000:
    print(-1)
else:
    print(ans)