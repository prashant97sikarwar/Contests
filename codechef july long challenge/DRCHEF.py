from sys import *
t = int(stdin.readline())
while t > 0:
    n,x = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    left = n
    ans = 0
    mn = 0
    arr.sort()
    while (left > 0):
        while (x < arr[mn]):
            x = x << 1
            ans += 1
        another = -1
        ans += 1
        for i in range(n-1,-1,-1):
            if (arr[i] != -1):
                if (arr[i] <= x):
                    another = i
                    break
        new = arr[another] << 1
        if new <= x:
            my_var = another + 1
            if (my_var != len(arr)):
                x = x << 1
            else:
                x = arr[another] << 1
                left -= 1
                arr.insert(another,-1)
                arr.pop(another)
        else:
            x = arr[another] << 1
            left -= 1
            arr.insert(another,-1)
            if (another == mn):
                mn += 1
            arr.pop(another)
    print(ans)
    t -= 1