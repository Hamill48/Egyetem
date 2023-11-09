from cmath import sqrt


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

gyokAlatt = ((b**2) - 4 * a * c)

if gyokAlatt >= 0:
    x1 = (- b + sqrt(gyokAlatt)) / 2 * a
    x2 = (- b - sqrt(gyokAlatt)) / 2 * a
    print(f'x1 = {x1}, x2 = {x2}')
else:
    print('Gyök alatt minusz!')