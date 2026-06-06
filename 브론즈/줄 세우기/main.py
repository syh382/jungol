n = int(input())
lis = list(map(int, input().split()))
result = []
for i in range(n):
    result.insert(i-lis[i],i+1)
print(*result)
# 브론즈 1
# https://jungol.co.kr/problem/1003