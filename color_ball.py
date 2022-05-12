# 10800
n = int(input())
balls = []
for i in range(n):
    c,s, = map(int,input().split())
    balls.append([i+1,c,s])

balls.sort(key=lambda x:(x[2],x[1]))
color_sum = [0]*(n+1)
size_sum = {}
ans = {}
pre_num, pre_colour, pre_size = 0,0,0
current_total = 0
for ball in balls:
    num, colour, size_ = ball
    if pre_colour == colour and pre_size == size_:
        ans[num] = ans[pre_num]
        pre_num, pre_colour, pre_size = num, colour, size_
        continue

    current_total += size_
    try:
        size_sum[size_] += size_
    except KeyError:
        size_sum[size_] = size_
    color_sum[num] += size_

    ans[num] = current_total - size_sum[size_] - color_sum[num] + size_
    pre_num, pre_colour, pre_size = num, colour, size_

print(ans)