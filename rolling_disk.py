# 17822
import dis


n,m,t = map(int,input().split())
disk = [0]
orders = []
for _ in range(n):
    disk.append(list(map(int,input().split())))
for _ in range(t):
    a,b,c = map(int,input().split())
    orders.append((a,b,c))

# 12345
# 51234 clock
# 45123
# 23451 counter clock
# 34512
def turn_disk(x,d,k):
    if d == 0:
        for i in range(1,n+1):
            if i % x == 0:
                disk[i] = disk[i][-k:] + disk[i][:-k]
    elif d == 1:
        for i in range(1,n+1):
            if i % x == 0:
                disk[i] = disk[i][k:] + disk[i][:k]

def clear_disk():
    for i in range(1,n):
        for j in range(m):
            
    return

for order in orders:
    x,d,k = order
    turn_disk()
    clear_disk()

ans = 0
for i in disk:
    ans += sum(i)
print(ans)