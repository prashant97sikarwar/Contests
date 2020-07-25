import sys
input = sys.stdin.readline
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    mx =  max(arr)
    ans =   ['a' * (mx + 1)] * (n+1)
    for i,x in enumerate(arr):
        tag = 'a' if ans[i][x] == 'b' else 'b'
        ans[i+1] = ans[i][:x] + tag + ans[i][x+1:]
    print('\n'.join(ans))    
    t -= 1