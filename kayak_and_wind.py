# 2891
n,s,r = map(int,input().split())
kayaks = [1]*n
broken_kayaks = list(map(int,input().split()))
more_kayaks = list(map(int,input().split()))

for i in broken_kayaks:
    kayaks[i-1] -= 1
for i in more_kayaks:
    kayaks[i-1] += 1

borrow_kayaks = [0]*n
cnt = 0
for num,kayak in enumerate(kayaks):
    if borrow_kayaks[num] + kayak >= 1:
        if borrow_kayaks[num] + kayak == 2:
            try:
                borrow_kayaks[num+1] = 1
            except IndexError:
                pass
    else:
        try:
            if kayaks[num+1] == 2:
                borrow_kayaks[num+1] = -1
            else:
                cnt += 1
        except IndexError:
            cnt+=1
print(cnt)