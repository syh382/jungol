from statistics import pstdev #모표준편차 함수
import math as m
n = int(input())
lis = [int(input()) for i in range(n)]
p,po = m.floor((sum(lis)/n+0.05)*10)/10,m.floor((pstdev(lis)+0.05)*10)/10
print(sum(lis))
print(p if p % 1 else int(p))
print(po if po % 1 else int(po))
# 브론즈 3
# https://jungol.co.kr/problem/1004
