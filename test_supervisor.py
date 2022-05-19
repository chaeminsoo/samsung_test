#13458
n = int(input())
test_room = list(map(int, input().split()))
b,c = map(int,input().split())
cnt = 0
for a in test_room:
    a -= b
    cnt += 1
    if a > 0:
        share = a//c
        rest = a%c
        cnt += share
        if rest != 0:
            cnt += 1
print(cnt)