from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    s = stdin.readline()
    st = []
    count = 0
    for i in s:
        if i is '(':
            st.append(i)
        elif i is ')' and len(st) > 0:
            st.pop()
        elif i is ')' and len(st) == 0:
            s + ')'
            count += 1
    print(count)
    t -= 1