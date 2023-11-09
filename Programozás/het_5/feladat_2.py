numbers = []

def codeBreaker():
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    code = sum(numbers)
    print(f'The code is: {code}')

codeBreaker()