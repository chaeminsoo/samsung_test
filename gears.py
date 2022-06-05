# 14891
fst_gear = input()
snd_gear = input() 
trd_gear = input()
fth_gear = input()
gears = [fst_gear, snd_gear, trd_gear, fth_gear]
k = int(input())
orders = []
for _ in range(k):
    a,b = map(int,input().split())
    orders.append((a,b))

def find_gears():
    global gears
    connections = [0,0,0]
    if gears[0][2] != gears[1][6]:
        connections[0] = 1
    if gears[1][2] != gears[2][6]:
        connections[1] = 1
    if gears[2][2] != gears[3][6]:
        connections[2] = 1
    return connections

connections = find_gears()

def clock_wise(n):
    global gears
    ref = gears[n-1][-1]
    gears[n-1] = ref + gears[n-1][:-1]

def c_clock_wise(n):
    global gears
    ref = gears[n-1][0]
    gears[n-1] = gears[n-1][1:] + ref

for n,d in orders:
    connections = find_gears()
    new_orcders = [(n,d)]
    if n ==1:
        if connections[0] ==1:
            new_orcders.append((2,-d))
            if connections[1] ==1:
                new_orcders.append((3,d))
                if connections[2] ==1:
                    new_orcders.append((4,-d))
    elif n ==2:
        if connections[0] ==1:
            new_orcders.append((1,-d))
        if connections[1] ==1:
            new_orcders.append((3,-d))
            if connections[2] ==1:
                new_orcders.append((4,d))
    elif n ==3:
        if connections[1] ==1:
            new_orcders.append((2,-d))
            if connections[0] ==1:
                new_orcders.append((1,d))
        if connections[2] ==1:
            new_orcders.append((4,-d))
    elif n ==4:
        if connections[2] ==1:
            new_orcders.append((3,-d))
            if connections[1] ==1:
                new_orcders.append((2,d))
                if connections[0] ==1:
                    new_orcders.append((1,-d))

    for nn,nd in new_orcders:
        if nd ==1:
            clock_wise(nn)
        else:
            c_clock_wise(nn)
ans = 0
for i,gear in enumerate(gears):
    if i == 0 and gear[0] =='1':
        ans+=1
    if i == 1 and gear[0] =='1':
        ans+=2
    if i == 2 and gear[0] =='1':
        ans+=4
    if i == 3 and gear[0] =='1':
        ans+=8
print(ans)