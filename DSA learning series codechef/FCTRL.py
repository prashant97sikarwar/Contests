t = int(input())
while t > 0:
    n = int(input())
    count = 1
    ans = 0
    s = 1
    while s > 0:
        s = n//(5**count)
        count += 1
        ans += s
    print(ans)
    t -= 1
        