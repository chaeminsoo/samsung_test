# 15684
n,m,h = map(int,input().split())
visited = [[False]*(n+1) for _ in range(h+1)]
garo = [] # 가로 후보군

for _ in range(m):
    a, b = map(int,input().split())
    visited[a][b] = True

def check():
    for i in range(1,n+1):
        now = i
        for j in range(1,h+1):
            if visited[j][now-1]: # 왼쪽에 사다리 -> 왼쪽으로 이동
                now-=1
            elif visited[j][now]: # 현위치 사다리 -> 오른쪽으로 이동
                now+=1
        if now != i:
            return False
    return True

ans = 4
def dfs(depth, idx):
    global ans
    if depth >= ans:
        return
    if check():
        ans = depth
        return

    for c in range(idx, len(garo)):
        x, y = garo[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)
            visited[x][y] = False

for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            garo.append((i,j))

dfs(0,0)
print(ans if ans < 4 else -1)