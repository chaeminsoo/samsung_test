# 16235
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
nourishment_field = [[5]*n for _ in range(n)]
put_nour = []
for _ in range(n):
    put_nour.append(list(map(int,input().split())))

alive_tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    alive_tree[x-1][y-1].append(z)
    
dead_tree = [[[] for _ in range(n)] for _ in range(n)]

def spring():
    global nourishment_field, alive_tree, dead_tree
    for i in range(n):
        for j in range(n):
            if alive_tree[i][j]:
                new_trees = []
                alive_tree[i][j].sort()

                for tree in alive_tree[i][j]:
                    if tree <= nourishment_field[i][j]:
                        nourishment_field[i][j] -= tree
                        new_trees.append(tree+1)
                    else:
                        dead_tree[i][j].append(tree)

                alive_tree[i][j] = new_trees

def summer():
    global nourishment_field, alive_tree, dead_tree
    for i in range(n):
        for j in range(n):
            if dead_tree[i][j]:
                for tree in dead_tree[i][j]:
                    nourishment_field[i][j] += tree//2

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def fall():
    global nourishment_field, alive_tree, dead_tree
    for i in range(n):
        for j in range(n):

            if alive_tree[i][j]:
                for tree in alive_tree[i][j]:
                    if tree%5 == 0:
                        for clockw in range(8):
                            nx = i + dx[clockw]
                            ny = j + dy[clockw]
                            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                                alive_tree[nx][ny].append(1)

def winter():
    global nourishment_field, alive_tree, dead_tree, put_nour
    for i in range(n):
        for j in range(n):
            nourishment_field[i][j] += put_nour[i][j]

for _ in range(k):
    spring()
    summer()
    fall()
    winter()

cnt = 0
for i in range(n):
    for j in range(n):
        if alive_tree[i][j]:
            cnt += len(alive_tree[i][j])
print(cnt)