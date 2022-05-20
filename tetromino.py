# 14500
n,m = map(int,input().split())
board = [[0]*(m+6) for _ in range(n+6)]
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        board[i+3][j+3] = row[j] 

def stick(x,y,d):
    if d == 0: # lay
        return board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3]
    elif d == 1:
        return board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y]

def box(x,y):
    return board[x][y] + board[x+1][y] + board[x][y+1] + board[x+1][y+1]

def el(x,y,d):
    if d == 0: # clockwise
        return board[x][y] + board[x+1][y] + board[x+2][y] + board[x+2][y+1]
    elif d == 1:
        return board[x][y] + board[x+1][y] + board[x][y+1] + board[x][y+2]
    elif d == 2:
        return board[x][y] + board[x][y+1] + board[x+1][y+1] + board[x+2][y+1]
    elif d == 3:
        return board[x][y] + board[x+1][y] + board[x+1][y-1] + board[x+1][y-2]
    
    if d == 4: # clockwise
        return board[x][y] + board[x+1][y] + board[x+2][y] + board[x+2][y-1]
    elif d == 5:
        return board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+1][y+2]
    elif d == 6:
        return board[x][y] + board[x][y+1] + board[x+1][y] + board[x+2][y]
    elif d == 7:
        return board[x][y] + board[x][y+1] + board[x][y+2] + board[x+1][y+2]


def thunder(x,y,d):
    if d == 0: # clockwise
        return board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+2][y+1]
    elif d == 1:
        return board[x][y] + board[x+1][y] + board[x][y+1] + board[x+1][y-1]

    elif d == 2:
        return board[x][y] + board[x+1][y] + board[x+1][y-1] + board[x+2][y-1]
    elif d == 3:
        return board[x][y] + board[x][y+1] + board[x+1][y+1] + board[x+1][y+2]

def oh(x,y,d):
    if d == 0: # clockwise
        return board[x][y] + board[x][y+1] + board[x+1][y+1] + board[x][y+2]
    if d == 1: # clockwise
        return board[x][y] + board[x+1][y] + board[x+2][y] + board[x+1][y-1]
    if d == 2: # clockwise
        return board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+1][y-1]
    if d == 3: # clockwise
        return board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+2][y]

ans = 0
for i in range(n):
    for j in range(m):
        r,c = i+3,j+3

        for t in range(2):
            ans = max(ans,stick(r,c,t))
        ans = max(ans,box(r,c))
        for t in range(8):
            ans = max(ans,el(r,c,t))
        for t in range(4):
            ans = max(ans,thunder(r,c,t))
        for t in range(4):
            ans = max(ans,oh(r,c,t))
print(ans)