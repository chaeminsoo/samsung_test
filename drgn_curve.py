# 15685
n = int(input())
drgns = []
for _ in range(n):
    x,y,d,g = map(int,input().split())
    drgns.append((x,y,d,g))

def drgn_crv(drgn):
    axis_a, axis_b = drgn[-1][0], drgn[-1][1]
    nor_drgn = []
    for i in range(len(drgn)-2,-1,-1):
        nor_drgn.append((drgn[i][0] - axis_a, drgn[i][1] - axis_b))
    for j in nor_drgn:
        a,b = j[0],j[1]
        drgn.append((axis_a-b,axis_b+a))
    return drgn

def st(a,b,c):
    if c == 0:
        return (a+1,b)
    elif c == 1:
        return (a,b-1)
    elif c == 2:
        return (a-1,b)
    elif c == 3:
        return (a,b+1)

all_drgn = []
for i in drgns:
    x,y,d,g = i
    ref = [(x,y),st(x,y,d)]
    for _ in range(g):
        ref = drgn_crv(ref)
    all_drgn += ref
all_drgn.sort(key=lambda x: x[1])

cnt = 0

def box_check(st_p, al):
    if (st_p[0]+1,st_p[1]) in al and (st_p[0],st_p[1]+1) in al and (st_p[0]+1,st_p[1]+1) in al:
        return True
    else:
        return False

for st_p in list(set(all_drgn)):
    if box_check(st_p,all_drgn):
        cnt+=1
print(cnt)