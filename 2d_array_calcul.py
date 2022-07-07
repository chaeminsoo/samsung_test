# 17140
r,c,k = map(int,input().split())
board = []
for _ in range(3):
    board.append(list(map(int,input().split())))

def s_sort(l):
    d_result = {}
    for i in l:
        if i !=0:
            try:
                d_result[i] += 1
            except KeyError:
                d_result[i] = 1
    rslt = list(d_result.items())
    rslt.sort(key= lambda x:(x[1], x[0]))
    real_rslt = []
    for j in rslt:
        a,b = j
        real_rslt.append(a)
        real_rslt.append(b)
    return real_rslt

def td_turn(l):
    a = zip(*l[::-1])
    return [list(i) for i in a]

def calcul(board):
    r_len = len(board)
    c_len = len(board[0])
    max_len = 0
    if  r_len >= c_len:
        for i in range(r_len):
            board[i] = s_sort(board[i])
            max_len = max(max_len,len(board[i]))
        for i in range(r_len):
            while len(board[i]) < max_len:
                board[i].append(0)
            if len(board[i]) > 100:
                board[i] = board[i][:100]
        return board
    else:
        for _ in range(3):
            board = td_turn(board)
        for i in range(c_len):
            board[i] = s_sort(board[i])
            max_len = max(max_len,len(board[i]))
        for i in range(c_len):
            while len(board[i]) < max_len:
                board[i].append(0)
            if len(board[i]) > 100:
                board[i] = board[i][:100]
        board = td_turn(board)
        return board

for ans in range(102):
    try:
        if board[r-1][c-1] == k:
            break
        else:
            board = calcul(board)
    except IndexError:
        board = calcul(board)
        pass
if ans <= 100:
    print(ans)
else:
    print(-1)