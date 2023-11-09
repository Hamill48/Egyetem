date = input('Date: ')
y, m, d = date.split(sep='.')
y = int(y)
m = int(m)
d = int(d)
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def dayOfTheYear():
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        months[2] = 29
    days = d + sum(months[:m])
    return days

result = dayOfTheYear()

print(f'The number of days in this year: {result}')