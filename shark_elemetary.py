# 21508
n = int(input())
board = [[0]*n for _ in range(n)]
students = []
for _ in range(n**2):
    students.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for data in students:
    prefer_board = []
    num = data[0]
    prefer = data[1:]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                pnt = 0
                bnt = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in prefer:
                            pnt += 1
                        elif board[nx][ny] == 0:
                            bnt += 1
                prefer_board.append((pnt,bnt,i,j))
    
    prefer_board.sort(key=lambda x:(x[0],x[1],-x[2],-x[3]))
    new_s = prefer_board.pop()
    board[new_s[2]][new_s[3]] = num

students.sort()

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in students[board[i][j]-1][1:]:
                    cnt +=1

        if cnt ==1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)