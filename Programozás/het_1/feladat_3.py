num = int(input('Give a number: '))

if num > 0:
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        print(round(num))

else:
    print('Only positive numbers!')