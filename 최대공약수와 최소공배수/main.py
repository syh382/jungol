a,b = map(int,input().split())
def f(a,b):
    if a%b:
        return f(b,a%b)
    else:
        return b
r = f(max(a,b),min(a,b))
print(r)
print(a*b//r)
#https://jungol.co.kr/problem/1658?cursor=IjU5MCIsMSwx