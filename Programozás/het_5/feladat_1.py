def collatzNumber(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

try:
    number = int(input('Give a positive whole number: '))
    if number > 0:
        collatzNumber(number)
    else:
        print('Number must be greater than 0!')
except:
    print('Wrong input!')
