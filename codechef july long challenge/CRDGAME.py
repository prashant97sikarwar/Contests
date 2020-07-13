from sys import *
def fun(p):
    total = 0
    while p > 0:
        total += (p % 10)
        p = p//10
    return total

t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    t1 = 0
    t2 = 0
    for i in range(n):
        p,q = map(int,stdin.readline().split())
        p1 = fun(p)
        p2 = fun(q)
        if p1 > p2:
           t1 += 1
        elif p1 == p2:
            t1 += 1
            t2 += 1
        else:
            t2 += 1
    if t1 > t2:
        print(0,t1)
    elif t1 == t2:
        print(2,t1)
    else:
        print(1,t2)
    t -= 1
    