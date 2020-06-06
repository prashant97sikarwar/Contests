from sys import *
t = int(stdin.readline())
while t > 0:
    s = stdin.readline()
    n = len(s)
    i = 0
    count = 0
    while i < n:
        if s[i] == 'x' and s[i+1] == 'y':
            count += 1
            i += 2
        elif s[i] == 'y' and s[i+1] == 'x':
            count += 1
            i += 2
        else:
            i += 1
    print(count)
    t -= 1