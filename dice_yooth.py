# 17825
board = [
    [0,1,2,3,4,5],
    [1,2,3,4,5,6],
    [2,3,4,5,6,7],
    [3,4,5,6,7,8],
    [4,5,6,7,8,9],
    [5,22,23,24,25,31],
    [6,7,8,9,10,11],
    [7,8,9,10,11,12],
    [8,9,10,11,12,13],
    [9,10,11,12,13,14],
    [10,29,30,25,31,32],
    [11,12,13,14,15,16],
    [12,13,14,15,16,17],
    [13,14,15,16,17,18],
    [14,15,16,17,18,19],
    [15,28,27,26,25,31],
    [16,17,18,19,20,21],
    [17,18,19,20,21,21],
    [18,19,20,21,21,21],
    [19,20,21,21,21,21],
    [20,21,21,21,21,21],
    [21,21,21,21,21,21],
    [22,23,24,25,31,32],
    [23,24,25,31,32,20],
    [24,25,31,32,20,21],
    [25,31,32,20,21,21],
    [26,25,31,32,20,21],
    [27,26,25,31,32,20],
    [28,27,26,25,31,32],
    [29,30,25,31,32,20],
    [30,25,31,32,20,21],
    [31,32,20,21,21,21],
    [32,20,21,21,21,21]
]

board_num = [0, 2, 4, 6, 8, 10, 12, 14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,13,16,19,25,26,27,28,22,24,30,35]

dice_num = list(map(int,input().split()))
ans = 0

def dfs(num,now_sum,horse):
    global ans
    if num == 10:
        ans = max(ans,now_sum)
        return
    
    for i in range(4):
        x = horse[i] # 돌아가기 위함
        horse[i] = board[x][dice_num[num]]
        if horse.count(horse[i]) == 1 or horse[i] == 21:
            dfs(num+1, now_sum + board_num[horse[i]], horse)
        horse[i] = x

dfs(0,0,[0,0,0,0])
print(ans)