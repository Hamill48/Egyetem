isNotOver = 'yes'

while isNotOver == 'yes':
    instr = input('Művelet: ')
    a, op, b = instr.split(sep=' ')

    if op == '+':
        result = int(a) + int(b)
    elif op == '-':
        result = int(a) - int(b)
    elif op == '/':
        if int(b) != 0:
            result = int(a) / int(b)
        else:
            print('You cannot devide by zero!')
            continue
    elif op == '*':
        result = int(a) * int(b)

    print(result)

    isNotOver = input('Do you want to continue? ')