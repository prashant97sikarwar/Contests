n = int(input())
s = input()
cw = 0
lol = 0
for i in s:
    if i == 'W':
        cw += 1
for i in range(n-1,n-cw-1,-1):
    if s[i] == 'W':
        lol += 1
print(abs(lol-cw))