t = int(input())
d = dict()
d['TLE'] = 0
d['AC'] = 0
d['WA'] = 0
d['RE'] = 0
while t > 0:
    s = input()
    if s == 'TLE':
        d['TLE'] += 1
    elif s == 'WA':
        d['WA'] += 1
    elif s == 'RE':
        d['RE'] += 1
    elif s == 'AC':
        d['AC'] += 1
    t-=1
print('AC', 'x' ,d['AC'])
print('WA', 'x' ,d['WA'])
print('TLE', 'x' ,d['TLE'])
print('RE', 'x' ,d['RE'])
    