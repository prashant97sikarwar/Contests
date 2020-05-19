t = int(input())
while t > 0:
    s = (input())
    n = len(s)
    count = 0
    for i in range(n-1,-1,-1):
        if s[i] != '0':
            break
        else:
            count += 1
    s = s[::-1]
    print(s[count:])
    t -= 1