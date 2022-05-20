n,m = map(int,input().split())
r,c,d = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
cnt = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]

bx = [1,0,-1,0]
by = [0,1,0,-1]

robot = [r,c,d]
def moving(rob):
    x,y,d = rob
    nx = x +dx[d]
    ny = y +dy[d]
    if board[nx][ny] == 0:
        return [nx,ny,(d+1)%4],0
    else:
        return [x,y,(d+1)%4],1

turn_cnt = 0
while turn_cnt < 100:
    if board[robot[0]][robot[1]] == 0:
        cnt+=1
        board[robot[0]][robot[1]] = 2

    robot,check_ = moving(robot)
    if check_ == 1:
        turn_cnt+=1
    else:
        turn_cnt = 0

    if turn_cnt >= 4:
        if board[robot[0]+bx[robot[2]]][robot[1]+by[robot[2]]] == 1:
            break
        else:
            robot = [robot[0]+bx[robot[2]], robot[1]+by[robot[2]], robot[2]]
            turn_cnt = 0
print(cnt)