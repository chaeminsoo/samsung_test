# 17779
n = int(input())
board = [[0]*(n+1)]
total = 0
for _ in range(n):
    data = list(map(int,input().split()))
    total+=sum(data)
    board.append([0]+data)

ans = 1e9
for d1 in range(1,n+1):
    for d2 in range(1,n+1):
        for x in range(1,n+1):
            for y in range(1,n+1):
                if x+d1+d2 <= n and 1 <= y-d1 and y+d2 <= n:
                    visited = [[False]*(n+1) for _ in range(n+1)]
                    ppls = [0,0,0,0,0]

                    for j in range(d2+1):
                        for i in range(d1+1):
                            visited[x+j+i][y+j-i] = True
                    for j in range(d2):
                        for i in range(d1):
                            visited[x+1+j+i][y+j-i] = True
                    
                    for r in range(1,n+1):
                        for c in range(1,n+1):
                            if 1<= r < x+d1 and 1<= c <= y and not visited[r][c]:
                                ppls[0]+=board[r][c]
                            if 1 <= r <= x+d2 and y < c <= n and not visited[r][c]:
                                ppls[1]+=board[r][c]
                            if x+d1 <= r <= n and 1 <= c < y-d1+d2 and not visited[r][c]:
                                ppls[2]+=board[r][c]
                            if x+d2 < r <= n and y-d1+d2 <= c <= n and not visited[r][c]:
                                ppls[3]+=board[r][c]
                    
                    ppls[4] = total - sum(ppls)
                    ans  = min(ans, max(ppls) - min(ppls))
print(ans)