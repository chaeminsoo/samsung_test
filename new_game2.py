# 17837
n,k = map(int,input().split())
piece_board = [[[] for _ in range(n)] for _ in range(n)]
color_board = []
for _ in range(n):
    color_board.append(list(map(int,input().split())))

for i in range(k):
    r,c,d = map(int,input().split())
    piece_board[r][c].append((d,i+1))

#1~4: rlud
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

def moving(b):
    for i in range(n):
        for j in range(n):
            if piece_board[i][j]:
                all_pieces = piece_board[i][j]
                l_p = all_pieces[0]
                bnt = 0
                
                nx = i + dx[l_p[0]]
                ny = j + dy[l_p[0]]