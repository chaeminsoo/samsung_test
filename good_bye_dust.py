# 17144
r,c,t = map(int,input().split())
cleaner = []
board = []
for i in range(r):
    ref = list(map(int,input().split()))
    if ref[0] == -1:
        cleaner.append(i)
    board.append(ref)
cleaner_u, cleaner_d = cleaner

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def diffusion():
    new_board = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            dust = board[i][j]
            new_d = dust//5
            if new_d <= 0:
                continue
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >=0 and nx < r and ny >=0 and ny < c and board[nx][ny] != -1:
                    new_board[nx][ny] += new_d
                    cnt+=1
            board[i][j] -= new_d*cnt
    return new_board

def dust_sum(nb):
    for i in range(r):
        for j in range(c):
            board[i][j] += nb[i][j]

def air_clean():
    ut, ul, ub, ur = 0, 0, cleaner_u, c-1
    temp = board[ut][ul]
    for k in range(ul, ur):
        board[ut][k] = board[ut][k+1]
    for k in range(ut, ub):
        board[k][ur] = board[k+1][ur]
    for k in range(ur, ul,-1):
        board[ub][k] = board[ub][k-1]
    for k in range(ub, ut, -1):
        board[k][ul] = board[k-1][ul]
    board[ut+1][ul] = temp
    board[cleaner_u][0] = -1
    board[cleaner_u][1] = 0

    dt, dl, db, dr = cleaner_d, 0, r-1, c-1
    temp = board[dt][dl]
    for k in range(dt, db):
        board[k][dl] = board[k+1][dl]
    for k in range(dl, dr):
        board[db][k] = board[db][k+1]
    for k in range(db, dt, -1):
        board[k][dr] = board[k-1][dr]
    for k in range(dr, dl,-1):
        board[dt][k] = board[dt][k-1]
    board[dt][dl+1] = temp
    board[cleaner_d][0] = -1
    board[cleaner_d][1] = 0

for _ in range(t):
    nboard = diffusion()
    dust_sum(nboard)
    air_clean()

ans = 0
for i in range(r):
    for j in range(c):
        ans += board[i][j]
print(ans+2)