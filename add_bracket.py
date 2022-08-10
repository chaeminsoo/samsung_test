# 16637
from collections import deque

n = int(input())
data = input()
exp = [i for i in data]
print(exp)

def cal(x,y,t):
    if t == '+':
        return str(int(x)+int(y))
    if t == '-':
        return str(int(x)-int(y))
    if t == '*':
        return str(int(x)*int(y))

nums = [str(i) for i in range(10)]
opers = ['+','-','*']

def checking(exp):
    return

ans = 0
def dfs(exp):
    global ans
    if ')' in exp[-3:]:
        rslt = deque()
        cursor_ = 0
        while cursor_ < len(exp):
            if exp[cursor_] in nums or exp[cursor_] in opers:
                rslt.append(exp[cursor_])
            else:
                ref_1 = []
                cursor_+=1
                while exp[cursor_] in nums or exp[cursor_] in opers:
                    ref_1.append(exp[cursor_])
                    cursor_+=1
                ref_2 = cal(ref_1[0],ref_1[2],ref_1[1])
                rslt.append(ref_2)
        result = rslt.popleft()
        while rslt:
            op = rslt.popleft()
            numnum = rslt.popleft()
            result = cal(result,numnum,op)
        ans = max(ans,int(result))
        return

    for i in range(len(exp)):
        if exp[i] in nums and exp[i+1] in opers and exp[i+2] in nums:
            ref = exp[:]
            exp.insert(i,'(')
            exp.insert(i+4,')')
            dfs(exp)
            exp = ref[:]
    rslt = deque()
    cursor_ = 0
    while cursor_ < len(exp):
        if exp[cursor_] in nums or exp[cursor_] in opers:
            rslt.append(exp[cursor_])
        else:
            ref_1 = []
            cursor_+=1
            while exp[cursor_] in nums or exp[cursor_] in opers:
                ref_1.append(exp[cursor_])
                cursor_+=1
            ref_2 = cal(ref_1[0],ref_1[2],ref_1[1])
            rslt.append(ref_2)
    result = rslt.popleft()
    while rslt:
        op = rslt.popleft()
        numnum = rslt.popleft()
        result = cal(result,numnum,op)
    ans = max(ans,int(result))
dfs(exp)
print(ans)