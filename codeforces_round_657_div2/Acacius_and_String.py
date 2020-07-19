from sys import *
def count(ss,n):
    cnt = 0
    for i in range(n-7+1):
        if ss[i:i+7] == 'abacaba':
            cnt += 1
    return cnt

t = int(stdin.readline())
ref = 'abacaba'
while t > 0:
    n = int(stdin.readline())
    s = stdin.readline()
    gf = False
    for i in range(n-7+1):
        ss = list(s)
        flag = True
        for j in range(7):
            if ss[i+j] != '?' and ref[j] != ss[i+j]:
                flag = False
                break
            ss[i+j] = ref[j]
        ss = ''.join(ss)
        if flag and count(ss,n) == 1:
            ss = list(ss)
            for j in range(n):
                if ss[j] == '?':
                    ss[j] = 'z'
            gf = True
            print("yes")
            print(''.join(ss),end='')
            break
    if gf == False:
        print("no")
    t -= 1
                