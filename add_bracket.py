# 16637
n = int(input())
data = input()
exp = [i for i in data]

def cal(x,y,z):
    if y == '+':
        return str(int(x)+int(z))
    if y == '-':
        return str(int(x)-int(z))
    if y == '*':
        return str(int(x)*int(z))

nums = [str(i) for i in range(10)]
ops = ['+','-','*']
ans = -1e9
def dfs(exp):
    global ans
    if ')' in exp[-3:]:
        rslt = 0
        cursor_ = 0
        while cursor_ < len(exp):
            if exp[cursor_] not in ops:
                rslt += int(eval(exp[cursor_]))
                cursor_+=1
            elif exp[cursor_] in ops:
                rslt = cal(rslt,exp[cursor_],eval(exp[cursor_+1]))
                cursor_+=2
        ans = max(ans,int(rslt))
        return
    
    for i in range(len(exp)):
        try:
            if exp[i] in nums and exp[i+1] in ops and exp[i+2] in nums:
                ref = exp[:]
                ref[i] = '('+ref[i]+ref[i+1]+ref[i+2]+')'
                del ref[i+2]
                del ref[i+1]
                dfs(ref)
        except IndexError:
            break
    rslt = 0
    cursor_ = 0
    while cursor_ < len(exp):
        if exp[cursor_] not in ops:
            rslt += int(eval(exp[cursor_]))
            cursor_+=1
        elif exp[cursor_] in ops:
            rslt = cal(rslt,exp[cursor_],eval(exp[cursor_+1]))
            cursor_+=2
    ans = max(ans,int(rslt))
    return
dfs(exp)
print(ans)