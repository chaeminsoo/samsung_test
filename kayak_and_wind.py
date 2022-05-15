# 2891
n,s,r = map(int,input().split())
kayaks = [1]*(n+2)
broken_kayaks = list(map(int,input().split()))
more_kayaks = list(map(int,input().split()))

for i in broken_kayaks:
    kayaks[i] -= 1
for i in more_kayaks:
    kayaks[i] += 1

cnt = 0
for num in range(1,n+1):
    if kayaks[num] == 0:
        if kayaks[num-1] == 2:
            kayaks[num-1] -= 1
            kayaks[num] += 1
        elif kayaks[num+1] == 2:
            kayaks[num+1] -= 1
            kayaks[num] += 1
        else:
            cnt+=1
print(cnt)