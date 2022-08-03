# 23289
from collections import deque

r,c,k = map(int,input().split())
board = []
heater = []
sensor = []

#rlud
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(r):
    data = list(map(int,input().split()))
    for j in range(c):
        if data[j] != 0 and data[j] != 5:
            heater.append([i,j,data[j]-1])
            data[j] = -1
        elif data[j] != 0 and data[j] == 5:
            sensor.append([i,j])
w = int(input())
walls = [[0]*c for _ in range(r)]
for _ in range(w):
    x,y,t = map(int,input().split())
    walls[x][y] = t

def heat_wind_d(i,j,d):
    if d == 0:
        return [[i+dx[d]-1,j+dy[d]],[i+dx[d],j+dy[d]],[i+dx[d]+1,j+dy[d]]]
    if d == 1:
        return [[i+dx[d]-1,j+dy[d]],[i+dx[d],j+dy[d]],[i+dx[d]+1,j+dy[d]]]
    if d == 2:
        return [[i+dx[d],j+dy[d]-1],[i+dx[d],j+dy[d]],[i+dx[d],j+dy[d]+1]]
    if d == 0:
        return [[i+dx[d],j+dy[d]-1],[i+dx[d],j+dy[d]],[i+dx[d],j+dy[d]+1]]

def heater_wind():
    for i,j,d in heater:
        ref_board = [[0]*c for _ in range(r)]

        ref_board[i+dx[d]][j+dy[d]] = 5
        cnt = 4
        q = deque()
        q.append([i+dx[d],j+dy[d]])
        while cnt > 0:
            x,y = q.popleft()
            for x1, y1 in heat_wind_d(x,y,d):
                if 0 <= x1 < r and 0 <= y1 < c and board[x1][y1] != -1
                ref_board[x1][y1] += cnt
            cnt -= 1
            x = 




        
    return

def temp():
    return

def checking():
    return

cnt = 0
while cnt < 101:
    heater_wind()
    temp()
    cnt += 1
    if checking:
        break
print(cnt)