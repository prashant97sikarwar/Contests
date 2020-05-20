t = int(input())
while t > 0:
    n = int(input())
    arr = input()
    count = 0
    red = 0
    i = 0
    j = 1
    lap = 0
    lap2 = 0
    mess = 0
    while i < 2*n and j < 2*n :
        lap2 += 1
        mess += 1
        if arr[i] == '1':
            count += 1
            if count > red + (n-lap):
                ans = mess
                break
        if red > count + (n - lap2):
                ans = mess
                break
        lap += 1
        mess += 1
        if arr[j] == '1':
            red += 1
            if red > count + (n - lap2):
                ans = mess
                break
        if count > red + (n-lap):
            ans = mess
            break
        i += 2
        j += 2
        if i >= 2*n or j >= 2*n:
            ans = 2*n
        
    print(ans)
    t -= 1