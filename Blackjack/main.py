import itertools as it
leng,num = map(int, input().split())
lis = list(map(int, input().split()))
max = 0
for i in it.combinations(lis,3):
    e = sum(i)
    if e == num:
        max = e
        break
    if num > e > max:
            max = e
            if max == num:
                break
print(max)
#https://jungol.co.kr/problem/1504