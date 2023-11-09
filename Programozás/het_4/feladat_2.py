leapDay = 0

for year in range(1800, 2023):
    if year % 4 == 0 and year % 100 != 0:
        leapDay += 1
    elif year % 4 == 0 and year % 400 == 0:
        leapDay += 1

print(leapDay)