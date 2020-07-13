from sys import *
t = int(stdin.readline())
while t > 0:
    k = int(stdin.readline())
    mat = [['X' for i in range(8)] for j in range(8)]
    mat[0][0] = 'O'
    l = k//8
    s = k - 8*l
    if l == 0:
        for i in range(1,s):
            mat[0][i] = '.'
    else:
        for i in range(l):
            for j in range(8):
                if mat[i][j] == 'X':
                    mat[i][j] = '.'
        for i in range(s):
            mat[l][i] =  '.'
    for i in range(8):
        for j in range(8):
            print(mat[i][j],end='')
        print()
    t -= 1