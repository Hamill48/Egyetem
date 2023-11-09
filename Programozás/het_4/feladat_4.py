typeOfCall = 0
lengthOfCall = 1

while typeOfCall != '' or lengthOfCall != '':
    typeOfCall = int(input('The type of call: '))
    lengthOfCall = int(input('Length of the call (min): '))

    if lengthOfCall < 1:
        lengthOfCall = 1

    if typeOfCall == 1:
        price = lengthOfCall * 40
    elif typeOfCall == 2:
        price = lengthOfCall * 60
    elif typeOfCall == 3:
        price = lengthOfCall * 100
    else:
        print('Invalid type of call!')
    print(f'The price of your is call: {price}Ft.')