#14499
import sys
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
board = []
for _ in range(n):
    a = list(map(int,input().split()))
    board.append(a)
orders = list(map(int,input().split()))

dice = [0,0,0,0,0,0]
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def dice_roll(dice,dir):
    u,d,h,t,l,r = dice
    if dir == 1:
        return [l,r,h,t,d,u]
    elif dir == 2:
        return [r,l,h,t,u,d]
    elif dir == 3:
        return [h,t,d,u,l,r]
    elif dir == 4:
        return [t,h,u,d,l,r]

def reflect(dice,board,x,y):
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0
    return dice[0],dice,board

ans = []
for order in orders:
    nx = x + dr[order-1]
    ny = y + dc[order-1]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
        dice = dice_roll(dice,order)
        aw, dice, board = reflect(dice,board,nx,ny)
        ans.append(aw)
        x,y = nx,ny
for i in ans:
    print(i)