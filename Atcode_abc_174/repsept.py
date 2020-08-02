def solve(n):
    if (n % 2 == 0) or (n % 5 == 0):
        print(-1)
    else:
        k = 7
        count = 1
        while True:
            if k % n == 0:
                print(count)
                break
            if count > n:
                print(-1)
                break
            else:
                k = 10*(k%n) + 7
                count += 1
n = int(input())
solve(n)