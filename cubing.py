# 5373
t = int(input())
orders = []
for _ in range(t):
    n = int(input())
    sub_orders = list(input().split())
    orders.append((n,sub_orders))

cube = [
    # U
    'w','w','w',
    'w','w','w',
    'w','w','w',
    # L
    'g','g','g',
    'g','g','g',
    'g','g','g',
    # F
    'r','r','r',
    'r','r','r',
    'r','r','r',
    # R
    'b','b','b',
    'b','b','b',
    'b','b','b',
    # B
    'o','o','o',
    'o','o','o',
    'o','o','o',
    # D
    'y','y','y',
    'y','y','y',
    'y','y','y'
]
ref_cube = [
    # U
    'w','w','w',
    'w','w','w',
    'w','w','w',
    # L
    'g','g','g',
    'g','g','g',
    'g','g','g',
    # F
    'r','r','r',
    'r','r','r',
    'r','r','r',
    # R
    'b','b','b',
    'b','b','b',
    'b','b','b',
    # B
    'o','o','o',
    'o','o','o',
    'o','o','o',
    # D
    'y','y','y',
    'y','y','y',
    'y','y','y'
]

def show_cude(cude):
    cnt = 1
    for i in cude[:9]:
        print(i,end='')
        if cnt % 3 == 0:
            print()
        cnt+=1

def turn_cube(s,d):
    # ref_cube = cube[:]
    if s == 'U':
        if d == '+':
            cube[9:12] = ref_cube[18:21]
            cube[18:21] = ref_cube[27:30]
            cube[27:30] = ref_cube[36:39]
            cube[37:39] = ref_cube[9:12]
        else:
            cube[9:12] = ref_cube[36:39]
            cube[18:21] = ref_cube[9:12]
            cube[27:30] = ref_cube[18:21]
            cube[37:39] = ref_cube[27:30]
    elif s == 'D':
        if d == '+':
            cube[15:18] = ref_cube[42:25]
            cube[24:27] = ref_cube[15:18]
            cube[33:36] = ref_cube[24:27]
            cube[42:45] = ref_cube[33:36]
        else:
            cube[15:18] = ref_cube[24:27]
            cube[24:27] = ref_cube[33:36]
            cube[33:36] = ref_cube[42:45]
            cube[42:45] = ref_cube[15:18]
    elif s == 'F':
        if d == '+':
            cube[6],cube[7],cube[8] = ref_cube[17], ref_cube[14], ref_cube[11]
            cube[27],cube[30],cube[33] = ref_cube[6], ref_cube[7], ref_cube[8]
            cube[47],cube[46],cube[45] = ref_cube[27], ref_cube[30], ref_cube[33]
            cube[17],cube[14],cube[11] = ref_cube[47], ref_cube[46], ref_cube[45]
        else:
            cube[6],cube[7],cube[8] = ref_cube[27], ref_cube[30], ref_cube[33]
            cube[27],cube[30],cube[33] = ref_cube[47], ref_cube[46], ref_cube[45]
            cube[47],cube[46],cube[45] = ref_cube[17], ref_cube[14], ref_cube[11]
            cube[17],cube[14],cube[11] = ref_cube[6], ref_cube[7], ref_cube[8]
    elif s == 'B':
        if d == '+':
            cube[0],cube[1],cube[2] = ref_cube[15], ref_cube[12], ref_cube[9]
            cube[29],cube[32],cube[35] = ref_cube[0], ref_cube[1], ref_cube[2]
            cube[53],cube[52],cube[51] = ref_cube[29], ref_cube[32], ref_cube[35]
            cube[15],cube[12],cube[9] = ref_cube[53], ref_cube[52], ref_cube[51]
        else:
            cube[0],cube[1],cube[2] = ref_cube[29], ref_cube[32], ref_cube[35]
            cube[29],cube[32],cube[35] = ref_cube[53], ref_cube[52], ref_cube[51]
            cube[53],cube[52],cube[51] = ref_cube[15], ref_cube[12], ref_cube[9]
            cube[15],cube[12],cube[9] = ref_cube[0], ref_cube[1], ref_cube[2]
    elif s == 'L':
        if d == '+':
            cube[0],cube[3],cube[6] = ref_cube[44], ref_cube[42], ref_cube[38]
            cube[18],cube[21],cube[24] = ref_cube[0], ref_cube[3], ref_cube[6]
            cube[45],cube[48],cube[51] = ref_cube[18], ref_cube[21], ref_cube[24]
            cube[44],cube[43],cube[42] = ref_cube[45], ref_cube[48], ref_cube[51]
        else:
            cube[0],cube[3],cube[6] = ref_cube[18], ref_cube[21], ref_cube[24]
            cube[18],cube[21],cube[24] = ref_cube[45], ref_cube[48], ref_cube[51]
            cube[45],cube[48],cube[51] = ref_cube[44], ref_cube[42], ref_cube[38]
            cube[44],cube[43],cube[42] = ref_cube[0], ref_cube[3], ref_cube[6]
    elif s == 'R':
        if d == '+':
            cube[2],cube[5],cube[8] = ref_cube[20], ref_cube[23], ref_cube[26]
            cube[20],cube[23],cube[26] = ref_cube[47], ref_cube[50], ref_cube[53]
            cube[48],cube[50],cube[53] = ref_cube[42], ref_cube[39], ref_cube[36]
            cube[42],cube[39],cube[36] = ref_cube[2], ref_cube[5], ref_cube[8]
        else:
            cube[2],cube[5],cube[8] = ref_cube[42], ref_cube[39], ref_cube[36]
            cube[20],cube[23],cube[26] = ref_cube[2], ref_cube[5], ref_cube[8]
            cube[48],cube[50],cube[53] = ref_cube[20], ref_cube[23], ref_cube[26]
            cube[42],cube[39],cube[36] = ref_cube[47], ref_cube[50], ref_cube[53]
            
for _,order in orders:
    for sub_order in order:
        side, direction = sub_order[0], sub_order[1]
        turn_cube(side,direction)
    show_cude(cube)
    cube = ref_cube[:]