# 17281
import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
innings = []
for i in range(n):
    innings.append(list(map(int,input().split())))

# rosters = list(permutations([i for i in range(9)], 9))
rosters = list(permutations([i for i in range(1,9)], 8))
ans = 0
for roster in rosters:
    # if roster[3] != 0:
    #     continue
    roster = list(roster)
    roster.insert(3,0)
    cnt = 0
    pnt = 0
    ont = 0
    snt = 0
    b1, b2, b3 = 0,0,0
    while cnt < n:
        now = innings[cnt][roster[pnt]]
        if now == 0:
            ont += 1
            if ont >= 3:
                cnt+=1
                ont = 0
                b1,b2,b3 = 0, 0, 0
        elif now == 1:
            snt += b3
            b1, b2, b3 = 1, b1, b2
        elif now == 2:
            snt += (b3+b2)
            b1, b2, b3 = 0, 1, b1
        elif now == 3:
            snt += (b3+b2+b1)
            b1, b2, b3 = 0, 0, 1
        elif now == 4:
            snt += (b3+b2+b1+1)
            b1, b2, b3 = 0, 0, 0
        pnt+=1
        pnt %= 9
    ans = max(ans,snt)
print(ans)