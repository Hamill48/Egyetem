year = int(input('Year: '))

if year % 4 == 0 and year % 100 != 0:
    print('It is leap day!')
elif year % 4 == 0 and year % 400 == 0:
    print('It is leap day!')
else:
    print('It is not leap day!')