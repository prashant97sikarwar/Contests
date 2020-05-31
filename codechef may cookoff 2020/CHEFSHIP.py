t = int(input())
for j in range(t):
    s = input()
    count = 0
    n = len(s)
    for i in range(2,n,2):
        if s[0:(i//2)] == s[(i//2):i] and s[i:((i+n)//2)] == s[((i+n)//2):n]:
            count += 1
    print(count)
    