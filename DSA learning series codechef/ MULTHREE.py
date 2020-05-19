t = int(input())
while t > 0:
    k, a, b = list(map(int,input().split()))
    if (a + b) % 5 == 0:
        print("NO")
        t -= 1
        continue
    if k == 2:
        if (a+b) % 3:
            print("NO")
        else:
            print("YES")
    else:
        c = (a + b) % 10
        d = (a + b + c) % 10
        rem = (k - 3) % 4
        mul = (k - 3) // 4
        ans = (mul * 20) + (a + b + c)
        p = [d]
        for _ in range(2):
            d = (2*d) % 10
            p.append(d)
        for i in range(rem):
            ans += p[i]
        if ans % 3 == 0:
            print("YES")
        else:
            print("NO")
    t-=1