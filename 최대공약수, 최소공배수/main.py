n = int(input())
lis = list(map(int, input().split()))
f,s = 0,0
for i in range(min(lis),0,-1):
    for j in lis:
        if j % i:
            break
    else:
        f = i
        break
num = 0
max = max(lis)
while not s:
    num+=1
    for i in lis:
        if max*num % i:
            break
    else:
        s = max*num
print(f,s)
# 브론즈 3
# https://jungol.co.kr/problem/1002