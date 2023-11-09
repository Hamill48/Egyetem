import math

t = int(input('Years: '))
c = 10000
r = 8 / 100
m = 12

fv = c * (pow(1 + (r / m), m * t))

print(fv)