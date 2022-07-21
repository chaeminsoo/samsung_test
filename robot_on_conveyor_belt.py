# 20055
from collections import deque

n,k = map(int,input().split())
data = list(map(int,input().split()))
belt = deque()
for i in range(2*n):
    belt.append([data[i],0])

# def belt_move():
#     global belt
#     belt = [belt[-1]] + belt[:-1]
#     belt[n-1][1] = 0
    
def robot_move():
    global belt
    for i in range(n-1,-1,-1):
        if belt[i][1] != 0 and belt[i+1][1] == 0 and belt[i+1][0] != 0:
            belt[i+1][0] -= 1
            belt[i+1][1] = belt[i][1]
            belt[i][1] = 0
    belt[n-1][1] = 0

def checking():
    global k, belt
    cnt = 0
    for i in range(2*n):
        if belt[i][0] == 0:
            cnt+=1
    if cnt >= k:
        return True
    else:
        return False

ans = 1
while True:
    # belt_move()
    belt.rotate(1)
    belt[n-1][1] = 0
    robot_move()
    if belt[0][0] != 0 and belt[0][1] == 0:
        belt[0][1] = 1
        belt[0][0] -= 1
    if checking():
        break
    else:
        ans += 1
print(ans)