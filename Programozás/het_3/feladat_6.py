points = int(input('Pontok száma: '))

if points >= 90:
    result = 'Jeles'
elif points < 90 and points >= 80:
    result = 'Jó'
elif points < 80 and points >= 70:
    result = 'Közepes'
elif points < 70 and points >= 60:
    result = 'Elégséges'
elif points < 60:
    result = 'Elégtelen'
else:
    print('Érvénytelen pontszám!')

print(result)