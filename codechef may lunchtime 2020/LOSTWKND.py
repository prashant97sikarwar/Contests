from sys import *
t = int(stdin.readline())
while t > 0:
    arr = list(map(int,stdin.readline().split()))
    p = arr.pop()
    total = 0
    for i in range(5):
        total += arr[i]
    fg = p * total
    if fg/24 > 5:
        print("Yes")
    else:
        print("No")
    t -= 1