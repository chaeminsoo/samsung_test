# 20057
import math

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

visited = [[False]*n for _ in range(n)]

tor = [math.ceil(n/2),math.ceil(n/2),3]
visited[tor[0]][tor[1]] = True

#ldru
dr = [0,1,0,-1]
dc = [-1,0,1,0]

def tor_move(r,c,d):
    nd = d%4
    nr = r + dr[nd]
    nc = c + dc[nd]

    if visited[nr][nc] == True:
        nr = r + dr[d]
        nc = c + dc[d]
        visited[nr][nc] = True
        return [nr,nc,d]
    else:
        visited[nr][nc] = True
        return [nr,nc,nd]
ans = 0

wdx = [-2,-1,-1,-1,0,0,1,1,1,2]
wdy = [0,-1,0,1,-2,-1,-1,0,1,0]

def wind(r,c,d):
    global ans
    ref = board[r][c]
    o = int(ref*0.01)
    two = int(ref*0.02)
    five = int(ref*0.05)
    seven = int(ref*0.07)
    ten = int(ref*0.1)
    a = ref - (2*two + 2*seven + 2*ten + five + 2*o)
    wdpersent = [two,ten,seven,o,five,a,ten,seven,o,two]

    for i in range(10):
        wnx = r + wdx[i]
        wny = c + wdy[i]
        