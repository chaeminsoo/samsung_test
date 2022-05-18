# 10800
n = int(input())
balls = []
for i in range(n):
    c,s, = map(int,input().split())
    balls.append([i+1,c,s])
    
now_total = 0
color_sum = [0]*n
size_sum = {}
ans = []

balls.sort(key=lambda x:(x[2],x[1]))

for num, color_, size_ in balls:
    ref = 0
    ref += now_total
    ref -= color_sum[color_-1]
    try:
        ref -= size_sum[size_]
    except KeyError:
        pass
    ans.append([num,ref])
    now_total += size_
    color_sum[color_-1] += size_
    try:
        size_sum[size_] += size_
    except KeyError:
        size_sum[size_] = size_
ans.sort()
for a in ans:
    print(a[1])