# 15683
n,m = map(int, input().split())
room = []
cctvs = []
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        if a[j] != 0 and a[j] != 6:
            cctvs.append((a[j],i,j))

cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3], [3,0]],
    [[0,1,3], [0,1,2], [1,2,3], [0,2,3]],
    [[0,1,2,3]]
]
# clockwise
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def watch(room, mm, x, y):
    