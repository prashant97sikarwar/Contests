from sys import *
import re
t = int(stdin.readline())
while t > 0:
    n,o =  stdin.readline().split()
    ans = 0
    for i in range(int(n)):
        des = stdin.readline()
        if 'CONTEST_WON' in des:
            fr = re.findall(r'\d+',des)
            rank = int(fr[0])
            if rank < 20:
                ans = ans + 300 + (20-rank)
            else:
                ans += 300
        if 'TOP_CONTRIBUTOR' in des:
            ans += 300
        if 'CONTEST_HOSTED' in des:
            ans += 50
        if 'BUG_FOUND' in des:
            my = re.findall(r'\d+',des)
            y = int(my[0])
            ans += y
    if o == 'NON_INDIAN':
        ds = ans//400
    else:
        ds = ans//200
    print(ds)
    t-=1