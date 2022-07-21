# 20056
n,m,k = map(int,input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b,c,d,e = map(int,input().split())
    board[a-1][b-1].append([c,d,e])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def ball_move(r,c,d,s):
    global n
    nx = (r + s*dx[d])%n
    ny = (c + s*dy[d])%n
    return nx,ny,d,s

def ball_split():
    global n
    ref_board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) == 0:
                continue
            elif len(board[i][j]) == 1:
                ref_board[i][j].append(board[i][j][0])
            elif len(board[i][j]) >= 2:
                odd_check1 = len(board[i][j])
                mass_sum = 0
                odd_check2 = 0
                speed_sum = 0
                for m,s,d in board[i][j]:
                    mass_sum += m
                    speed_sum += s
                    if d%2 == 0:
                        odd_check2 += 1
                
                new_mass = mass_sum//5
                new_speed = speed_sum//odd_check1
                if odd_check1 == odd_check2 or odd_check2 == 0:
                    new_d = [0,2,4,6]
                else:
                    new_d = [1,3,5,7]
                
                if new_mass == 0:
                    continue
                else:
                    for l in new_d:
                        ref_board[i][j].append([new_mass,new_speed,l])
    return ref_board

cnt = 0
while cnt < k:
    ref_board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for m_,s_,d_ in board[i][j]:
                    ni,nj,nd,ns = ball_move(i,j,d_,s_)
                    ref_board[ni][nj].append([m_,ns,nd])
    board = ref_board
    board = ball_split()
    cnt += 1

ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            for k in board[i][j]:
                ans += k[0]
print(ans)