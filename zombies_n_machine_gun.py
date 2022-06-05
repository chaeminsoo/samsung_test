# 19644
import sys
input = sys.stdin.readline

l = int(input())
ml,mk = map(int,input().split())
claymores = int(input())
zombies = [0]
for _ in range(l):
    z = int(input())
    zombies.append(z)
live = True
claymores_hill = 0
for idx, zombie in enumerate(zombies):
    claymores_hill -= 1
    if idx <= ml:
        damage = idx*mk
    else:
        damage = ml*mk
    
    if claymores_hill > 0:
        damage -= mk

    if zombie <= damage:
        continue
    else:
        if claymores > 0:
            claymores -= 1
            claymores_hill = ml
        else:
            live = False
            break
if live:
    print('YES')
else:
    print('NO')