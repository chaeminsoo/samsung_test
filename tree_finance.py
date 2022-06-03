# 16235
import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
nourishment_field = [[5]*n for _ in range(n)]
put_nour = []
for _ in range(n):
    put_nour.append(list(map(int,input().split())))

alive_tree = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    alive_tree[x-1][y-1].append(z)
    
def ss():
    global nourishment_field, alive_tree
    for i in range(n):
        for j in range(n):
            if alive_tree[i][j]:

                tree_num = len(alive_tree[i][j])
                for idx in range(tree_num):
                    if alive_tree[i][j][idx] <= nourishment_field[i][j]:
                        nourishment_field[i][j] -= alive_tree[i][j][idx]
                        alive_tree[i][j][idx] += 1
                    else:
                        for _ in range(idx,tree_num):
                            nourishment_field[i][j] += alive_tree[i][j].pop()//2
                        break
                        
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def fw():
    global nourishment_field, alive_tree
    for i in range(n):
        for j in range(n):
    
            if alive_tree[i][j]:
                for tree in alive_tree[i][j]:
                    if tree%5 == 0:
                        for clockw in range(8):
                            nx = i + dx[clockw]
                            ny = j + dy[clockw]
                            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                                alive_tree[nx][ny].appendleft(1)

            nourishment_field[i][j] += put_nour[i][j]
            
for _ in range(k):
    ss()
    fw()
    
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(alive_tree[i][j])
print(cnt)