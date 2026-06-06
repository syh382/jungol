while True:
    count,legs = map(int,input().split())
    if not count and not legs:
        break
    if 0 <= count <= 1000 and 0 <= legs <= 4000:
        if count*2 <= legs <= count*4 and not legs % 2:
            r = (count*4 - legs)//2
            print(count-r, r)
        else:
            print(0)
    else:
        print("INPUT ERROR!")
# 브론즈 2
# https://jungol.co.kr/problem/1001