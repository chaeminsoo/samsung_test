# 17070
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
# pipe_ = [[0,0],[0,1]]
dirt = [
    [[[0,1], [0,1]], [[0,1], [1,1]]],
    [[[1,0], [1,0]], [[1,0], [1,1]]],
    [[[1,1], [0,1]], [[1,1], [1,0]], [[1,1], [1,1]]]
]

def pd(pp):
    p1,p2 = pp
    pr1,pc1 = p1
    pr2,pc2 = p2
    if pc1 == pc2:
        return 0
    elif pr1 == pr2:
        return 1
    else:
        return 2

def done_(pp):
    d = pd(pp)
    p1,p2 = pp
    pr2,pc2 = p2
    if d == 0:
        if pc2 == n-1:
            return True
        else:
            if board[pr2][pc2+1] == 1:
                return True
            else:
                return False
    if d == 1:
        if pr2 == n-1:
            return True
        else:
            if board[pr2+1][pc2] == 1:
                return True
            else:
                return False
    if d == 2:
        if pc2 == n-1 and pr2 == n-1:
            return True
        else:
            if board[pr2][pc2+1] == 1 and board[pr2+1][pc2] == 1:
                return True
            else:
                return False

ans = 0
def dfs(pp):
    global ans
    if done_(pp) or pp[1] == [n-1,n-1]:
        if pp[1] == [n-1,n-1]:
            ans+=1
            # print('=',pp) 
        return
    pp1, pp2 = pp
    d = pd(pp)
    dp = dirt[d]
    if d == 0:
        for dp0, ddp in enumerate(dp):
            dp1, dp2 = ddp
            np1 = [pp1[0]+dp1[0],pp1[1]+dp1[1]]
            np2 = [pp2[0]+dp2[0],pp2[1]+dp2[1]]
            if dp0 == 0:
                if np2[0] < n and np2[1] < n and board[pp2[0]][pp2[1]+1] != 1:
                    dfs([np1,np2])
            else:
                if np2[0] < n and np2[1] < n and board[pp2[0]][pp2[1]+1] != 1 and board[pp2[0]+1][pp2[1]+1] != 1 and board[pp2[0]+1][pp2[1]] != 1:
                    dfs([np1,np2])
    if d == 1:
        for dp0, ddp in enumerate(dp):
            dp1, dp2 = ddp
            np1 = [pp1[0]+dp1[0],pp1[1]+dp1[1]]
            np2 = [pp2[0]+dp2[0],pp2[1]+dp2[1]]
            if dp0 == 0:
                if np2[0] < n and np2[1] < n and board[pp2[0]+1][pp2[1]] != 1:
                    dfs([np1,np2])
            else:
                if np2[0] < n and np2[1] < n and board[pp2[0]+1][pp2[1]] != 1 and board[pp2[0]+1][pp2[1]+1] != 1 and board[pp2[0]][pp2[1]] != 1:
                    dfs([np1,np2])
    if d == 2:
        for dp0, ddp in enumerate(dp):
            dp1, dp2 = ddp
            np1 = [pp1[0]+dp1[0],pp1[1]+dp1[1]]
            np2 = [pp2[0]+dp2[0],pp2[1]+dp2[1]]
            if dp0 == 0:
                if np2[0] < n and np2[1] < n and board[pp2[0]][pp2[1]+1] != 0:
                    dfs([np1,np2])
            elif dp0 == 1:
                if np2[0] < n and np2[1] < n and board[pp2[0]+1][pp2[1]] != 0:
                    dfs([np1,np2])
            elif dp0 == 2:
                if np2[0] < n and np2[1] < n and board[pp2[0]+1][pp2[1]] != 0 and board[pp2[0]+1][pp2[1]+1] != 0 and board[pp2[0]][pp2[1]+1] != 0:
                    dfs([np1,np2])
dfs([[0,0], [0,1]])
print(ans)