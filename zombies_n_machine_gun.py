# 19644
l = int(input())
ml,mk = map(int,input().split())
c = int(input())
zombies = [0]
for _ in range(l):
    z = int(input())
    zombies.append(z)

cursor_ = 0

def c_bomb(cursor_,c):
    for i in range(cursor_+1,cursor_+l):
        try:
            zombies[i] += mk
        except IndexError:
            pass
    return c-1
live = True
while cursor_ <= l:
    if cursor_ >= ml:
        damage = ml*mk
    else:
        damage = mk*cursor_
        
    if damage < zombies[cursor_]:
        if c > 0:
            c = c_bomb(cursor_,c)
            cursor_+=1
        else:
            live = False
            break
    else:
        cursor_+=1
if live:
    print('Yes')
else:
    print('NO')