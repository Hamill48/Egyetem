'''Masodfiku egyenlet megoldasa
be: 3 konstans
ki: valos gyok(ok)
Diszkriminans: (b^2 - 4ac)
    - > 0 => ket gyok
    - = 0 => egy gyok
    - <0 => nincs valos gyok
'''
import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (b * -1 + math.sqrt(d)) / (2 * a)
    x2 = (b * -1 - math.sqrt(d)) / (2 * a)
    print(f'x1: {x1} x2: {x2}')
elif d == 0:
    x = (b * -1) / (2 * a)
    print(f'x: {x}')
else:
    print('No real square root of discriminant.')