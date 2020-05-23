from sys import *
t = int(stdin.readline())
while t > 0:
    s = stdin.readline()
    l = 0
    r = 0
    con = 0
    for i in range(len(s)):
        if s[i] == '<':
            l += 1
        elif s[i] == '>':
            r += 1
        if l == r:
            con = r
        elif r > l:
            break
    print(con*2)
    t -= 1
            