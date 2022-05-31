# 16235
n,m,k = map(int,input().split())
nourishment_field = []
for _ in range(n):
    nourishment_field.append(list(map(int,input().split())))
alive_tree = [[[]]*n for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    alive_tree[x-1][y-1].append(z)

for i in alive_tree:
    print(i)