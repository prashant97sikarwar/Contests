from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    flag = 0
    l = [False] * (max(arr)+2)
    for i in range(n-1):
        if arr[i] != arr[i+1] and l[arr[i+1]] == False:
            l[arr[i]] = True
        if l[arr[i+1]] == True:
            flag = 1
            break
    count = 0
    s = {}
    for i in range(n):
        if arr[i] not in s.keys():
            s[arr[i]] = 1
        else:
            s[arr[i]] += 1
    d = set()
    flag2 = 0
    for x in s:
        if s[x] not in d:
            d.add(s[x])
        else:
            flag2 = 1
            break
    if flag or flag2:
        ans = 'NO'
    else:
        ans = 'YES'
    print(ans)
    t -= 1
        