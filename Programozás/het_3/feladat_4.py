numberOfStartDay = int(input('What number of day will you go? '))
lengthOfDay = int(input('How many days will you be there? '))
leaveDay = (numberOfStartDay + lengthOfDay) % 8

if leaveDay == 0:
    leaveDay = 1

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

if numberOfStartDay != 0 and numberOfStartDay <= 7:
    print(f'You will be leave on: {days[leaveDay]}')
else:
    print('Invalid starting day number!')