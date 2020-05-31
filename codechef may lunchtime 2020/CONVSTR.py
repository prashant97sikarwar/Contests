def mylove(a,b,n):
    ans = []
    set1 = list(set(a))
    set2 = list(set(b))
    set1.sort(reverse = True)
    set2.sort(reverse = True)
    for i in set2:
        if i not in set1:
            return -1
    d = {}
    for i in range(len(b)):
        if b[i] not in d:
            d[b[i]] = [i]
        else:
            d[b[i]].append(i)
    for i in set2:
        c = 0
        mylst = []
        bv = a.index(i)
        if bv == -1:
            return -1
        for j in range(len(d[i])):
            if ord(a[d[i][j]]) > ord(i):
                a[d[i][j]] = i
            elif ord(a[d[i][j]]) == ord(i):
                c += 1
            else:
                return -1
        if c == len(d[i]):
            continue
        mylst.append(bv)
        mylst.extend(d[i])
        mylst = sorted(list(set(mylst)))
        mylst.insert(0,len(mylst))
        ans.append(mylst)
    return ans 
            
    
    
from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    a = list(stdin.readline())
    b = list(stdin.readline())
    despo = mylove(a,b,n)
    if despo == -1:
        print(-1)
    else:
        print(len(despo))
        for i in despo:
            for j in i:
                print(j,end=' ')
            print()
            
    t-=1
    