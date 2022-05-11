# 12100
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def moving(board,dir,n):
    if dir == 0: # up
        check_=[]
        for r in range(n):
            for c in range(n):
                if board[r][c] == 0:
                    continue
                while True:
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if nr >= 0  and nr < n and nc >= 0 and nc < n:
                        if board[nr][nc] == 0:
                            board[nr][nc] = board[r][c]
                            board[r][c] = 0
                            r,c = nr,nc
                            continue
                        elif board[nr][nc] == board[r][c]:
                            if (nr,nc) not in check_:
                                board[nr][nc] *=2
                                board[r][c] = 0
                                r,c = nr,nc
                                check_.append((r,c))
                                continue
                            else:
                                break
                        elif board[nr][nc] != board[r][c]:
                            break
        return board

    elif dir == 1: # down
        check_=[]
        for r in range(n-1,-1,-1):
            for c in range(n):
                if board[r][c] == 0:
                    continue
                while True:
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if nr >= 0  and nr < n and nc >= 0 and nc < n:
                        if board[nr][nc] == 0:
                            board[nr][nc] = board[r][c]
                            board[r][c] = 0
                            r,c = nr,nc
                            continue
                        elif board[nr][nc] == board[r][c]:
                            if (nr,nc) not in check_:
                                board[nr][nc] *=2
                                board[r][c] = 0
                                r,c = nr,nc
                                check_.append((r,c))
                                continue
                            else:
                                break
                        elif board[nr][nc] != board[r][c]:
                            break
        return board

    elif dir == 2: # left
        check_=[]
        for c in range(n):
            for r in range(n):
                if board[r][c] == 0:
                    continue
                while True:
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if nr >= 0  and nr < n and nc >= 0 and nc < n:
                        if board[nr][nc] == 0:
                            board[nr][nc] = board[r][c]
                            board[r][c] = 0
                            r,c = nr,nc
                            continue
                        elif board[nr][nc] == board[r][c]:
                            if (nr,nc) not in check_:
                                board[nr][nc] *=2
                                board[r][c] = 0
                                r,c = nr,nc
                                check_.append((r,c))
                                continue
                            else:
                                break
                        elif board[nr][nc] != board[r][c]:
                            break
        return board

    elif dir == 3: # right
        check_=[]
        for c in range(n-1,-1,-1):
            for r in range(n):
                if board[r][c] == 0:
                    continue
                while True:
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if nr >= 0  and nr < n and nc >= 0 and nc < n:
                        if board[nr][nc] == 0:
                            board[nr][nc] = board[r][c]
                            board[r][c] = 0
                            r,c = nr,nc
                            continue
                        elif board[nr][nc] == board[r][c]:
                            if (nr,nc) not in check_:
                                board[nr][nc] *=2
                                board[r][c] = 0
                                r,c = nr,nc
                                check_.append((r,c))
                                continue
                            else:
                                break
                        elif board[nr][nc] != board[r][c]:
                            break
        return board

def dfs(board,cnt):
    if cnt == 5:
        return max(map(max,board))

    return dfs(moving([j[:] for j in board],0,n),cnt+1), dfs(moving([j[:] for j in board],1,n),cnt+1), dfs(moving([j[:] for j in board],2,n),cnt+1), dfs(moving([j[:] for j in board],3,n),cnt+1)

print(dfs(board,0))