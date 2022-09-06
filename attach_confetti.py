# 17136
board = []
ont = 0
for i in range(10):
    data = list(map(int,input().split()))
    for j in data:
        if j == 1: ont+=1
    board.append(data)

def box(x,y,num,board):
    if num == 0:
        return True, [[x,y]]
    elif num == 1:
        ref = []
        for i in range(x,x+2):
            for j in range(y,y+2):
                if i >= 10 or j >= 10 or board[i][j] == 0:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref
    elif num == 2:
        ref = []
        for i in range(x,x+3):
            for j in range(y,y+3):
                if i >= 10 or j >= 10 or board[i][j] == 0:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref
    elif num == 3:
        ref = []
        for i in range(x,x+4):
            for j in range(y,y+4):
                if i >= 10 or j >= 10 or board[i][j] == 0:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref
    elif num == 4:
        ref = []
        for i in range(x,x+5):
            for j in range(y,y+5):
                if i >= 10 or j >= 10 or board[i][j] == 0:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref

def b_check(b):
    for i in b:
        if i > 5:
            return True
    return False
#=======================================================
ans = 1e9
def dfs(x,y,board,b,cnt,ont):
    global ans
    # print('xy:',x,y)
    if ont <= 0:
        ans = min(ans,cnt)
        return
    if b_check(b):
        return
    if x > 9 or y > 9:
        return
    
    if board[x][y] == 1:
        
        for k in range(5):
            tf, targets = box(x,y,k,board)
            if tf:
                b[k]+=1
                ont -= (k+1)**2
                for tr,tc in targets:
                    board[tr][tc] = 0
                if y+1 < 10:
                    dfs(x,y+1,[c[:] for c in board],b,cnt+1,ont)
                elif y+1 >= 10:
                    dfs(x+1,0,[c[:] for c in board],b,cnt+1,ont)

                for tr,tc in targets:
                    board[tr][tc] = 1
                ont += (k+1)**2
                b[k] -=1
    else:
        if y+1 < 10:
            dfs(x,y+1,[c[:] for c in board],b,cnt,ont)
        elif y+1 >= 10:
            dfs(x+1,0,[c[:] for c in board],b,cnt,ont)

# origin =======================================================
# ans = 1e9
# def dfs(x,board,b,cnt,ont):
#     global ans
#     if ont <= 0:
#         ans = min(ans,cnt)
#         return
#     if b_check(b):
#         return
    
#     for i in range(x,10):
#         for j in range(10):
#             if board[i][j] == 1:
                
#                 for k in range(5):
#                     tf, targets = box(i,j,k,board)
#                     if tf:
#                         b[k]+=1
#                         ont -= (k+1)**2
#                         for tr,tc in targets:
#                             board[tr][tc] = 0
#                         dfs(i,[c[:] for c in board],b,cnt+1,ont)
#                         for tr,tc in targets:
#                             board[tr][tc] = 1
#                         ont += (k+1)**2
#                         b[k] -=1
#=============================================================
if ont == 100:
    ans = 4
else:
    dfs(0,0,board,[0,0,0,0,0],0,ont)
# dfs(0,board,[0,0,0,0,0],0,ont)
if ans == 1e9:
    print(-1)
else:
    print(ans)