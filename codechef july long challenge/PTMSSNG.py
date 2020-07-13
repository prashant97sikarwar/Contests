from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    x = []
    y = []
    for i in range(4*n - 1):
        m,n = map(int,stdin.readline().split())
        x.append(m)
        y.append(n)
    de = x[0]
    rt = y[0]
    for i in range(1,len(x)):
        de = de ^ x[i]
    for j in range(1,len(y)):
        rt = rt ^ y[j]
    print(de,rt)
    t -= 1
    
    