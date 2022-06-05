# 14890
n,l = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def counting_roads(board):
    cnt = 0
    for i in board:
        cursor1 = 0
        cursor2 = 0
        ramp = [False]*n
        road_okay = True
        while cursor2 < n:
            if i[cursor1] == i[cursor2]:
                cursor2+=1
                continue
            else:
                if i[cursor1] - i[cursor2] == -1:
                    r_cnt = 0
                    for j in range(cursor1,cursor2):
                        if not ramp[j]:
                            ramp[j] = True
                            r_cnt+=1
                    if r_cnt >= l:
                        cursor1 = cursor2
                        continue
                    else:
                        road_okay = False
                        break

                if i[cursor1] - i[cursor2] == 1:
                    r_cnt = 0
                    try:
                        for j in range(cursor2,cursor2+l):
                            if i[j] == i[cursor2] and not ramp[j]:
                                ramp[j] = True
                                r_cnt+=1
                    except IndexError:
                        pass
                    if r_cnt >= l:
                        cursor2 += (l-1)
                        cursor1 = cursor2
                    else:
                        road_okay = False
                        break
                    
                else:
                    road_okay = False
                    break
                    
        if road_okay:
            cnt+=1
            # print(i)

    return cnt

ans = 0
ans += counting_roads(board)
ans += counting_roads(rotated(board))
print(ans)