from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    if  arr[0] > 1:
        ans = 'First'
    else:
        count = 0
        for i in range(n):
            if arr[i] == 1:
                count += 1
            else:
                break
        if count == n and count % 2 == 1:
            ans =  'First'
        elif count == n and count % 2 == 0:
            ans = 'Second'
        elif count < n and count % 2 == 1:
            ans = 'Second'
        elif count < n and count % 2 == 0:
            ans = 'First'
    print(ans)
    t -= 1