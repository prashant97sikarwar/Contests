t = int(input())
while t > 0:
    s = input()
    l = len(s)
    flag = 0
    if l%2 == 0:
        k1 = s[ : l//2]
        k2 = s[l//2 : ]
    if l%2 == 1:
        k1 = s[ : l//2]
        k2 = s[(l//2)+1 : ]
    for i in k1:
        if k1.count(i) == k2.count(i):
            flag = 0
        else:
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")
    t -= 1