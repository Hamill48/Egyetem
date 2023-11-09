actualTime = int(input('What hour is it? '))
whenAlert = int(input('After how many hours do you want the alarm? '))

alertTime = actualTime + whenAlert

print(f'The clock will alarm at: {alertTime % 24}')