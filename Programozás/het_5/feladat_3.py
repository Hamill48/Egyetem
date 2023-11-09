def isPrime(number):
    divider = 0
    for i in range(number + 1):
        if i == 0:
            continue
        elif number % i == 0:
            divider += 1
    if divider == 2:
        print('The number is prime!')
    else:
        print('The number is not prime!')

isPrime(20)
