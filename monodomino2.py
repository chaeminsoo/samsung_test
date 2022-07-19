# 20061
n = int(input())
orders = []
for _ in range(n):
    t,a,b = map(int,input().split())
    orders.append([t,a,b])

green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]

def green_blue(t,x,y):
    if t == 0:
        return t,x,y,t,y,x
    elif t == 1:
        return t,x,y,t+1,y,x
    elif t == 2:
        return t,x,y,t-1,y,x

def block_shoot(board,t,x,y):
    if t == 0:
        for i in range(6):
            if board[i][y] == 0 and (board[i+1][y] == 1 or i == 5):
                board[i][y] = 1
                break
    elif t == 1:
        for i in range(6):
            if board[i][y] == 0 and board[i][y+1] == 0 and (i == 5 or board[i+1][y] == 1 or board[i+1][y+1] == 1): 
                board[i][y] == 1
                board[i][y+1] == 1
                break
    elif t == 2:
        for i in range(5):
            if board[i][y] == 0 and board[i+1][y] == 0 and (i == 4 or board[i+2][y] == 1):
                board[i][y] == 1
                board[i+1][y] == 1
                break
    return

def block_clear1(board):
    cnt = 0
    ref = []
    for i in range(6):
        if sum(board[i]) >= 4:
            cnt+=1
        else:
            ref.append(i)
    new_board = [[0]*4 for _ in range(cnt)]
    for i in ref:
        new_board.append(board[i])
    return cnt, new_board

def block_clear2(board):
    cnt = 0
    for i in range(2):
        if sum(board[i]) >= 1:
            cnt += 1
    new_board = [[0]*4 for _ in range(cnt)]
    new_board += board[:-cnt]
    return cnt, new_board

ans = 0
for t,x,y in orders:
    gt,gx,gy, bt,bx,by = green_blue(t,x,y)
    block_shoot(green,gt,gx,gy)
    block_shoot(blue,bt,bx,by)
    gnt,green = block_clear1(green)
    bnt,blue = block_clear1(blue)
    ans+=(gnt+bnt)
    gnt,green = block_clear2(green)
    bnt,blue = block_clear2(blue)
    ans+=(gnt+bnt)

rslt = 0
for i in green:
    rslt += sum(green[i])
for i in blue:
    rslt += sum(blue[i])

print(ans)
print(rslt)