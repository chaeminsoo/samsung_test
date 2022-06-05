# 14889
n = int(input())
skills = []
for i in range(n):
    skills.append(list(map(int,input().split())))

ans = 1e9
visit = [False]*n
def dfs(idx,depth):
    global ans
    if depth == n//2:
        start_team = 0
        link_team = 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start_team += skills[i][j]
                elif not visit[i] and not visit[j]:
                    link_team += skills[i][j]
        ans = min(ans,abs(start_team - link_team))

    for i in range(idx,n):
        if not visit[i]:
            visit[i] = True
            dfs(i+1,depth+1)
            visit[i] = False

dfs(0,0)
print(ans)