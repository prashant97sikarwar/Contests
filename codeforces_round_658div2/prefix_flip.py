from sys import *
t = int(stdin.readline())
for _i in range(t):
    n = int(stdin.readline())
    a = stdin.readline()
    b = stdin.readline()
    l = []
    count = 0
    for i in range(n):
        if a[i] != b[i]:
            l.append(i+1)
            count += 1
    if count == 0:
        print(count)
    else:
        print(3*count,end=' ')
        for j in range(len(l)):
            print(l[j],1,l[j],end=' ')
        print()