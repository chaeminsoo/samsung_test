# 17136
board = []
for i in range(10):
    board.append(list(map(int,input().split())))

def box(x,y,num,board):
    if num == 0:
        return True, [[x,y]]
    elif num == 1:
        ref = []
        for i in range(x,x+2):
            for j in range(y,y+2):
                if board[i][j] == 0 or i > 10 or j > 10:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref
    elif num == 2:
        ref = []
        for i in range(x,x+3):
            for j in range(y,y+3):
                if board[i][j] == 0 or i > 10 or j > 10:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref
    elif num == 3:
        ref = []
        for i in range(x,x+4):
            for j in range(y,y+4):
                if board[i][j] == 0 or i > 10 or j > 10:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref
    elif num == 4:
        ref = []
        for i in range(x,x+5):
            for j in range(y,y+5):
                if board[i][j] == 0 or i > 10 or j > 10:
                    return False, False
                else:
                    ref.append([i,j])
        return True, ref

def a_check(b):
    for i in range(10):
        for j in range(10):
            if b[i][j] == 1:
                return False
    return True
def b_check(b):
    for i in b:
        if i > 5:
            return True
    return False

ans = 1e9
def dfs(x,y,board,b,cnt):
    global ans
    if a_check(board):
        ans = min(ans,cnt)
        return
    if b_check(b):
        return
    
    for i in range(x,10):
        for j in range(y,10):
            if board[i][j] == 1:
                
                for k in range(5):
                    tf, targets = box(i,j,k,board)
                    if tf:
                        b[k]+=1
                        for tr,tc in targets:
                            board[tr][tc] = 0
                        dfs(i,j,[c[:] for c in board],b,cnt+1)
                        for tr,tc in targets:
                            board[tr][tc] = 1
                        b[k] -=1


dfs(0,0,board,[0,0,0,0,0],0)
if ans == 1e9:
    print(-1)
else:
    print(ans)