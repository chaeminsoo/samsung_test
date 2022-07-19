# 20061
n = int(input())
orders = []
for _ in range(n):
    t,a,b = map(int,input().split())
    orders.append([t,a,b])

green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]

def green_blue(t,x,y):
    if t == 1:
        return t,x,y,t,y,(3-x)
    elif t == 2:
        return t,x,y,t+1,y,(3-(x+1))
    elif t == 3:
        return t,x,y,t-1,y,(3-x)

def block_shoot(board,t,x,y):
    if t == 1:
        cursor_ = 0
        while cursor_ <= 5:
            if cursor_ == 5:
                board[cursor_][y] = 1
                break
            if board[cursor_+1][y] == 0:
                cursor_+=1
                continue
            else:
                board[cursor_][y] = 1
                break
    elif t == 2:
        cursor_ = 0
        while cursor_ <= 5:
            if cursor_ == 5:
                board[cursor_][y] = 1
                board[cursor_][y+1] = 1
                break
            if board[cursor_+1][y] == 0 and board[cursor_+1][y+1] == 0:
                cursor_+=1
                continue
            else:
                board[cursor_][y] = 1
                board[cursor_][y+1] = 1
                break
    elif t == 3:
        cursor_ = 0
        while cursor_ <= 5:
            if cursor_ == 4:
                board[cursor_][y] = 1
                board[cursor_+1][y] = 1
                break
            if board[cursor_+2][y] == 0:
                cursor_+=1
                continue
            else:
                board[cursor_][y] = 1
                board[cursor_+1][y] = 1
                break
    return board

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
    if cnt:
        new_board = [[0]*4 for _ in range(cnt)]
        new_board += board[:-cnt]
        return cnt, new_board
    else:
        return cnt, board

ans = 0
for t,x,y in orders:
    gt,gx,gy, bt,bx,by = green_blue(t,x,y)
    green = block_shoot(green,gt,gx,gy)
    blue = block_shoot(blue,bt,bx,by)
    gnt,green = block_clear1(green)
    bnt,blue = block_clear1(blue)
    ans+=(gnt+bnt)
    gnt,green = block_clear2(green)
    bnt,blue = block_clear2(blue)
    ans+=(gnt+bnt)

rslt = 0
for i in green:
    rslt += sum(i)
for i in blue:
    rslt += sum(i)

print(ans)
print(rslt)