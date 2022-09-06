# 17281
from itertools import permutations

n = int(input())
innings = []
for i in range(n):
    innings.append(list(map(int,input().split())))

rosters = list(permutations([i for i in range(9)], 9))
ans = 0
for roster in rosters:
    if roster[3] != 0:
        continue
    cnt = 0
    pnt = 0
    ont = 0
    bases = [0,0,0,0,0]
    while cnt < n:
        bases[0] = 1
        now = innings[cnt][roster[pnt]]
        if now == 0:
            ont += 1
            if ont >= 3:
                cnt+=1
                ont = 0
                bases = [0,0,0,0] + [bases[4]]
                # for j in range(4):
                #     bases[j] = 0
        elif now == 1:
            for j in range(3,-1,-1):
                if bases[j] == 1:
                    bases[j+1] +=1
                    bases[j] = 0
        elif now == 2:
            for j in range(3,-1,-1):
                if bases[j] == 1:
                    k = j+2 if j+2 <= 4 else 4 
                    bases[k] +=1
                    bases[j] = 0
        elif now == 3:
            for j in range(3,-1,-1):
                if bases[j] == 1:
                    k = j+3 if j+3 <= 4 else 4 
                    bases[k] +=1
                    bases[j] = 0
        elif now == 4:
            for j in range(3,-1,-1):
                if bases[j] == 1:
                    k = j+4 if j+4 <= 4 else 4 
                    bases[k] +=1
                    bases[j] = 0
        pnt+=1
        pnt %= 9
    ans = max(ans,bases[4])
print(ans)

# 3 8 8
# 8 8 8