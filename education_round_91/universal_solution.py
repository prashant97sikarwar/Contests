from sys import *
t = int(stdin.readline())
while t > 0:
    s = stdin.readline()
    d = dict()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    dk = max(d, key = d.get)
    if dk == 'R':
        ans = 'P'
    if dk == 'P':
        ans = 'S'
    if dk == 'S':
        ans = 'R'
    l = [ans for i in range(len(s)-1)]
    print(''.join(l))
    t-=1