a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a < b + c and b < a + c and c < a + b:
    print('It can be a triangle!')
else:
    print('It cannot be a triangle!') 