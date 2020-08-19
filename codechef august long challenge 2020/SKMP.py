t = int(input())
while t > 0:
    s = input()
    p = input()
    d = dict()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    for i in range(len(p)):
        d[p[i]] -= 1
    ans = p
    flag1 = ""
    flag2 = ""
    for i in sorted(d.keys()):
        if ord(i) < ord(ans[0]) and d[i] > 0:
            flag1 += d[i]*i
        elif ord(i) == ord(ans[0]) and d[i] > 0:
            j = 0
            while ord(i) == ord(ans[j]):
                j += 1
            if ord(i) > ord(ans[j]):
                flag2 += d[i]*i
            else:
                flag1 += d[i]*i
        elif d[i] > 0:
            flag2 += d[i]*i
    print(str(flag1+ans+flag2))
    t -= 1 
    