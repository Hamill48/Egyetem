number = int(input('Give a number to get the name of the day: '))

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

if number > 0 and number <= 7:
    print(days[number])
elif number == 0:
    print('Invalid number!')
else:
    print('Invalid number!')